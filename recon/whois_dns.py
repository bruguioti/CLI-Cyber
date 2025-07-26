import whois
import dns.resolver

def get_domain_info(domain):
    print("[+] WHOIS:")
    try:
        print(whois.whois(domain))
    except Exception as e:
        print("Erro WHOIS:", e)

    print("\n[+] DNS:")
    for rtype in ['A', 'MX', 'NS']:
        try:
            result = dns.resolver.resolve(domain, rtype)
            for res in result:
                print(f"{rtype}: {res}")
        except:
            print(f"[-] Nenhum registro {rtype} encontrado.")
