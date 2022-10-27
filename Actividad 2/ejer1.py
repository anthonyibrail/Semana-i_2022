import pyrebase

config = {
  "apiKey" : "AIzaSyD57f8TRtQUYN76L04l-e7QYyVSmROWiNI",
  "authDomain" : "esp32-anthony.firebaseapp.com",
  "databaseURL" : "https://esp32-anthony-default-rtdb.firebaseio.com",
  "projectId" : "esp32-anthony",
  "storageBucket" : "esp32-anthony.appspot.com",
  "messagingSenderId" : "1031989251866",
  "appId" : "1:1031989251866:web:80ebc1ffeeefb86f1ba6a3"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
email = input("Please Enter Your Email : ")
password = input("Please Enter Your Password : ")
user = auth.create_user_with_email_and_password(email, password)
print("User Created Successfully")
try:
    signin = auth.sign_in_with_email_and_password(email, password)
    print("Sign In Was Successfull")
except:
    print("Invalid user or password")
auth.send_email_verification(signin['idToken'])
print("Email Verification Has Been Sent")
auth.send_password_reset_email(email)
print("We have sent an email, check your inbox ")