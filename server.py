import socket
import sys
import _thread 
import threading
from os import system, name 

def clear():  
    if name == 'nt':            
        _ = system('cls') 
    else:                       
        _ = system('clear') 

def connet_client(conn, addr):
    global client_list
    conn_message = """
  _______   _________  ________  _________  _  ___  ________________________ 
 / ___/ /  /  _/ __/ |/ /_  __/ / ___/ __ \/ |/ / |/ / __/ ___/_  __/ __/ _ \\
/ /__/ /___/ // _//    / / /   / /__/ /_/ /    /    / _// /__  / / / _// // /
\___/____/___/___/_/|_/ /_/    \___/\____/_/|_/_/|_/___/\___/ /_/ /___/____/ 
                                                                                       
                   """
    conn_message = conn_message.encode()
    conn.send(conn_message)
    name = conn.recv(1024)
    name = name.decode()
    connected = name + ' (' + addr[0] + ') is connected'
    print(connected)
    connected = connected.encode()
    for send_to in client_list:
        send_to.send(connected)
    check_client = bool(client_list)
    if check_client == True:
        conn_people = "People who are already connected to the server : "
        conn_people = conn_people.encode()
        conn.send(conn_people)
        for conn_names in client_list.keys():
            conn_name = client_list[conn_names] + " "
            conn_name = conn_name.encode()
            conn.send(conn_name)
    else:
        no_people = "No one is connected to the server."
        no_people = no_people.encode()
        conn.send(no_people)
    temp_list = {conn:name}
    client_list.update(temp_list)

def recv_send_message(conn, addr):
    while True:
        global client_list
        try:
            message = conn.recv(1024)
            if message:
                message = message.decode()
                message = client_list[conn] + " - " + message
                print(message)
                message = message.encode()
                for send_to in client_list.keys():
                    if send_to == conn:
                        pass
                    else:
                        send_to.send(message)
            else:
                temp_name = client_list[conn]
                temp_addr = addr[0]
                temp_conn = conn
                del client_list[conn]
                disconnected = temp_name + ' (' + temp_addr + ') is disconnected'
                print(disconnected)
                disconnected = disconnected.encode()
                temp_conn.close()
                for send_to in client_list.keys():
                    send_to.send(disconnected)
                break
        except:
            pass

def server_message():
    global client_list
    while True:
        server_message = input()
        server_message = "Server - " + server_message
        server_message = server_message.encode()
        for send_to in client_list.keys():
            send_to.send(server_message)

if __name__ == "__main__":
   
    clear()

    message = """ 
  _______   _ __  _______        __  __         
 / ___/ /  (_) /_/ ___/ /  ___ _/ /_/ /____ ____
/ /__/ _ \/ / __/ /__/ _ \/ _ `/ __/ __/ -_) __/
\___/_//_/_/\__/\___/_//_/\_,_/\__/\__/\__/_/   
                                                
                    by - de4dgh0st
                                              
"""
    print(message)
    
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    host = input(str("[+] Enter the host for the server - "))
    port = int(input("[+] Enter the port for the server - "))

    conn = 0
    addr = 0

    s.bind((host,port))

    clear()

    ser_message = """
   ___________ _   _________    _____________   ___  _____________ 
  / __/ __/ _ \ | / / __/ _ \  / __/_  __/ _ | / _ \/_  __/ __/ _ \\
 _\ \/ _// , _/ |/ / _// , _/ _\ \  / / / __ |/ , _/ / / / _// // /
/___/___/_/|_||___/___/_/|_| /___/ /_/ /_/ |_/_/|_| /_/ /___/____/ 
                                                                    
                  """
    print(ser_message)
    print("\nListening for connections....")

    s.listen(20)

    client_list = {}

    server = threading.Thread(target=server_message)
    server.start()

    while True:
        conn , addr = s.accept()
        if conn and addr:
            connet_client(conn, addr)
            _thread.start_new_thread(recv_send_message,(conn, addr))
            conn=0
            addr=0
        else:
            pass
