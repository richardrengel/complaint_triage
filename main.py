from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World, from me R!</p>"


# def main():
#     print("hello")

if __name__=="__main__":
    app.run()