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
db = firebase.database()
#create your onKey, for label elements
#update elements
db.child("users").child("Gatitos").update({"name":"Juan Camanaey"})
print("Data updated successfully ")
db.child("users").child("-NFG7SzW_7kQtt7dmoFT").update({"name":"Fulano Detal"})#-LzqIcMVMPaQKVLLjK5d is an onKey print("Data updated successfully ")
#accesing database in firebase
db = firebase.database()
#reading some atributes of the onKey elements
all_users = db.child("users").get()
for users in all_users.each():
    print(users.val())
    print(users.key())