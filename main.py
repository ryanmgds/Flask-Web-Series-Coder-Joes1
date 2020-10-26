
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home(): 
    return render_template("home.html")

@app.route('/main')
def main():
  return render_template("main.html")

@app.route('/healthylunches')
def healthylunches():
  return render_template("healthylunches.html") 


@app.route('/tastydesserts')
def tastydesserts():

  desserts = [
    {
      "name":"cheesecake",
      "price":10
    },

    {
      "name":"ice cream",
      "price":15
    },
  ]

  return render_template("tastydesserts.html", desserts=desserts)

@app.route('/healthydinners')
def healthydinners():
  return render_template("healthydinners.html")

@app.route('/shoppingbag')
def shoppingbag():
  return render_template("shoppingbag.html")


if __name__ == "__main__":
    app.run(debug=True, port='3000', host='0.0.0.0')


