from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello Swati"

if __name__ == "__main__":
  print("I am inside If")
  app.run(host='0.0.0.0', debug=True)