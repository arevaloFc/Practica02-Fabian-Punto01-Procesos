import os
from time import sleep

def padre():

    cantidadProcesos = int(input("Cuantos procesos quieres: "))

    for x in range(cantidadProcesos):
        
        pid = os.fork()

        if(pid != 0):
            print("Proceso padre -- ID:",os.getpid(),"proceso hijo",pid)
        else:
            hijo()

def hijo():

    print("Proceso hijo -- ID:",os.getpid())
    sleep(5)
    print("Proceso hijo con ID:",os.getpid(),"se ha terminado")
    os._exit(1)

if __name__ == "__main__":
    padre()