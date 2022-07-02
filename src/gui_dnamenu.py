import tkinter as tk
import tkinter.filedialog as tkf  # python3
import fastareader as fasta


class WDnaMenu(tk.Frame):
    def __init__(self, racine=None):
        "Le constructeur de la menubar"
        tk.Frame.__init__(self, racine)
        self.racine = racine

        self.menu = tk.Menu(racine)

        self.createMenu()

        racine.config(menu=self.menu)

    def createMenu(self):
        # http://stackoverflow.com/questions/4140437/python-tkinter-interactively-validating-entry-widget-content
        w = self.menu
        w.add_cascade(label="File", menu=self.createFileMenu())
        w.add_cascade(label="Edit", menu=self.createEditMenu())
        w.add_cascade(label="Tool", menu=self.createToolMenu())

    def createFileMenu(self):
        # =============================================File option
        m = tk.Menu(self, tearoff=0)
        m.add_command(label="Open Fasta", command=self.cmdOpenFasta)
        m.add_command(label="Save", command=lambda: self.emptyCmd("File.Save"))
        m.add_separator()
        m.add_command(label="Exit", command=self.racine.quit)
        return m

    def createEditMenu(self):
        # =============================================Edit option
        m = tk.Menu(self, tearoff=0)
        m.add_command(label="Cut", command=lambda: self.emptyCmd("Edit.Cut"))
        m.add_command(label="Copy", command=lambda: self.emptyCmd("Edit.Copy"))
        m.add_command(
            label="Paste", command=lambda: self.emptyCmd("Edit.Paste"))
        return m

    def createToolMenu(self):
        # =============================================Tool option
        m = tk.Menu(self, tearoff=0)
        m.add_command(label="Tool1", command=lambda: self.emptyCmd("Tool.1"))
        return m

    def emptyCmd(self, menu):
        print("in emptyCmd:", menu)
        # for arg in args:
        #   print(arg)

    def cmdOpenFasta(self):
        opts = {'filetypes': (('fasta', '.fasta'),
                              ('fsta', '.fsta'),
                              ('Text files', '.txt'),
                              ('All files', '.*'),)}
        opts['title'] = 'Select a file to open...'
        fn = tkf.askopenfilename(**opts)
        if len(fn) > 0:
            self.seq = fasta.fastaReader(fn)
            print("in cmdOpenFasta", self.bindtags())
            print("length:", len(self.seq))
            self.event_generate("<<NewDNA>>")

    def getDNA(self):
        return self.seq


if __name__ == '__main__':

    def affiche(event):
        print("in affiche")
        print(event.widget.getDNA())

# http://zetcode.com/gui/tkinter/menustoolbars/
    print("in main")
    root = tk.Tk()
    fm = WDnaMenu(root)
    fm.pack()

    root.bind_all("<<NewDNA>>", affiche)

    root.mainloop()
