import socket
import threading
import time

fmt_line = "----"


# Specify IP address and UDP port number for Raspberry Pi Zero
TARGET_IP = input("Target IP is: ")  # "192.168.3.5"

UDP_PORT = 50000


# 受信機能を持つ関数
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
            print("正規の信号ではありませんでした")

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
                print("responseを待っています")

                response, _ = sock.recvfrom(1)

                if response == b"j":
                    print("\n A jpeg image was taken")

                    break
                if response == b"r":
                    print("\n raw画像が撮影されました")
                    break
                if response == b"n":
                    print("\n 撮影を中止しました")


# ソケットの作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", UDP_PORT))  # 任意のアドレスからの受信を許可

# 受信機能を別のスレッドで開始
rxthread = threading.Thread(target=receive_messages, args=(sock,))
rxthread.daemon = True
rxthread.start()

while True:
    time.sleep(0.5)
    if flag == 0:
        cmd = input("送信するデータをA~Cで入力してください: ")
        try:
            cmd = cmd.encode("utf-8")
        except:
            print("ENCODE ERROR")

        MESSAGE = cmd
        sock.sendto(MESSAGE, (TARGET_IP, UDP_PORT))
        print(f"Sent message: {MESSAGE} to {TARGET_IP}:{UDP_PORT}")
