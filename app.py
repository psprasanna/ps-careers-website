from flask import Flask
# print(__name__)
app = Flask(__name__)

@app.route("/")
def helloworld():
  return 'hello world printed from app.py'

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug = True)
