import socket
import sys

port = 2500

# 서버 소켓 생성
s_sock = socket.socket()
# 모든 호스트를 받겠다는 의미
host = ''
s_sock.bind((host.port))
s_sock.listen(1)

print("Waiting for Connection")

# 클라이언트의 연결을 대기
# 소켓의 연결을 끊기지 않게: 대기 상태로 잠정적 연결상태를 유지하는것
c_sock, addr = s_sock.accept()
print("connetion from", addr)

# 클라이언트로부터 메세지 수신 및 출력
msg = c_sock.recv(1024)
print(msg.decode())
# 클라이언트로부터 파일 이름 입력받기
# input으로 입력 받는 데이터는 기본적으로 string
filename = input("파일 이름")

# 클라이언트에 파일 이름 전송
# 그러므로 encoding
c_sock.send(filename.encode())

# 파일 열어서 전송
with open("./dummy/" + filename, 'rb') as f:
    c_sock.sendfile(f,0)

print("Sending Complete")
c_sock.close()
