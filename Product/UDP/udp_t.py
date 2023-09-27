import socket

# サーバーのIPアドレスとポート番号の設定
SERVER_IP = '192.168.3.5'  # サーバーのIPアドレス
PORT = 12345            # サーバーのポート番号

# ソケットの作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 1バイトのデータを送信
data_to_send = b'm'  # 例: 'A'の文字をバイト形式で送信
sock.sendto(data_to_send, (SERVER_IP, PORT))

# サーバーからの応答を受け取る
response, _ = sock.recvfrom(1024)
print(f"Received from server: {response.decode()}")

# ソケットを閉じる
sock.close()
