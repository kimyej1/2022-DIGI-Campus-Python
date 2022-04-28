# 25Chatting.py

from socket import *    # socket에 있는거 모든걸 import해라

PORT = 10000

def udpClient():
    client = socket(AF_INET, SOCK_DGRAM)    # UDP : User Datagram Protocol (send and pray)
    client.sendto('Hello I am Python'.encode(), ("127.0.0.1", PORT))
    s, addr = client.recvfrom(1024)         # s: message, addr: IP 두개를 리시브함
    print(s)                                # IP는 필요없고 메시지만 출력해줘~

if __name__ == "__main__":
    udpClient()