#encoding: utf-8
import csv
def lercsv():
    #Abre o arquivo csv com a lista de clientes
    with open('Lista-Clientes.xls.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=';')
        arquivolido = list(reader)
        clientes = len(arquivolido)
    listapronta = [[0 for x in range(2)] for y in range(clientes)]
    #print len(clientslist)
    for linha in range(clientes):
        listapronta[linha][0] = arquivolido[linha][0]
        listapronta[linha][1] = (arquivolido[linha][2]).replace('.','').replace('/','').replace('-','')
    return listapronta