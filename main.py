from flask import Flask , request, redirect, render_template
import cgi

app = Flask(__name__)

app.config ['DEBUG'] = True

@app.route("/signup", methods=['POST'])
def username():
    errors=[]
    user= request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email= request.form["email"]
    error1=''
    if len(user) <4 or user.isalpha()==False:
        error1 = 'Please enter a valid username' 
        errors.append(error1)
    error2=''
    if len(password) < 4:
        error2= "Please enter a valid password of atleast 3 characters."
        errors.append(error2)
    error3=''
    if verify != password:
        error3 = "Password does not match"
        errors.append(error3)
    error4=''
    if "@." not in email and " " in email:
        error4= "Please enter a valid email"
        errors.append(error4)
    elif len(email)>1 and len(email)<4:
        error4= "Please enter a valid email"
        errors.append(error4)
    if len(errors) > 0:
        return render_template("/login.html",error1=error1,error2=error2,error3=error3,
     error4=error4,user=user, email=email)
    return render_template("welcome.html", user=user)

@app.route("/", methods = ['GET'])    
def index():
    error_encoded = request.args.get("error")
    return render_template("login.html", error = error_encoded)

app.run()
