from flask import Flask, request, abort

application = Flask(__name__)

@application.route('/hello')
def hello():
    user_agent = request.headers.get('User-Agent')
    if user_agent == "bad guy":
        abort(403)
    return "hello prozorro"

if __name__ == "__main__":
    application.run()
