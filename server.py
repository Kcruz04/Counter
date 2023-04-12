from flask import Flask, render_template, request, redirect, session
# don't forget to import redirect!
app = Flask(__name__)
app.secret_key = "secret"
# set a secret key for security purposes



@app.route('/')
def index():
    if 'count' not in session:
        session['count']=0
    session['count']+= 1
    return render_template('index.html')

@app.route('/clear')
def clear():
    session.clear()		# clears all keys
    return redirect('/')


if __name__=="__main__":
    app.run(debug = True, port = 5001)