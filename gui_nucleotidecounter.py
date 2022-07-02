import tkinter as tk
import nucleotidecounter as nc

class WNucleotideCounter(tk.Frame):
    def __init__(self, racine=None):
        "Le constructeur du compteur de nucléotides A T G C"
        tk.Frame.__init__(self, racine)
        self.racine=racine
        self.createWidget()

    def createWidget(self):
        #afficher les totaux pour les lettres A, G, C, T
        
        for elt in [('A', 0, 0), ('T', 0,2), ('G', 1, 0), ('C', 1, 2)]:
            self.buildCounter(elt[0], elt[1], elt[2])

    def buildCounter(self, letter, x, y):
            cmd="self.{0:}LblName=tk.Label(self, text=' {0:} :')".format(letter)
            exec(cmd)
            cmd="self.{}LblName.grid(row={},column={})".format(letter, x, y)
            exec(cmd)
            cmd="self.{}LblVar=tk.StringVar()".format(letter)
            exec(cmd)
            cmd="self.{}LblVar.set('    ')".format(letter)
            exec(cmd)
            cmd="self.{0:}LblVal=tk.Label(self, textvariable=self.{0:}LblVar)".format(letter)
            exec(cmd)
            cmd="self.{}LblVal.grid(row={},column={})".format(letter, x, y+1)
            exec(cmd)
        
    def onUpdateDnaSequenceEvent(self, event):
        brin=event.widget.getDNA()
        print("==>brin in DNA counter", brin)
        letters=nc.countLetters(brin)
    #http://docs.python.org/3.3/library/string.html#formatspec
        for c in ['A', 'T', 'G', 'C']:
            cmd="self.{0:}LblVar.set('{1:4d}')".format(c, letters[c])
            print(cmd)
            eval(cmd)    
        
if __name__ == '__main__':
    import dnagen as dna
    class Appli(tk.Tk):
        def __init__(self):
            tk.Tk.__init__(self)

        def getDNA(self):
            brin=dna.genereDNA(50)
            print(brin)
            return brin

    def sendEvent():
        root.event_generate("<<UpdateDNA>>")
        root.after(2000, sendEvent )


    print("in main")
    root=Appli()
    wcnt=WNucleotideCounter(root)
    wcnt.pack()
    root.bind_all("<<UpdateDNA>>", wcnt.onUpdateDnaSequenceEvent)
    print("In loop")
    root.after(2000, sendEvent )
    
    root.mainloop()
