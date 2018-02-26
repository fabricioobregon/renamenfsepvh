from renomeiapdf import renomeiapdf
from Tkinter import Tk
from tkFileDialog import askdirectory

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
folder = askdirectory() # show an "Open" dialog box and return the path to the selected file
renomeiapdf(folder+"/")
'''
from renomeiapdf import renomeiapdf
from importapdf import importapdf
import sys
Path = sys.argv[1]
renomeiapdf(Path)
'''
