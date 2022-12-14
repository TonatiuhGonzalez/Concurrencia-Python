from socket import socket, error
from threading import Thread
class Client(Thread):
    def __init__(self, conn, addr):
        # Inicializar clase padre.
        Thread.__init__(self)        
        self.conn = conn
        self.addr = addr    
    def run(self):
        while True:
            try:
                # Recibimos el mensaje, con el metodo recv recibimos datos. Por parametro la cantidad de bytes para recibir
                input_data = self.conn.recv(1024)
            except error:
                print("[%s] Error de lectura." % self.name)
                break
            else:
                # #Si se reciben datos nos muestra el mensaje recibido
                if input_data:
                    self.conn.send(input_data)
                    print (input_data.decode())
def main():
    s = socket()    
    #Puerto y servidor que debe escuchar
    s.bind(("localhost", 6030))
    s.listen(0)    
    while True:
        conn, addr = s.accept()
        c = Client(conn, addr)
        c.start()
        print("%s:%d se ha conectado." % addr)
if __name__ == "__main__":
    main()