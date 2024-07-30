import socket   #to establish connection
from datetime import datetime as dt

#socket.AF_INET --> Through the internet
#socket.SOCK_DGRAM --> protocol (UDP/TCP)

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
#socket() is a class and s is an object of socket class
#s is like an end point (it is like a gate)

#ip_address="192.168.1.4"
ip_address='127.0.0.1'

#port number 0-65353 (but 0-1023 are reserved)
port_no=2004
complete_address=(ip_address,port_no)
s.bind(complete_address)    #name registration
#sender and receiver are now capable of sharing and receiving information
#bind() is like a name plate of that gate
print("Hey I am listening!!")
condition=True
while condition:
    #Receiving data 
    data=s.recvfrom(100)     
    message=data[0]
    message_decrypt=message.decode('ascii')
    ip=data[1][0]
    target_address=data[1]      #(ip_address and port)
    print(message_decrypt)

    #sending data back or replying
    msg=input("Reply:")
    msg_encrypt=msg.encode('ascii')
    s.sendto(msg_encrypt,target_address)
    time=dt.now().strftime("%d/%m/%Y,   %H:%M:%S")

    with open("messages/"+str(ip)+".txt",'a') as fp:
        fp.write(f"{msg}    {time}\n")

    if msg.upper()=='BYE':
        condition=False


