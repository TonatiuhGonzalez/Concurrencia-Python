from ast import arg
import threading

def trabajador():
    print("Trabajador")

hilos = []
for i in range(5):
    h = threading.Thread(target=trabajador)
    hilos.append(h)
    h.start()

def trabajador2(num):
    print("Trabajador: %s" %num)

hilos2 = []
for i in range(5):
    h2 = threading.Thread(target=trabajador2, args=(i,))
    hilos2.append(h2)
    h2.start() 