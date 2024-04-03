import socket
from mDev import mDEV  # Make sure this class is accessible; might need to adjust import path

# Initialize the mDEV class
mdev = mDEV()

# Network setup
HOST = '192.168.05.20'  # Symbolic name meaning all available interfaces
PORT = 12345  # Arbitrary non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("Waiting for a connection...")
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            command = data.decode('utf-8').strip()
            if command == 'forward':
                mdev.move(1000, 1000)  # Adjust values based on your setup
            elif command == 'backward':
                mdev.move(-1000, -1000)
            elif command == 'left':
                mdev.move(-500, 500)
            elif command == 'right':
                mdev.move(500, -500)
