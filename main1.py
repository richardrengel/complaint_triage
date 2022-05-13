# from flask import Flask,render_template,request,url_for
#
# app = Flask(__name__)
# #add comment
#
# def generate_html(message):
#     version_number = '007'
#     html = """
#         <html>
#         <body>
#             <div style='text-align:center;font-size:80px;'>
#                 <br> {0}
#                 <p>Version Number: {1}</p>
#                 <br>
#                 <image height="800" width="500" src="https://raw.githubusercontent.com/richardrengel/complaint_triage/main/images/IMG-8086.jpg">
#
#             </div>
#         </body>
#         </html>""".format(message,version_number)
#     return html
#
# def greet():
#     greeting = 'Hi, from Mushroom'
#     return greeting
#
#
#
#
# # @app.route("/")
# # def hello_world():
# #     html = generate_html(greet())
# #     return html
# @app.route("/")
# def index():
# 	return render_template("index.html")
#     # return "<p>Hello, World, from me R!</p>"
#
#
# # def main():
# #     print("hello")
#
# if __name__=="__main__":
#     app.run(host='0.0.0.0', port=5000)
#     # app.run(host="127.0.0.1", port=8080, debug=True)