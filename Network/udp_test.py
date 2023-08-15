import socket
import os

# UDPのポート番号を指定
UDP_PORT = 50000
BUFFER_SIZE = 1  # 1バイトのデータを受信

# ソケットを作成してバインド
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("192.168.3.5", UDP_PORT))

while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    print(f"Received message: {data} from {addr}")

    if data==b"\x41":
        print("Camera activate")
        sock.sendto(b'0', addr)
        sock.sendto(b'a', addr)  # 「a」のバイトデータをPCに返す
        
        response, _ = sock.recvfrom(1)  # PCからの返信を待つ
        if response == b'j':
            os.system("libcamera-raw -t 2000 -o test.jpg")
            sock.sendto(b'j', addr)  # 「j」のバイトデータをPCに返す
        if response == b'r':
            os.system("libcamera-raw -t 2000 -o test.raw")
            sock.sendto(b'r', addr)  # 「r」のバイトデータをPCに返す
        if response == b'n':
            #os.system("libcamera-raw -t 2000 -o test.jpg")
            sock.sendto(b'n', addr)  # 「n」のバイトデータをPCに返す
    elif data==b"\x42":
        print("HK data are ...")
        response="HK data abcdef...".encode('utf-8')
        sock.sendto(response, addr)
    elif data==b"\x43" :
        print("reboot")
        response="now rebooting".encode('utf-8')
        sock.sendto(response, addr)
        #os.system("python ./../Camera-test/Experiment/capture.py")
    else :
        response="正規の信号ではありませんでした".encode('utf-8')
        sock.sendto(response, addr)
