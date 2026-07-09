import socket
import time

SERVER_IP = '127.0.0.1'  # Serverin IP-si
SERVER_PORT = 5140

def send_log(message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_IP, SERVER_PORT))
            s.sendall(message.encode('utf-8'))
    except ConnectionRefusedError:
        print("[-] Serverə qoşulmaq mümkün olmadı.")

if __name__ == "__main__":
    # Test üçün uğursuz giriş cəhdi simulyasiyası
    print("[+] Test logu göndərilir...")
    send_log("User admin: Failed password for invalid user root from 192.168.1.50")
