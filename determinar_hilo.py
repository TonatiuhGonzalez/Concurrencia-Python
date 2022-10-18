import threading
import time
import logging

def trabajador():
    print(threading.current_thread(),'Startign')
    time.sleep(0.2)
    print(threading.current_thread(),'Exiting')

def mi_servicio():
    print(threading.current_thread(),'Startign')
    time.sleep(0.3)
    print(threading.current_thread(),'Exiting')

s = threading.Thread(name='Juanita', target=mi_servicio)
h = threading.Thread(name='Panchito', target=trabajador)
h2 = threading.Thread(target=trabajador)

h.start()
h2.start()
s.start()


def trabajador2():
    logging.debug("Starting")
    time.sleep(0.2)
    logging.debug("Exiting")


def mi_servicio2():
    logging.debug("Starting")
    time.sleep(0.3)
    logging.debug("Exiting")


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)

ss = threading.Thread(name='Juanita', target=mi_servicio2)
hh = threading.Thread(name='Pedrito', target=trabajador2)
hh2 = threading.Thread(target=trabajador2)

hh.start()
hh2.start()
ss.start()