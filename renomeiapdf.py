#encoding: utf-8
import glob, os, lercsv
from lercsv import lercsv
from importapdf import importapdf

from importapdf import importapdf
#Funcao para ler os arquivos. Recebe a pasta onde os arquivos estao
def renomeiapdf(pathPdf):
    #Caminho para os arquivos, limitados a PDF
    notas = pathPdf + "*.pdf"
    #Joga todos os nomes de arquivos no objeto arquivos
    arquivos = glob.glob(notas)
    #Joga o conteudo do csv de clientes e joga na varial listaclientes
    listaclientes = lercsv()
    counter = len(listaclientes)
    #Percorres todos os arquivos e chama a funcao que renomia para pdf
    for arquivo in arquivos:
        try:
            inscfederal, nota, nomenota = importapdf(arquivo.strip())
            #print inscfederal, nota, nomenota
            for linha in range(counter):
                if listaclientes[linha][1] == inscfederal:
                    inscfederal = listaclientes[linha][0]
            nomearquivo = inscfederal + nomenota
            # Renomeia os arquivos de acordo com os dados lidos
            os.rename(arquivo, pathPdf + nomearquivo)
        except:
            pass
    return