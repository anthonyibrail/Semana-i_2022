import paho.mqtt.client as paho
import time
import psutil

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

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
           listOfProcObjects.append(pinfo);
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass
    # Sort list of dict by key vms i.e. memory usage
    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)
    return listOfProcObjects

client = paho.Client()
#client.username_pw_set("etorresr", "G4t0")
client.on_publish = on_publish
client.connect("broker.mqttdashboard.com", 1883)
client.loop_start()

while True:

    #Se obtiene el str de frecuencia y se hace split al string hasta conseguir el numero de la frecuencia
    f = psutil.cpu_freq()
    fr = str(f).split(",")
    frec = fr[0].split("=")
    (rc, mid) = client.publish("anthony/frec", str(frec[1]), qos=1)
    print("CPU frequency", psutil.cpu_freq())

    #Se obtiene el numero de cores del CPU
    nuc = psutil.cpu_count()
    (rc) = client.publish("anthony/nuc", str(nuc), qos=1)
    print("Number of cores in system", psutil.cpu_count())

    #Se obtiene el porcentaje de uso de CPU
    uso = psutil.cpu_percent(4)
    (rc) = client.publish("anthony/uso", str(uso), qos=1)
    print('The CPU usage is: ', psutil.cpu_percent(4))
    
    #Se obtiene el string de virtual memory y se hace split hasta obtener el numero de porcentaje de uso de memoria
    m = psutil.virtual_memory()
    me = str(m).split(",")
    mem = me[2].split("=")
    (rc) = client.publish("anthony/mem", str(mem[1]), qos=1)
    print("Porcentaje de memoria: ", psutil.virtual_memory())

    #Se obtiene el proceso activo que mas recursos ocupa y se hace split hasta conseguir el nombre del proceso 
    listOfRunningProcess = getListOfProcessSortedByMemory()
    p = listOfRunningProcess[0]
    pr = str(p).split(",")
    str_match1 = [s for s in pr if "'name'" in s]
    proc = str(str_match1).split("'")
    (rc) = client.publish("anthony/proc", str(proc[3]), qos=1)
    print("Proceso: ", listOfRunningProcess[0])

    time.sleep(30)