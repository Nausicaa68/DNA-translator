import tkinter as tk

class WDnaPresenter(tk.Frame):
    def __init__(self, racine=None):
        "Affiche la séquence d'ADN dasn un widget Text"
        tk.Frame.__init__(self, racine)
        self.racine=racine
        self.createWidget()

    def createWidget(self):
        self.vsb=tk.Scrollbar(self, orient=tk.VERTICAL)
        self.vsb.pack(fill=tk.Y, side=tk.RIGHT)
        
        self.textDna=tk.Text(self, width=60, height=10)
        self.textDna['yscrollcommand']=self.vsb.set
        self.textDna.config(state=tk.DISABLED)
        
        self.vsb.config(command=self.textDna.yview)
        
        #http://effbot.org/tkinterbook/grid.htm
        self.textDna.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def onNewDnaSequenceEvent(self, event):
        print("onNewDnaSequenceEvent")
        brin=event.widget.getDNA()
        self.textDna.config(state=tk.NORMAL)
        self.textDna.delete("0.0",tk.END)
        self.textDna.insert(tk.END,"".join(brin))
        self.textDna.config(state=tk.DISABLED)
        self.event_generate("<<UpdateDNA>>")

    def getDNA(self):
        print("dna de Text:", tk.END)
        brin= self.textDna.get(1.0, tk.END)
        brin=brin.strip(" \n")
        return brin

if __name__ == '__main__':
    import dnagen as dna
    class Appli(tk.Tk):
        def __init__(self):
            tk.Tk.__init__(self)

        def getDNA(self):
            brin=dna.genereDNA(50)
            print("brin de root:<","".join(brin),">",sep="")
            return brin

    def sendNewDnaEvent():
        print("new DNA event")
        root.event_generate("<<NewDNA>>")
        root.after(2000, sendNewDnaEvent )

    def onUpdateDnaSequenceEvent(event):
        brin=event.widget.getDNA()
        print("Update:<",brin,">", sep="")
        

    print("in main")
    root=Appli()
    wpres=WDnaPresenter(root)
    wpres.pack()
    root.bind_all("<<NewDNA>>", wpres.onNewDnaSequenceEvent)
    root.bind_all("<<UpdateDNA>>", onUpdateDnaSequenceEvent)
    print("In loop")
    root.after(2000, sendNewDnaEvent )
    
    root.mainloop()
