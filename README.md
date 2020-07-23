# ChitChatter
A complete command line chat app.

This is my first python project, a command line chat app using sockets.
From this you can chat with anyone, on the same network or on the different network.
There is no pre-req for this except python3.

USAGE:

    [A] STARTING THE SERVER

        [1] First start the chat server using the server.py file.
            python3 server.py

        [2] Then enter your computer's local ipv4 or public ipv4.

        [3] Then enter any port of your choice (8000+ preffered)

        [4] By doing this your server should start.

        [5] Server message can be sent just by typing the message on the server screen.


    [B] CONNECTING THE CLIENT

        [1] First run the client script by:
            python3 client.py

        [2] Then enter the ipv4 of the server. (Remember if you are using the local ipv4 both the computers should be on the same network)

        [3] Then enter the port on which you started the server.

        [4] Enter your name, and you are all set.

        [5] New message can be sent just by typing the message on the client screen.
  
  
FEATURES:

    [1] You can connect as many clients you want, by just changing the argument s.listen() in server.py, line 123. (Default is set to 20)

    [2] If you want to disconnect the client (from the client-end) just type bye on the client window.

    [3] Server can also send messages.

    [4] If any client is connected or disconnected, all the clients and the server gets the connection or disconnection message.

    [5] As soon as a new client is connected it will recieve a message of all the people already connected to the server.


    NOTE: If you just want to try this tool (on the same machine) use 127.0.0.1 as the ip and you can open server and client on the same machine.
