import sys
import socket
import time

hostname = "172.18.64.2"
port = 4224
content = '+'


def netcat(hn, p, content):
    # content = "*"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hn, p))

    s.sendall(content.encode())
    time.sleep(.5)
    s.shutdown(socket.SHUT_WR)

    res = ""
    count = 1

    while True:
        count += 1
        data = s.recv(4096)
        if not data:
            break
        res += data.decode()
    if count == 3: 
        # print(res.split('\n')[34])
        # print((res.split('\n')[34]).split(' ')[-5])
        # print((res.split('\n')[34]).split(' ')[-3])
        # print((res.split('\n')[34]).split(' ')[-1])
        
        z = int((res.split('\n')[34]).split(' ')[-1])
        x = int((res.split('\n')[34]).split(' ')[-5])
        y = int((res.split('\n')[34]).split(' ')[-3])
        if x + y  == z:
            print('use +')
            content = '+'
            
        elif x - y == z:
            print('use -')
            content = '-'
            
        else:
            print('use *')
            content = '*'
            
    else:

       # print(res.split('\n')[34])
       # print((res.split('\n')[34]).split(' ')[-5])
       # print((res.split('\n')[34]).split(' ')[-3])
       # print((res.split('\n')[34]).split(' ')[-1])
        
        z = int((res.split('\n')[34]).split(' ')[-1])
        x = int((res.split('\n')[34]).split(' ')[-5])
        y = int((res.split('\n')[34]).split(' ')[-3])
        print(res)
        if x + y  == z:
            print('use +')
            content = '+'
            )
        elif x - y == z:
            print('use -')
            content = '-'
          
        else:
            print('use *')
            content = '*'
            
    

# content = '+'

netcat(hostname, port, content)
