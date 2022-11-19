from flask import Flask, render_template
app = Flask(__name__)
 

@app.route('/')
def login():
   return render_template("index.html")

@app.route('/base'   )
def login1():
   return render_template("base.html")   

@app.route('/cards' )
def login2():
   return render_template("cards.html")   

if __name__ == '__main__':
  app.run(debug=True)