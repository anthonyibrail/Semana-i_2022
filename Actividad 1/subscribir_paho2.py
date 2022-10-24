import paho.mqtt.client as paho

# Inicializacion de arreglos
frec_Count = [0,0,2000,0,0,0,0]
nuc_Count = [0,0,4,0,0,0,0]
uso_Count = [0,0,12,0,0,0,0]
mem_Count = [0,0,55,0,0,0,0]
proc_Count = ["","","zoom.exe","","","",""]

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

    """ USUARIOS """
    #dafne
    if(msg.topic == "dafne/frec"):
        data = str(msg.payload).split("'")
        print(float(data[1]))
        frec_Count[0] = float(data[1])
    
    if(msg.topic == "dafne/nuc"):
        data = str(msg.payload).split("'")
        print(int(data[1]))
        nuc_Count[0] = int(data[1])

    if(msg.topic == "dafne/uso"):
        data = str(msg.payload).split("'")
        print(float(data[1]))
        uso_Count[0] = float(data[1])

    if(msg.topic == "dafne/mem"):
        data = str(msg.payload).split("'")
        print(float(data[1]))
        mem_Count[0] = float(data[1])
    
    if(msg.topic == "dafne/proc"):
        data = str(msg.payload).split("'")
        print(str(data[1]))
        proc_Count[0] = str(data[1])
    
    #miles
    if(msg.topic == "miles/frec"):
        data = str(msg.payload).split("'")
        print(float(data[1]))
        frec_Count[1] = float(data[1])
    
    if(msg.topic == "miles/nuc"):
        data = str(msg.payload).split("'")
        print(int(data[1]))
        nuc_Count[1] = int(data[1])

    if(msg.topic == "miles/uso"):
        data = str(msg.payload).split("'")
        print(float(data[1]))
        uso_Count[1] = float(data[1])

    if(msg.topic == "miles/mem"):
        data = str(msg.payload).split("'")
        print(float(data[1]))
        mem_Count[1] = float(data[1])
    
    if(msg.topic == "miles/proc"):
        data = str(msg.payload).split("'")
        print(str(data[1]))
        proc_Count[1] = str(data[1])

    #dafne_badillo
    """ if(msg.topic == "dafne_badillo/frec"):
        data = str(msg.payload).split("'")
        print(float(data[1]))
        frec_Count[2] = float(data[1])
    
    if(msg.topic == "dafne_badillo/nuc"):
        data = str(msg.payload).split("'")
        print(int(data[1]))
        nuc_Count[2] = int(data[1])

    if(msg.topic == "dafne_badillo/uso"):
        data = str(msg.payload).split("'")
        print(float(data[1]))
        uso_Count[2] = float(data[1])

    if(msg.topic == "dafne_badillo/mem"):
        data = str(msg.payload).split("'")
        print(float(data[1]))
        mem_Count[2] = float(data[1])
    
    if(msg.topic == "dafne_badillo/proc"):
        data = str(msg.payload).split("'")
        print(str(data[1]))
        proc_Count[2] = str(data[1]) """

    #victor
    if(msg.topic == "victor/frec"):
        data = str(msg.payload).split("'")
        print(float(data[1]))
        frec_Count[3] = float(data[1])
    
    if(msg.topic == "victor/nuc"):
        data = str(msg.payload).split("'")
        print(int(data[1]))
        nuc_Count[3] = int(data[1])

    if(msg.topic == "victor/uso"):
        data = str(msg.payload).split("'")
        print(float(data[1]))
        uso_Count[3] = float(data[1])

    if(msg.topic == "victor/mem"):
        data = str(msg.payload).split("'")
        print(float(data[1]))
        mem_Count[3] = float(data[1])
    
    if(msg.topic == "victor/proc"):
        data = str(msg.payload).split("'")
        print(str(data[1]))
        proc_Count[3] = str(data[1])
    
    #joseduardo
    if(msg.topic == "joseduardo/frec"):
        data = str(msg.payload).split("'")
        print(float(data[1]))
        frec_Count[4] = float(data[1])
    
    if(msg.topic == "joseduardo/nuc"):
        data = str(msg.payload).split("'")
        print(int(data[1]))
        nuc_Count[4] = int(data[1])

    if(msg.topic == "joseduardo/uso"):
        data = str(msg.payload).split("'")
        print(float(data[1]))
        uso_Count[4] = float(data[1])

    if(msg.topic == "joseduardo/mem"):
        data = str(msg.payload).split("'")
        print(float(data[1]))
        mem_Count[4] = float(data[1])
    
    if(msg.topic == "joseduardo/proc"):
        data = str(msg.payload).split("'")
        print(str(data[1]))
        proc_Count[4] = str(data[1])

    #alonso
    if(msg.topic == "alonso/frec"):
        data = str(msg.payload).split("'")
        print(float(data[1]))
        frec_Count[5] = float(data[1])
    
    if(msg.topic == "alonso/nuc"):
        data = str(msg.payload).split("'")
        print(int(data[1]))
        nuc_Count[5] = int(data[1])

    if(msg.topic == "alonso/uso"):
        data = str(msg.payload).split("'")
        print(float(data[1]))
        uso_Count[5] = float(data[1])

    if(msg.topic == "alonso/mem"):
        data = str(msg.payload).split("'")
        print(float(data[1]))
        mem_Count[5] = float(data[1])
    
    if(msg.topic == "alonso/proc"):
        data = str(msg.payload).split("'")
        print(str(data[1]))
        proc_Count[5] = str(data[1])

    #anthony
    if(msg.topic == "anthony/frec"):
        data = str(msg.payload).split("'")
        print(float(data[1]))
        frec_Count[6] = float(data[1])
    
    if(msg.topic == "anthony/nuc"):
        data = str(msg.payload).split("'")
        print(int(data[1]))
        nuc_Count[6] = int(data[1])

    if(msg.topic == "anthony/uso"):
        data = str(msg.payload).split("'")
        print(float(data[1]))
        uso_Count[6] = float(data[1])

    if(msg.topic == "anthony/mem"):
        data = str(msg.payload).split("'")
        print(float(data[1]))
        mem_Count[6] = float(data[1])
    
    if(msg.topic == "anthony/proc"):
        data = str(msg.payload).split("'")
        print(str(data[1]))
        proc_Count[6] = str(data[1])

    print("Arreglo de frecuencias:  ", frec_Count)
    print("Arreglo de cores:    ", nuc_Count)
    print("Arreglo de porcentaje de uso:    ", uso_Count)
    print("Arreglo de porcentaje de memoria:    ", mem_Count)
    print("Arreglo de procesos:    ", proc_Count)
    print("\n--------------------")
    print("La frecuencia max es: ", max(frec_Count))
    print("Mi frecuencia es: ", frec_Count[6])
    print("La frecuencia min es: ", min(frec_Count))
    print("\n--------------------")
    print("El número de cores max es: ", max(nuc_Count))
    print("Mi número de cores es: ", nuc_Count[6])
    print("El número de cores min es: ", min(nuc_Count))
    print("\n--------------------")
    print("El porcentaje de uso de CPU max es: ", max(uso_Count))
    print("Mi porcentaje de uso de CPU es: ", uso_Count[6])
    print("El porcentaje de uso de CPU min es: ", min(uso_Count))
    print("\n--------------------")
    print("El porcentaje de memoria usado max es: ", max(mem_Count))
    print("Mi porcentaje de memoria usado es: ", mem_Count[6])
    print("El porcentaje de memoria usado min es: ", min(mem_Count))
    print("\n--------------------")
    print("Lista de procesos: ")
    for item in proc_Count:
        print(item)

client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
#client.username_pw_set("etorresr", "G4t0")
client.connect("broker.mqttdashboard.com", 1883)

""" USUARIOS """

#dafne
client.subscribe("dafne/frec", qos=1)
client.subscribe("dafne/nuc", qos=1)
client.subscribe("dafne/uso", qos=1)
client.subscribe("dafne/mem", qos=1)
client.subscribe("dafne/proc", qos=1)

#miles
client.subscribe("miles/frec", qos=1)
client.subscribe("miles/nuc", qos=1)
client.subscribe("miles/uso", qos=1)
client.subscribe("miles/mem", qos=1)
client.subscribe("miles/proc", qos=1)

#dafne_badillo
# client.subscribe("dafne_badillo/frec", qos=1)
# client.subscribe("dafne_badillo/nuc", qos=1)
# client.subscribe("dafne_badillo/uso", qos=1)
# client.subscribe("dafne_badillo/mem", qos=1)
# client.subscribe("dafne_badillo/proc", qos=1)

#victor
client.subscribe("victor/frec", qos=1)
client.subscribe("victor/nuc", qos=1)
client.subscribe("victor/uso", qos=1)
client.subscribe("victor/mem", qos=1)
client.subscribe("victor/proc", qos=1)

#joseduardo
client.subscribe("joseduardo/frec", qos=1)
client.subscribe("joseduardo/nuc", qos=1)
client.subscribe("joseduardo/uso", qos=1)
client.subscribe("joseduardo/mem", qos=1)
client.subscribe("joseduardo/proc", qos=1)

#alonso
client.subscribe("alonso/frec", qos=1)
client.subscribe("alonso/nuc", qos=1)
client.subscribe("alonso/uso", qos=1)
client.subscribe("alonso/mem", qos=1)
client.subscribe("alonso/proc", qos=1)

#anthony
client.subscribe("anthony/frec", qos=1)
client.subscribe("anthony/nuc", qos=1)
client.subscribe("anthony/uso", qos=1)
client.subscribe("anthony/mem", qos=1)
client.subscribe("anthony/proc", qos=1)

client.loop_forever()