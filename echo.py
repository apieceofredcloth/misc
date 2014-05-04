import socket
import signal
import sys


listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((
    '0.0.0.0', 8080))  # remember, 80 is the port for HTTP traffic
listen_socket.listen(1)


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    #listen_socket.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
    connection, address = listen_socket.accept()
    # connection.recv(1024)
    connection.sendall("""HTTP/1.1 200 OK
    Content-type: text/html


    <html>
        <body>
            <h1>Hello, World!</h1>
        </body>
    </html>""")
    connection.close()
