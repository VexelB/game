import socket


def parser(data1, conn, nconn):
    nconn.send(data1.encode())

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(2)
conn1, addr1 = sock.accept()
#conn1.send('1'.encode())
conn2, addr2 = sock.accept()
#conn2.send('2'.encode())
while True:
    parser(conn1.recv(512).decode(), conn1, conn2)
    parser(conn2.recv(512).decode(), conn2, conn1)
