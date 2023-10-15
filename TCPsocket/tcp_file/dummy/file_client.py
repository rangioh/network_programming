import socket

s_sock = socket.socket()
host = "localhost"
# 클라이언트 포트번호는: 설정하는 이유는 내 컴퓨터 내부에 설치하는 서버 클라이언트라서
port = 2500

# 서버에 연결
# 주소는 항상 ip port 튜플로 들어가야한다.
s_sock.send((host.port))


# 서버에 "I am ready" 메세지 전송
# 메세지 전송 시 string을 encode해서 보내야함
s_sock.send("I am ready".encode())

# 서버로부터 파일 이름 수신
# 전송 받은 메세지 decoding
fn = s_sock.recv(1024).decode()

# 파일을 "recv"라는 이름으로 현재 디렉토리에 저장
with open("./dummy/" + "recv", 'wb') as f:
    print("Receiving")
    while True:
        data = s_sock.recv(8192)
        if not data:
            break
        f.write(data)

print("Download Complete")
s_sock.close()