from flask import Flask
app = Flask(__name__)

@app.route("/rev/<float:revNo>")
def hello(revNo):
    return "the float value is: %f" % revNo

if __name__ == "__main__":
    app.run(debug = True)


"""
program not excuted
"""