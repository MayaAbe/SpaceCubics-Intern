import socket
#import subprocess


def main():
    # Specify the UDP port number
    UDP_PORT = 50000
    BUFFER_SIZE = 1  # Receive 1 byte of data

    # Create a socket and bind
    SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    SOCK.bind(("192.168.3.5", UDP_PORT))

    while True:
        DATA, ADDR = SOCK.recvfrom(BUFFER_SIZE)
        print(f"Received message: {DATA} from {ADDR}")

        if DATA == b"a":
            print("Camera activate")
            SOCK.sendto(b"0", ADDR)
            SOCK.sendto(b"A", ADDR)  # Return byte data 'A' to the PC

            response, _ = SOCK.recvfrom(1)  # Wait for a reply from the PC
            if response == b"j":
                #subprocess.run(["libcamera-jpeg", "-o", "test.jpg"], check=True)
                SOCK.sendto(b"j", ADDR)  # Return byte data 'j' to the PC
            if response == b"r":
                #subprocess.run(["libcamera-raw", "-t", "2000", "-o", "test.raw"], check=True)
                SOCK.sendto(b"r", ADDR)  # Return byte data 'r' to the PC
            if response == b"n":
                SOCK.sendto(b"n", ADDR)  # Return byte data 'n' to the PC
        elif DATA == b"b":
            print("HK data are ...")
            response = "HK data abcdef...".encode("utf-8")
            SOCK.sendto(response, ADDR)
        elif DATA == b"c":
            print("reboot")
            response = "now rebooting".encode("utf-8")
            SOCK.sendto(response, ADDR)
        else:
            response = "Received an irregular signal".encode("utf-8")
            SOCK.sendto(response, ADDR)
        DATA = b""

if __name__ == "__main__":
    main()
