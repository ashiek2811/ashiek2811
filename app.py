from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('home.html',name="ashiek")




if __name__ == '__main__':
   app.run(debug = True)