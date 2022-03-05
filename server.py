from flask import Flask, render_template, request, redirect, session

import random 

app = Flask(__name__)  
app.secret_key = 'safekey'

@app.route('/')
def index():
    session.clear()
    print(session)
    return render_template('index.html')

@app.route('/userguess', methods=['POST'])
def submit_guess():
    print('Got Post Info')
    print(request.form)
    session['user_guess'] = request.form['user_guess']
    return redirect ('/guess')

@app.route('/guess')
def show_guess():
    print('Showing Session:')
    print(session)
    print ('Showing User Guess From the Form')
    print(request.form)
    random_num = random.randint(1,100)
    print(f'Random number is:', random_num)
    if int(session['user_guess']) > random_num:
        print("Too High!")
        session['answer'] = 'too High'
        return render_template('highguess.html', guess_on_template=session['user_guess'])
    if int(session['user_guess']) < random_num:
        print("Too Low!")
        session['answer'] = 'too Low'
        return render_template('lowguess.html', guess_on_template=session['user_guess'])
    if int(session['user_guess']) == random_num: 
        print("Correct!")
        session['answer'] = 'Correct'
        return render_template('correctguess.html', guess_on_template=session['user_guess'])





if __name__ == "__main__":
    app.run(debug=True)











