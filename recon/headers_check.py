import requests

def check_security_headers(url):
    if not url.startswith("http"):
        url = "http://" + url

    try:
        r = requests.get(url)
        headers = r.headers
        print(f"\n[+] Verificando headers de {url}")
        expected = [
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "X-XSS-Protection"
        ]
        for header in expected:
            if header in headers:
                print(f"[+] {header}: {headers[header]}")
            else:
                print(f"[-] {header} NÃO encontrado")
    except Exception as e:
        print("Erro:", e)
