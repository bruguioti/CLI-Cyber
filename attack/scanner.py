import socket

def scan_ports(target_ip, ports=[21, 22, 23, 25, 53, 80, 443, 8080]):
    print(f"[+] Iniciando scan em {target_ip}")
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"[+] Porta {port} aberta")
            sock.close()
        except Exception as e:
            print(f"Erro na porta {port}: {e}")
