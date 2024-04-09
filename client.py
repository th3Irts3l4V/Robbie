import socket
import keyboard
import time

RASPBERRY_PI_IP = '192.168.254.105'  # Change to your Raspberry Pi's IP address
PORT = 12345  # The port number used by the server on the Raspberry Pi

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((RASPBERRY_PI_IP, PORT))
    print("Connected to Raspberry Pi. Use WASD keys to control the car, press ESC to quit.")

    last_command_time = 0
    command_interval = 0.1  # Adjust this value to control the command sending interval

    try:
        while True:
            current_time = time.time()
            if current_time - last_command_time >= command_interval:
                if keyboard.is_pressed('w'):
                    s.sendall(b'forward\n')
                elif keyboard.is_pressed('s'):
                    s.sendall(b'backward\n')
                elif keyboard.is_pressed('a'):
                    s.sendall(b'left\n')
                elif keyboard.is_pressed('d'):
                    s.sendall(b'right\n')
                else:
                    s.sendall(b'stop\n')
                last_command_time = current_time

            if keyboard.is_pressed('esc'):
                print("Exiting...")
                break

            time.sleep(0.01)  # Add a small delay to reduce CPU usage

    except KeyboardInterrupt:
        print("Program terminated.")
