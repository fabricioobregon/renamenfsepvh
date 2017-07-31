#encoding: utf-8
import glob, importapdf, os, lercsv
#Caminho para os arquivos limitados a PDF
pathPdf = "Notas/"
notas = pathPdf + "*.pdf"
#Joga todos os nomes de arquivos no objeto arquivos
arquivos = glob.glob(notas)
#Joga o conteudo do csv de clientes e joga na varial listaclientes
listaclientes = lercsv.lercsv()
counter = len(listaclientes)
#Percorres todos os arquivos e chama a funcao que renomia para pdf
for i in arquivos:
    inscfederal, nota, nomenota = importapdf.importapdf(i.strip())
    #print inscfederal, nota, nomenota
    for j in range (counter):
        if listaclientes[j][1] == inscfederal:
            inscfederal = listaclientes[j][0]
    nomearquivo = inscfederal + nomenota
    #Renomeia os arquivos de acordo com os dados lidos
    os.rename(i ,pathPdf + nomearquivo)