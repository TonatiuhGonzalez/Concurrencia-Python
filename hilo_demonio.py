import threading
import time
import logging
'''
def demonio():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')

def no_demonio():
    logging.debug('Starting')
    logging.debug('Exiting')

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

d = threading.Thread(name='daemon', target=demonio, daemon=True)
h = threading.Thread(name='non-daemon', target=no_demonio)

d.start()
h.start()

def demonio2():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')


def no_demonio2():
    logging.debug('Starting')
    logging.debug('Exiting')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

d2 = threading.Thread(name='daemon', target=demonio2, daemon=True)
h2 = threading.Thread(name='non-daemon', target=no_demonio2)
d2.start()
h2.start()

d2.join()
h2.join()'''


def demonio():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')


def no_demonio():
    logging.debug('Starting')
    logging.debug('Exiting')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

d = threading.Thread(name='daemon', target=demonio, daemon=True)
h = threading.Thread(name='non-daemon', target=no_demonio)
d.start()
h.start()

d.join(0.1)
print('d.isAlive()', d.is_alive())
h.join() 