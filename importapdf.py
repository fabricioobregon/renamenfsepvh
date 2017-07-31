#encoding: utf-8
import lerpdf, codecs
def importapdf(arquivo):
    #Iniciando variaveis
    vencimento = ""
    nomenota = ""
    #Envia o caminho do arquivo para a funcao lerpdf e salva na variavel line
    line = lerpdf.lerpdf(arquivo)
    #Conta a quantidade de linhas do arquivo
    counter = len(line)
    #Procura os dados nas possiveis linhas do campo e salva nas variaveis
    for j in range(counter):
        if str(line[j])[:-12] == "Vencimento":
            vencimento = str(line[j])[-10:-8]
        if str(line[j]) == "Competência":
            competencia = str(line[j+1]).replace("/","")
        if str(line[j]) == "Número da Nota":
            nota = str(line[j+2])
        if str(line[j]) == "CNPJ/CPF":
            inscfederal = str(line[j+1])
        if str(line[j]) == "9119":
            emissor = str(line[j])
    #Testa o emissor para formar o nome do arquivo
    if emissor == "9119":
        nomenota = "-NFS" + vencimento + "-" + competencia + ".pdf"
    else:
        nomenota = "-ENFS" + vencimento + "-" + competencia + ".pdf"
    return inscfederal, nota, nomenota