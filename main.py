from core.banner import show_banner
from core.menu import show_menu
from recon.headers_check import check_security_headers
from recon.whois_dns import get_domain_info
from attack.scanner import scan_ports
from attack.brute_ssh import ssh_brute_force
from attack.brute_http import brute_http_login
from analysis.nmap_check import nmap_vuln_scan
from core.utils import resolve_target
from recon.network_scan import scan_lan
from core.utils import resolve_target

def main():
    show_banner()
    while True:
        show_menu()
        op = input("Escolha: ")

        if op == '1':
            target = input("Host/IP: ")
            ip = resolve_target(target)
            if ip:
                scan_ports(ip)
        elif op == '2':
            ip = input("IP do SSH: ")
            user = input("Usuário: ")
            wordlist = input("Wordlist: ")
            ssh_brute_force(ip, user, wordlist)
        elif op == '3':
            url = input("URL do login: ")
            user = input("Usuário: ")
            wordlist = input("Wordlist: ")
            brute_http_login(url, user, wordlist)
        elif op == '4':
            site = input("URL do site: ")
            check_security_headers(site)
        elif op == '5':
            dominio = input("Domínio: ")
            get_domain_info(dominio)
        elif op == '6':
            alvo = input("Host/IP: ")
            nmap_vuln_scan(alvo)
        elif op == '7':
            entrada = input("Digite sua sub-rede (ex: 192.168.0.0/24) [Enter para padrão]: ")
            subnet = entrada.strip() if entrada.strip() else "192.168.0.0/24"
            scan_lan(subnet)
        elif op == '0':
            print("Saindo... até a próxima com bruna.code!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
