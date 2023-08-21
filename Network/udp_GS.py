import socket
import threading
import time

fmt_line = "----"

# Specify IP address and UDP port number for Raspberry Pi Zero
TARGET_IP = input("Target IP is: ")  # "192.168.3.5"
UDP_PORT = 50000


# Function with receiving capability
def receive_messages(sock):
    while True:
        data, addr = sock.recvfrom(1024)  # can receive up to 1024 bytes
        # print(f"----\nReceived response: {data.decode('utf-8')} \nfrom {addr}\n----")
        # print(f"{fmt_line}Response from: {addr} {fmt_line}")
        if data == b"0":
            pass
        if data == b"1":
            print("HK data are ABCDEF")
        if data == b"2":
            print("now rebooting")
        if data == b"3":
            print("Received an irregular signal")

        if data == b"A":
            while True:
                while True:
                    print("Camera Activated")
                    choice = input(
                        "Do you want to take a photo? (JPG: j, RAW: r, no: n): "
                    )

                    if choice in ["j", "r", "n"]:
                        sock.sendto(choice.encode("utf-8"), (TARGET_IP, UDP_PORT))
                        break
                print("Waiting for response")

                response, _ = sock.recvfrom(1)
                if response == b"j":
                    print("\n A jpeg image was taken")
                    break
                if response == b"r":
                    print("\n A raw image was taken")
                    break
                if response == b"n":
                    print("\n Photo capture was cancelled")


# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", UDP_PORT))  # allow reception from any address

# Start receiving functionality in a separate thread
rxthread = threading.Thread(target=receive_messages, args=(sock,))
rxthread.daemon = True
rxthread.start()

while True:
    time.sleep(0.5)
    if flag == 0:
        cmd = input("Please enter the data to send from A to C: ")
        try:
            cmd = cmd.encode("utf-8")
        except:
            print("ENCODE ERROR")

        MESSAGE = cmd
        sock.sendto(MESSAGE, (TARGET_IP, UDP_PORT))
        print(f"Sent message: {MESSAGE} to {TARGET_IP}:{UDP_PORT}")
