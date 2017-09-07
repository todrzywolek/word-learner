from tkinter.filedialog import askopenfilename
from tkinter import Tk

def open_file(open_options):
    Tk().withdraw()
    try:
        filename = askopenfilename(**open_options)
        return filename

    except FileNotFoundError:
        print("Incorrect file loaded")
    
    
