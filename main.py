from flask import *
app=Flask(__name__)
app.secret_key='Om'
@app.route('/')
def o():
    return redirect(url_for('home'))
@app.route('/index')
def home():
    return render_template('index.html')
@app.route('/login',methods=['GET','POST'])
def login():
    error=None
    if request.method=='POST':
        if request.form['pass']!='Om':
            error='invalid password'
        else:
            flash('Successfully logged in')
            return "Logged in"
    return render_template('login.html',error=error)
if __name__=='__main__':
    app.run(debug=True)