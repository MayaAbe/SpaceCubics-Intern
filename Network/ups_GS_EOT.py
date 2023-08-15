import socket

TARGET_IP = "192.168.3.5"
UDP_PORT = 50000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", UDP_PORT))

# ハンドシェイク用のバイナリデータを送信
sock.sendto(b"\x05", (TARGET_IP, UDP_PORT))

# 応答を待機
data, addr = sock.recvfrom(1)

# 応答が "\x06" であるか確認
if data == b"\x06":
    message = "送信するデータをA~Cで入力してください: \n" \
                "  A: 画像撮影\n" \
                "  B: HKデータ取得\n" \
                "  C: rebootをかける\n" \
                "入力してください: "
    
    cmd = input(f"{message}")
    MESSAGE = cmd.encode('utf-8')
    
    sock.sendto(MESSAGE, (TARGET_IP, UDP_PORT))
    print(f"Sent message: {MESSAGE} to {TARGET_IP}:{UDP_PORT}")
else:
    print("Expected handshake response not received.")
