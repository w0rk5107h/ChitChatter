import socket
import sys
import threading
import time
import select
from os import system, name 

def clear():  
    if name == 'nt':                 
        _ = system('cls') 
    else:                           
        _ = system('clear') 

def connect_server():
    try:
        s.connect((host,port))
    except:
        print("Server not up...")
        exit()
    message = s.recv(1024)
    message = message.decode()
    clear()
    print(message)
    name = input(str("Enter your name - "))
    name = name.encode()
    s.send(name)

def recv_message():
    while True:
        try:
            in_message = s.recv(1024)
            if in_message:
                in_message = in_message.decode()
                print(in_message)
            else:
                pass
        except:
            pass
        in_message = 0

def send_message():
    dis_message = """
   ___  _________________  _  ___  ______________________  _______          
  / _ \/  _/ __/ ___/ __ \/ |/ / |/ / __/ ___/_  __/  _/ |/ / ___/          
 / // // /_\ \/ /__/ /_/ /    /    / _// /__  / / _/ //    / (_ / _   _   _ 
/____/___/___/\___/\____/_/|_/_/|_/___/\___/ /_/ /___/_/|_/\___/ (_) (_) (_)
                                                                            
                  """
    while True:
        out_message = input(str())
        if out_message.lower() == 'bye':
            clear()
            print(dis_message)
            s.close()
            sys.exit()
        out_message = out_message.encode()
        s.send(out_message)

if __name__ == "__main__":

    clear()

    message = """ 
  _______   _ __  _______        __  __         
 / ___/ /  (_) /_/ ___/ /  ___ _/ /_/ /____ ____
/ /__/ _ \/ / __/ /__/ _ \/ _ `/ __/ __/ -_) __/
\___/_//_/_/\__/\___/_//_/\_,_/\__/\__/\__/_/   
                                                
                    by - agpriyansh
                                              
"""
    print(message)

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    host = input(str("[+] Enter the host to which you want to connect to  - "))
    port = int(input("[+] Enter the port through which you want to connect - "))
    
    connect_server()

    send = threading.Thread(target=send_message)
    recv = threading.Thread(target=recv_message,daemon=True)

    send.start()
    recv.start()

    send.join()

    print("Connection CLOSED!!!!")
    input()
