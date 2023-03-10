# from flask import Flask
# app = Flask(__name__)
#
# @app.route("/blog/<int:postID>")
# def show_blog(postID):
#     return "show blog ID: %d" %postID
#
# if __name__ == "__main__":
#     app.run()

from flask import Flask
app = Flask(__name__)

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

if __name__ == '__main__':
   app.run()

""" 
note - 
program not working
"""