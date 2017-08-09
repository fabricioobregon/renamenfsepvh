from renomeiapdf import renomeiapdf
from importapdf import importapdf
import sys
Path = sys.argv[1]
renomeiapdf(Path)








'''
def zero():
    renomeiapdf(Path, importapdf)
    return "zero"

def one():
    return "one"

def numbers_to_functions_to_strings(argument):
    switcher = {
        0: zero,
        1: one,
        2: lambda: "two",
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "nothing")
    # Execute the function
    return func()
#if sys.argv[2] == 'nfse':
#    renomeiapdf(Path, importanfse)"
#numbers_to_functions_to_strings(sys.argv[2])
'''