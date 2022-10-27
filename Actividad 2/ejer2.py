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
#create authetication
firebase = pyrebase.initialize_app(config)
#accesing database in firebase
db = firebase.database()
data = {"name":"Ignacio Altamirano"}
data1 = {"job":"Periodista"}
db.child("users").push(data)
db.child("users").push(data1)
print("Data added to real time database ")