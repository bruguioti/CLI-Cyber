import subprocess

def nmap_vuln_scan(target_ip):
    print(f"[+] Rodando Nmap em {target_ip}")
    try:
        subprocess.run(["nmap", "-sV", "--script=vuln", target_ip])
    except Exception as e:
        print("Erro ao executar Nmap:", e)
