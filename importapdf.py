# encoding: utf-8
from lerpdf import lerpdf


def importapdf(arquivo):

    # Envia o caminho do arquivo para a funcao lerpdf e salva na variavel arquivoaberto
    arquivoaberto = lerpdf(arquivo)
    if str(arquivoaberto[0]).strip() == "Prefeitura do Município de Porto Velho":
        inscfederal, nota, nomenota = nfse(arquivoaberto)
    elif str(arquivoaberto[0]).strip() == "033-7":
        inscfederal, nota, nomenota = boleto(arquivoaberto)
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
        nomenota = "-NFS" + vencimento + "-" + competencia + ".pdf"
    else:
        nomenota = "-ENFS" + vencimento + "-" + competencia + ".pdf"
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
            elif int(mes) < 11:
                competencia = "0" + str(int(mes)-1) + ano
            else:
                competencia = str(int(mes)-1) + ano
            if str(arquivoaberto[linha - 7]).strip() == "D. DUWE CONTABILIDADE LTDA.":
                emissor = "9119"
            else:
                emissor = ""
        if str(arquivoaberto[linha]).strip() == "Sacado:":
            busca = str(arquivoaberto[linha + 2]).split()
            inscfederal = busca[busca.index("CNPJ/CPF:")+1]
            inscfederal = inscfederal.replace("/","").replace(".","").replace("-","")
    # Testa o emissor para formar o nome do arquivo
    if emissor == "9119":
        nomenota = "-BLT" + vencimento + "-" + competencia + ".pdf"
    else:
        nomenota = "-EBLT" + vencimento + "-" + competencia + ".pdf"
    return inscfederal, nota, nomenota