## Create a simple socket server that will listen on a specified port

# Listen on localhost.  127.0.0.1
# Port: 12345  -- this is the port to listen on


# import the socket library
import socket

HOST = '127.0.0.1'
PORT = 12345

print ('Python Server is starting ...')

# we open this socket that is defined by HOST and PORT
# we will use 'with' to ensure the socket closes

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    # accept a connection
    conn, addr = s.accept()
    with conn:
        print('Connected to: ', addr)
        data = conn.recv(1024)  # this is enough for a request

        print(data.decode())

        # send a generic reponse
        response = "HTTP/1.1 200 OK\n\n<html><body>Hello World</body></html>"
        conn.sendall(response.encode())