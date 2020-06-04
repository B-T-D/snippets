from tkinter import Tk
import pyperclip

def tk_to_clipboard(string):
    """Copies to the system clipboard using Tkinter.

    Args:
        string (str): a string

    Returns:
        None
    """
    tkobj = Tk()
    tkobj.withdraw()
    tkobj.clipboard_clear()
    tkobj.clipboard_append(string)
    tkobj.update()
    tkobj.destroy()

def pyperclip_to_clipboard(string):
    """Pyperclip method."""
    pyperclip.copy(string)
    
def main():
    tk_to_clipboard('tkinter test')
    pyperclip_to_clipboard('pyperclip test')

if __name__ == '__main__':
    main()
    
