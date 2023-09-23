import socket

# UDPのポート番号の設定
PORT = 12345

# ソケットの作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', PORT))  # IPアドレスを指定せずにバインド

while True:
    # 1バイトのデータを受け取る
    data, addr = sock.recvfrom(1)

    # 受け取ったデータを送信元のアドレスに返す
    sock.sendto(data, addr)

# ソケットを閉じる
# クローズのプログラムがあるからには地上局が自動的にクローズされることは無さそう
sock.close() 
