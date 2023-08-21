import socket
import os

# Specify the UDP port number
UDP_PORT = 50000
BUFFER_SIZE = 1  # Receive 1 byte of data

# Create a socket and bind
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("192.168.3.5", UDP_PORT))

while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    print(f"Received message: {data} from {addr}")

    if data==b"\x41":
        print("Camera activate")
        sock.sendto(b'0', addr)
        sock.sendto(b'a', addr)  # Return byte data 'a' to the PC
        
        response, _ = sock.recvfrom(1)  # Wait for a reply from the PC
        if response == b'j':
            os.system("libcamera-jpeg -o test.jpg")
            # Planning to change to the Python program
            sock.sendto(b'j', addr)  # Return byte data 'j' to the PC
        if response == b'r':
            os.system("libcamera-raw -t 2000 -o test.raw")
            # Planning to change to the Python program
            sock.sendto(b'r', addr)  # Return byte data 'r' to the PC
        if response == b'n':
            #os.system("libcamera-raw -t 2000 -o test.jpg")
            sock.sendto(b'n', addr)  # Return byte data 'n' to the PC
    elif data==b"\x42":
        print("HK data are ...")
        response="HK data abcdef...".encode('utf-8')
        sock.sendto(response, addr)
    elif data==b"\x43":
        print("reboot")
        response="now rebooting".encode('utf-8')
        sock.sendto(response, addr)
        #os.system("python ./../Camera-test/Experiment/capture.py")
    else:
        response="Received an irregular signal".encode('utf-8')
        sock.sendto(response, addr)
