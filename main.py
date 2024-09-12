from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    
    # Construct the mailto link
    mailto_link = f"mailto:sohitmahato0803@gmail.com?subject={subject}&body=Name: {name}%0AEmail: {email}%0AMessage: {message}"
    
    # Redirect to the mailto link
    return redirect(mailto_link)

    return redirect(url_for('home'))



if(__name__ == '__main__'):
    app.run(debug=True)