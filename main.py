from flask import Flask

app = Flask(__name__)

def generate_html(message):
    version_number = '0001'
    html = """
        <html>
        <body>
            <div style='text-align:center;font-size:80px;'>
                <image height="1200" width="400" src="https://raw.githubusercontent.com/richardrengel/complaint_triage/main/images/IMG-8086.jpg">
                <br> {0}
                <p>Version Number: {1}</p>
                <br>
            </div>
        </body>
        </html>""".format(message,version_number)
    return html

def greet():
    greeting = 'Welcome to CI/CD, from Mushroom'
    return greeting




@app.route("/")
def hello_world():
    html = generate_html(greet())
    return html
    # return "<p>Hello, World, from me R!</p>"


# def main():
#     print("hello")

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)