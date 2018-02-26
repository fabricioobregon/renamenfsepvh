#encoding: utf-8
import subprocess


def lerpdf(pdffile):
  #Executa um programa e retorna o stdout
  proc = subprocess.Popen(["python", "pdf2txt.py", pdffile], stdout=subprocess.PIPE)
  #Iniciei o array
  linhas = []
  #Enquanto nao e o final do arquivo, cada linha e adicionada no array linhas
  while True:
    line = proc.stdout.readline()
    if line != '':
      linhas.append(line.strip())
    else:
      break
  #Retorna o array linhas
  return linhas