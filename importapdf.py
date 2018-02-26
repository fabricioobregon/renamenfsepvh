# encoding: utf-8
from lerpdf import lerpdf


def importapdf(arquivo):
    inscfederal =""
    nota = ""
    nomenota = ""
    # Envia o caminho do arquivo para a funcao lerpdf e salva na variavel arquivoaberto
    try:
        arquivoaberto = lerpdf(arquivo)
        if str(arquivoaberto[0]).strip() == "Prefeitura do Município de Porto Velho":
            inscfederal, nota, nomenota = nfse(arquivoaberto)
        elif (str(arquivoaberto[0]).strip() == "033-7") or (str(arquivoaberto[0]).strip() == "Cedente"):
            inscfederal, nota, nomenota = boleto(arquivoaberto)
    except:
        return 0
    return inscfederal, nota, nomenota

def nfse(arquivoaberto):
    # Iniciando variaveis
    vencimento = ""
    competencia = ""
    nota = ""
    inscfederal = ""
    emissor = ""
    # Conta a quantidade de linhas do arquivo
    contador = len(arquivoaberto)
    # Procura os dados nas possiveis linhas do campo e salva nas variaveis
    for linha in range(contador):
        if str(arquivoaberto[linha])[:-12] == "Vencimento":
            vencimento = str(arquivoaberto[linha])[-10:-8]
        if str(arquivoaberto[linha]) == "Competência":
            competencia = str(arquivoaberto[linha + 1]).replace("/", "")
        if str(arquivoaberto[linha]) == "Número da Nota":
            nota = str(arquivoaberto[linha + 2])
        if str(arquivoaberto[linha]) == "CNPJ/CPF":
            inscfederal = str(arquivoaberto[linha + 1])
        if str(arquivoaberto[linha]) == "9119":
            emissor = str(arquivoaberto[linha])
    # Testa o emissor para formar o nome do arquivo
    if emissor == "9119":
        nomenota = "-NFS" + vencimento + "-" + competencia
    else:
        nomenota = "-ENFS" + vencimento + "-" + competencia
    return inscfederal, nota, nomenota

def boleto(arquivoaberto):
    # Iniciando variaveis
    vencimento = ""
    competencia = ""
    nota = ""
    inscfederal = ""
    emissor = ""
    # Conta a quantidade de linhas do arquivo
    contador = len(arquivoaberto)
    # Procura os dados nas possiveis linhas do campo e salva nas variaveis
    for linha in range(contador):
        if str(arquivoaberto[linha]).strip() == "Recebi(emos) o boleto":
            dia,mes,ano = str(arquivoaberto[linha - 1]).split("/")
            vencimento = dia
            if int(dia) > 25:
                competencia = mes+ano
            elif int(mes) < 2:
                competencia = str(int(mes) + 11) + str(int(ano) - 1)
            elif int(mes) < 11:
                competencia = "0" + str(int(mes)-1) + ano
            else:
                competencia = str(int(mes)-1) + ano
        if str(arquivoaberto[linha]).strip() == "D. DUWE CONTABILIDADE LTDA.":
            emissor = "9119"
        if str(arquivoaberto[linha]).strip() == "Sacado:":
            try:
                busca = str(arquivoaberto[linha + 2]).split()
                inscfederal = busca[busca.index("CNPJ/CPF:")+1]
                inscfederal = inscfederal.replace("/","").replace(".","").replace("-","")
            except:
                inscfederal = "Sem inscricao"
    # Testa o emissor para formar o nome do arquivo
    if emissor == "9119":
        nomenota = "-BLT" + vencimento + "-" + competencia
    else:
        nomenota = "-EBLT" + vencimento + "-" + competencia
    return inscfederal, nota, nomenota