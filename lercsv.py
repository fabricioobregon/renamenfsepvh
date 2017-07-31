#encoding: utf-8
import csv
def lercsv():
    with open('Lista-Clientes.xls.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=';')
        arquivolido = list(reader)
        clientes = len(arquivolido)
    listapronta = [[0 for x in range(2)] for y in range(clientes)] 
    #print len(clientslist)
    for i in range (clientes):
        listapronta[i][0] = arquivolido[i][0]
        listapronta[i][1] = (arquivolido[i][2]).replace('.','').replace('/','').replace('-','')
    return listapronta