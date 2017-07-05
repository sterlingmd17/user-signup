from flask import Flask , request, redirect, render_template
import cgi

app = Flask(__name__)

app.config ['DEBUG'] = True


#password= request.form["password"]
#password2= request.form["verify"]
#email = request.form["email"]
@app.route("/signup", methods=['POST'])
def username():
    errors=[]
    user= request.form["username"]
    error1=''
    if len(user) <4 or user.isalpha()==False:
        error1 = 'Please enter a valid username' 
        errors.append(error1)
        #return render_template("/login.html", error1=error1)


#@app.route("/signup", methods=['POST'])
#def password():
    password = request.form["password"]
    verify = request.form["verify"]
    error2=''
    if len(password) < 4:
        error2= "Please enter a valid password of atleast 3 characters."
        errors.append(error2)
        #return render_template("/login.html", error2 = error2)
    error3=''
    if verify != password:
        error3 = "Password does not match"
        errors.append(error3)
        #return render_template("/login.html", error3 = error3)
    email= request.form["email"]
    error4=''
    x=" "
    if "@." not in email and " " in email:
        error4= "Please enter a valid email"
        errors.append(error4)
    elif len(email)>1 and len(email)<4:
        error4= "Please enter a valid email"
        errors.append(error4)
    if len(errors) > 0:
        return render_template("/login.html",error1=error1,error2=error2,error3=error3, error4=error4,user=user, email=email)
    return render_template("welcome.html", user=user)

    

    
    
    
    



@app.route("/", methods = ['GET'])    
def index():
    error_encoded = request.args.get("error")
    return render_template("login.html", error = error_encoded)

app.run()
