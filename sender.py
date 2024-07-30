import socket   #to establish connection
from datetime import datetime as dt

# socket.AF_INET --> Through the internet
# socket.SOCK_DGRAM --> protocol (UDP/TCP)

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   #socket() is a class
#target_ip = "192.168.1.65" 
target_ip='127.0.0.1'   
target_port=2004
target_address=(target_ip,target_port)
condition=True
while condition:
    message = input("Msg: ")
    message_encrypted = message.encode('ascii')
    s.sendto(message_encrypted,target_address)
    print("Message sent...")
    time = dt.now().strftime("%d/%m/%Y,   %H:%M:%S")

    #Receiving data 
    data=s.recvfrom(100)
    message_decrypted=data[0].decode('ascii')
    ip_address=data[1][0]
    print(message_decrypted)
    
    #opening a file
    with open("messages/"+str(ip_address)+'.txt','a') as fp:
        #returns string[ type(time)->'str' ]
        fp.write(f"{message}    {time}\n")

    if message.upper() == "BYE":
        condition = False 