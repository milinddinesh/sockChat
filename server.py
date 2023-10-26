#! /myenv/bin/ python3
import socket
import threading
import argparse

parser = argparse.ArgumentParser(description="Chat Server")
parser.add_argument("-p", type=int, required=True, help="Port to bind the server to")
args = parser.parse_args()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', args.p))
server.listen()
print("Listening on port : "+str(args.p))

def broadcast(message, clientSocket):
    for client in clients:
        if client != clientSocket:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handleClient(client):
    while True:
        try:        
            message = client.recv(1024)
            if message == "":
                break
            broadcast(message,client)
        except:
            clients.remove(client)
            break

clients = []
while True:
    client, addr = server.accept()
    clients.append(client)
    print("Client connected") #add code to display which user 
    messageThread = threading.Thread(target=handleClient, args=(client,))
    messageThread.start()


    
 

