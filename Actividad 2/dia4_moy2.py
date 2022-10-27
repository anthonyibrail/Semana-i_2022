from random import randint
import time
import psutil
import pyrebase
config = {
"apiKey": "AIzaSyCJp3wOiDbR_zhVGDhq88HtoQ6bXp8NqQg",
"authDomain": "semana-i-esp32.firebaseapp.com",
"databaseURL": "https://semana-i-esp32-default-rtdb.firebaseio.com",
"projectId": "semana-i-esp32",
"storageBucket": "semana-i-esp32.appspot.com",
"messagingSenderId": "601338901220",
"appId": "1:601338901220:web:db9d0e28282465b3ff32f1"
}

#create authetication
firebase = pyrebase.initialize_app(config)
#accesing database in firebase
db = firebase.database()

#Funcion para ver cual es la que mas consume
def getListOfProcessSortedByMemory():
    '''
    Get list of running process sorted by Memory Usage
    '''
    listOfProcObjects = []
    # Iterate over the list
    for proc in psutil.process_iter():
       try:
           # Fetch process details as dict
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
           pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
           # Append dict to list
           listOfProcObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass
    # Sort list of dict by key vms i.e. memory usage
    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)
    return listOfProcObjects


#Creamos un while para que cada 30 seg publique la informacion en el formato correcto
while True:
    listOfRunningProcess = getListOfProcessSortedByMemory()

    frec  = str(psutil.cpu_freq())
    frecc  = frec[17:23]

    memo = str(psutil.virtual_memory())
    memo = memo.split(",")
    memo = memo[2].split("=")

    pro = str(listOfRunningProcess[0])
    pro = pro.split(":") 
    pro = pro[3].split("'") 

    print(frecc)
    print (memo[1])
    print(pro[1])

    
    
    data = {"frec": frecc, "nuc":psutil.cpu_count(), "uso": psutil.cpu_percent(4), "mem": memo[1], "prog":pro[1] }

    db.child("users").child("anthony").push(data)
    print("Data added to real time database ")
    
    time.sleep(120)


