import subprocess
import ipaddress
import socket
from concurrent.futures import ThreadPoolExecutor

# Obter IP local da máquina e deduzir sub-rede
def descobrir_subrede():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))  # conexão simulada
        ip_local = s.getsockname()[0]
        s.close()

        ip_parts = ip_local.split('.')
        subnet = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.0/24"
        return subnet
    except Exception as e:
        print("Erro ao descobrir IP local:", e)
        return "192.168.0.0/24"  # fallback

def ping_host(ip):
    ip_str = str(ip)
    try:
        result = subprocess.run(['ping', '-c', '1', '-W', '1', ip_str],
                                stdout=subprocess.DEVNULL)
        return result.returncode == 0
    except:
        return False

def check_ports(ip):
    common_ports = [21, 22, 80, 443]
    ip_str = str(ip)
    for port in common_ports:
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            if sock.connect_ex((ip_str, port)) == 0:
                sock.close()
                return True
            sock.close()
        except:
            pass
    return False

def scan_host(ip):
    if ping_host(ip):
        print(f"[+] Host ativo via ping: {ip}")
    elif check_ports(ip):
        print(f"[+] Host ativo via porta aberta: {ip}")

def scan_lan(subnet=None):
    if not subnet:
        subnet = descobrir_subrede()

    print(f"[+] Escaneando a rede {subnet}...")
    try:
        ips = ipaddress.IPv4Network(subnet, strict=False)
    except Exception as e:
        print("[-] Sub-rede inválida:", e)
        return

    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(scan_host, ips)

if __name__ == "__main__":
    entrada = input("Digite sua sub-rede (ex: 192.168.0.0/24) [Enter para detectar]: ")
    subnet = entrada.strip() if entrada.strip() else None
    scan_lan(subnet)
