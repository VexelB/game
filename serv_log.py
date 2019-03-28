import socket

sock_reg = socket.socket()
sock_reg.bind(('', 9191))
sock_reg.listen(1)
users = {}
userstxt = open("users.txt", "r")
for line in userstxt:
    dataset = line.split(':')
    users.update({dataset[0]: [dataset[1], dataset[2], dataset[3]]})
userstxt.close()
while True:
    try:
        conn, addr = sock_reg.accept()
        data = conn.recv(512).decode()
        data += '\n'
        dataset = data.split(':')
        if dataset[0] == 'reg':
            if users.get(dataset[1]) == None:
                users.update({dataset[1]: [dataset[2], dataset[3], dataset[4]]})
                userstxt = open("users.txt", "w")
                for a in users.keys():
                    b = users.get(a)
                    userstxt.write(f"{a}:{b[0]}:{b[1]}:{b[2]}")
                userstxt.close()
                conn.send('sucksess/'.encode())
            else:
                conn.send('fuckyou/'.encode())
        if dataset[0] == 'log':
            if (users.get(dataset[1]) != None):
                b = users.get(dataset[1])
                if b[0] == dataset[2]:
                    conn.send('sucksess/'.encode())
                else:
                    conn.send('fuckyou/'.encode())
        conn.close()
    except Exception as e:
        print(e)
