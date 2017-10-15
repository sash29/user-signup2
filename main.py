from flask import Flask,request,redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env=jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),autoescape=True)

app=Flask(__name__)
app.config['DEBUG']=True

def is_field_empty(form_field):
    if form_field == "":
        return True
    else:
        return False

def is_valid_email(emailStr):
    if '@' in emailStr or "." in emailStr :
        return True
    
    else:
        return False

@app.route("/")
def index():
    template=jinja_env.get_template('basic_form.html')
    return template.render()

@app.route("/validate_field", methods=["POST"])
def validate_field():
    UserName = request.form['UserName']
    password = request.form['password']
    cnfrmPswd = request.form['verify']
    email= request.form['email']

    userName_error=""
    password_error=""
    verification_error=""
    email_error=""

              
    if len(UserName) < 3 or len(UserName) > 20 :
        userName_error="3-20 characters required with no spaces "
        userName=""
       
    pswdLen= len(password)
    if pswdLen <3 or pswdLen >20 :
        password_error="3-20 characters required with no spaces"
        password=""
           
    if cnfrmPswd != password :
        verification_error = "Passwords dont match"

    if len(email) < 3 or len(email) > 20 :
        email_error="3-20 characters required with no spaces"
        email="" 

    if not is_valid_email(email) and email != "":
        email_error="Pls enter a valid email address"

    if not userName_error and not password_error and not verification_error and not email_error :
        UserName = request.form['UserName']
        email = request.form['email']
        template = jinja_env.get_template('successfulSignup.html')
        return template.render(UserName =UserName, email=email)

    else:
        
        template = jinja_env.get_template('basic_form.html')
        return template.render(userName_error = userName_error, password_error = password_error,
                verification_error = verification_error, email_error = email_error)

    
app.run()