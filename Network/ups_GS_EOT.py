import socket

TARGET_IP = "192.168.3.5"
UDP_PORT = 50000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", UDP_PORT))

# Send binary data for handshake
sock.sendto(b"\x05", (TARGET_IP, UDP_PORT))

# Wait for response
data, addr = sock.recvfrom(1)

# Check if the response is "\x06"
if data == b"\x06":
    message = "Please enter the data to send from A to C: \n" \
                "  A: Take a picture\n" \
                "  B: Get HK data\n" \
                "  C: Trigger a reboot\n" \
                "Please enter: "
    
    cmd = input(f"{message}")
    MESSAGE = cmd.encode('utf-8')
    
    sock.sendto(MESSAGE, (TARGET_IP, UDP_PORT))
    print(f"Sent message: {MESSAGE} to {TARGET_IP}:{UDP_PORT}")
else:
    print("Expected handshake response not received.")
