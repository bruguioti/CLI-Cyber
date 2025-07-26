import datetime

def salvar_relatorio(nome_arquivo, conteudo):
    data = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    caminho = f"relatorios/{nome_arquivo}-{data}.txt"
    with open(caminho, 'w') as f:
        f.write(conteudo)
    print(f"[+] Relatório salvo em {caminho}")
