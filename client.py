import socket
import keyboard

RASPBERRY_PI_IP = '192.168.20.105'  # Change to your Raspberry Pi's IP address
PORT = 12345  # The port number used by the server on the Raspberry Pi

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((RASPBERRY_PI_IP, PORT))
    print("Connected to Raspberry Pi. Use WASD keys to control the car, press ESC to quit.")

    try:
        while True:
            if keyboard.is_pressed('w'):
                s.sendall(b'forward\n')
            elif keyboard.is_pressed('s'):
                s.sendall(b'backward\n')
            elif keyboard.is_pressed('a'):
                s.sendall(b'left\n')
            elif keyboard.is_pressed('d'):
                s.sendall(b'right\n')
            elif keyboard.is_pressed('esc'):
                print("Exiting...")
                break
    except KeyboardInterrupt:
        print("Program terminated.")
