from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


def get_quizzes():
    con = sqlite3.connect("hvahoot.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM quizzes")
    quizzes = cur.fetchall()
    con.close()
    return quizzes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    quizzes = get_quizzes() 
    if request.method == 'POST':
        selected_answer = request.form['answer']
        correct_answer = request.form['correct_answer']
        if selected_answer == correct_answer:
            
            return redirect(url_for('quiz1'))
        else:
            
            return render_template('quiz.html', quizzes=quizzes, message="Feil svar, prøv igjen.")
    
    return render_template('quiz.html', quizzes=quizzes)

@app.route('/quiz1', methods=['GET', 'POST'])
def quiz1():
    quizzes = get_quizzes() 
    if request.method == 'POST':
        selected_answer = request.form['answer']
        correct_answer = request.form['correct_answer']
        if selected_answer == correct_answer:
            
            return redirect(url_for('quiz2'))
        else:
            
            return render_template('quiz1.html', quizzes=quizzes, message="Feil svar, prøv igjen.")
    
    return render_template('quiz1.html', quizzes=quizzes)

@app.route('/quiz2', methods=['GET', 'POST'])
def quiz2():
    quizzes = get_quizzes() 
    if request.method == 'POST':
        selected_answer = request.form['answer']
        correct_answer = request.form['correct_answer']
        if selected_answer == correct_answer:
            
            return redirect(url_for('quiz3'))
        else:
            
            return render_template('quiz2.html', quizzes=quizzes, message="Feil svar, prøv igjen.")
    
    return render_template('quiz2.html', quizzes=quizzes)

@app.route('/quiz3', methods=['GET', 'POST'])
def quiz3():
    quizzes = get_quizzes() 
    if request.method == 'POST':
        selected_answer = request.form['answer']
        correct_answer = request.form['correct_answer']
        if selected_answer == correct_answer:
            
            return redirect(url_for('quiz4'))
        else:
            
            return render_template('quiz3.html', quizzes=quizzes, message="Feil svar, prøv igjen.")
    
    return render_template('quiz3.html', quizzes=quizzes)
@app.route('/quiz4', methods=['GET', 'POST'])
def quiz4():
    quizzes = get_quizzes() 
    if request.method == 'POST':
        selected_answer = request.form['answer']
        correct_answer = request.form['correct_answer']
        if selected_answer == correct_answer:
            
            return redirect(url_for('correct'))
        else:
            
            return render_template('quiz4.html', quizzes=quizzes, message="Feil svar, prøv igjen.")
    
    return render_template('quiz4.html', quizzes=quizzes)

@app.route('/correct')
def correct():
    
    return render_template('correct.html')

if __name__ == '__main__':
    app.run(debug=True)
