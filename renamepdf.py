from renomeiapdf import renomeiapdf
from importanfse import importanfse
import sys
Path = sys.argv[1]

def zero():
    renomeiapdf(Path, importanfse)
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
#    renomeiapdf(Path, importanfse)
numbers_to_functions_to_strings(sys.argv[2])