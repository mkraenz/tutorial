import socket 
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind(("", 60000)) 
server.listen(1)

clients = []

try: 
    while True: 
        lesen, schreiben, oob = select.select([server] + clients, 
                                              [], [])

        for sock in lesen: 
            if sock is server: 
                client, addr = server.accept() 
                clients.append(client) 
                print("+++ Client %s verbunden" % addr[0])
            else: 
                nachricht = sock.recv(1024) 
                ip = sock.getpeername()[0] 
                if nachricht: 
                    print("[%s] %s" % (ip, nachricht))
                else: 
                    print("+++ Verbindung zu %s beendet" % ip)
                    sock.close() 
                    clients.remove(sock) 
finally: 
    for c in clients: 
        c.close() 
    server.close()