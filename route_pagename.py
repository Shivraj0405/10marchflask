from flask import Flask
app = Flask(__name__)



@app.route("/hello")
def hello_world():
   return "well-come to python world"

if __name__ == '__main__':
   app.run()