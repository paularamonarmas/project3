from flask import Flask, render_template, request
app = Flask(__name__)
#app = Flask("MyApp")
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/tda", methods=["POST"])
def tda():
    form_data = request.form
    #tda = form_data["tda"]
    #print (tda)
    return render_template("tda.html")

@app.route("/signup", methods=["POST"])
def signup():
    form_data = request.form
    return render_template("signup.html")
    #send_message(form_data["email"])


#def send_message(email):
	#print(email)
	#return requests.post("https://api.mailgun.net/v3/sandboxbec895c8e12a4174a2462f053a6bad7c.mailgun.org/messages",
        #auth=("api", "41f4e00ee0156073d275f5162b7ea638-e566273b-8f7e8104"),
        #data={"from": "The Day After <mailgun@sandboxbec895c8e12a4174a2462f053a6bad7c.mailgun.org>",
             ## "to": [email],
             # "subject": "Hello",
             # "text": "Thank you for subscribing!"})
