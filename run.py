from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    from_number = request.values.get('From', None)
    resp = twilio.twiml.Response()
    resp.message("Hey! You\'re about to become Dattch most popular, beautiful, funny new user. We can\'t wait to have you.")
    resp.message("Download iOS: http://taps.io/getdattchios Download Android: http://taps.io/getdattchandroid")
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)
