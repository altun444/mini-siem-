import socket
import json

HOST = '0.0.0.0'
PORT = 5140  # Mini SIEM log qəbuledici portu

# Sadə təhlükə aşkarlama qaydaları
RULES = ["failed password", "unauthorized", "root access", "attack"]

def analyze_log(log_data):
    log_lower = log_data.lower()
    for rule in RULES:
        if rule in log_lower:
            print(f"[ALARM] Şübhəli fəaliyyət aşkarlandı: {rule.upper()} -> Log: {log_data.strip()}")
            # Burada insidenti bazaya və ya GitHub panelinə çıxarmaq olar

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[*] Mini SIEM Server {PORT} portunda işə düşdü. Loglar gözlənilir...")
        while True:
            conn, addr = s.accept()
            with conn:
                data = conn.recv(1024)
                if not data:
                    break
                log_message = data.decode('utf-8')
                analyze_log(log_message)

if __name__ == "__main__":
    start_server()
