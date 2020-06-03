from tkinter import Tk

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

def main():
    tk_to_clipboard('test')

if __name__ == '__main__':
    main()
    
