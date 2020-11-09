import socket

s = socket.socket()

s.bind(('0.0.0.0', 8080)) #It will accept all the clients with IP Address in the range (0-255.0-255.0-255.0-255)

s.listen(1) #Listening to a client for data

while(1):
    client, addr = s.accept()
    
    while(1):
        content = client.recv(50)
        if(len(content) == 0):
            break
        else:
            print(content)
    print("Closing Connection")
    client.close()