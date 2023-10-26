#! myenv/bin/ python3
import socket
import argparse
import threading

parser = argparse.ArgumentParser(description="Chat Client")
parser.add_argument("-p", type=int, required=True, help="Port of the service on the server")
parser.add_argument("-ip",type=str,required=True,help="The ip of the sever")
args = parser.parse_args()

username = input("Enter a username to display:")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((args.ip,args.p))
print("Connection established")

def receiveMessages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            print("Connection closed")
            break
        
def sendMessages():
    while True:
        message = input()
        if message == "\disconnect":
            message = username+" disconnected."
            client_socket.send(message.encode())
            client_socket.close()
            break
        message = username + ": "+message
        client_socket.send(message.encode())
        


sendThread = threading.Thread(target=sendMessages)
receiveThread = threading.Thread(target=receiveMessages)

sendThread.start()
receiveThread.start()
