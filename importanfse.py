#encoding: utf-8
import lerpdf, codecs
def importanfse(arquivo):
    #Iniciando variaveis
    vencimento = ""
    competencia = ""
    nota = ""
    inscfederal = ""
    emissor = "" 
    nomenota = ""
    #Envia o caminho do arquivo para a funcao lerpdf e salva na variavel line
    arquivolido = lerpdf.lerpdf(arquivo)
    #Conta a quantidade de linhas do arquivo
    counter = len(arquivolido)
    #Procura os dados nas possiveis linhas do campo e salva nas variaveis
    for linha in range(counter):
        if str(arquivolido[linha])[:-12] == "Vencimento":
            vencimento = str(arquivolido[linha])[-10:-8]
        if str(arquivolido[linha]) == "Competência":
            competencia = str(arquivolido[linha+1]).replace("/","")
        if str(arquivolido[linha]) == "Número da Nota":
            nota = str(arquivolido[linha+2])
        if str(arquivolido[linha]) == "CNPJ/CPF":
            inscfederal = str(arquivolido[linha+1])
        if str(arquivolido[linha]) == "9119":
            emissor = str(arquivolido[linha])
    #Testa o emissor para formar o nome do arquivo
    if emissor == "9119":
        nomenota = "-NFS" + vencimento + "-" + competencia + ".pdf"
    else:
        nomenota = "-ENFS" + vencimento + "-" + competencia + ".pdf"
    return inscfederal, nota, nomenota