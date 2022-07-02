import tkinter as tk
import translator as dnatl


class WDnaTranslator(tk.Frame):

    def __init__(self, racine=None):
        "Affiche la séquence de proteine"
        tk.Frame.__init__(self, racine)
        self.racine = racine
        self.source = None
        self.createWidget()

    def createWidget(self):
        self.top = tk.Frame()
        w = self.top
        w.pack(side=tk.TOP, fill=tk.X)

        #-------- Phase
        self.textLbl = tk.Label(w, text="Phase :")
        self.textLbl.pack(side=tk.LEFT)

        self.varPhase = tk.IntVar()
        self.Rphase1 = tk.Radiobutton(w, text="0",
                                      variable=self.varPhase, value=0,
                                      command=self.translateDNA)
        self.Rphase1.pack(side=tk.LEFT)
        self.Rphase2 = tk.Radiobutton(w, text="1",
                                      variable=self.varPhase, value=1,
                                      command=self.translateDNA)
        self.Rphase2.pack(side=tk.LEFT)
        self.Rphase3 = tk.Radiobutton(w, text="2",
                                      variable=self.varPhase, value=2,
                                      command=self.translateDNA)
        self.Rphase3.pack(side=tk.LEFT)

        # -------- 1 ou 3 lettres
        self.varOneOr3Letter = tk.IntVar()
        self.Rletter1 = tk.Radiobutton(w, text="3",
                                       variable=self.varOneOr3Letter, value=0,
                                       command=self.translateDNA)

        self.Rletter1.pack(side=tk.RIGHT)
        self.Rletter2 = tk.Radiobutton(w, text="1",
                                       variable=self.varOneOr3Letter, value=1,
                                       command=self.translateDNA)
        self.Rletter2.pack(side=tk.RIGHT)

        self.Rletter1.select()

        self.textLbl = tk.Label(w, text="1 ou 3 lettre(s) :")
        self.textLbl.pack(side=tk.RIGHT)

        # ---------- scrollbar
        self.bottom = tk.Frame()
        w = self.bottom
        w.pack(fill=tk.BOTH, expand=1)
        self.vsb = tk.Scrollbar(w, orient=tk.VERTICAL)
        self.vsb.pack(fill=tk.Y, side=tk.RIGHT)

        # ----------- zone de texte
        self.textDNA = tk.Text(w, width=60, height=10)
        self.textDNA['yscrollcommand'] = self.vsb.set
        self.textDNA.config(state=tk.DISABLED)

        self.vsb.config(command=self.textDNA.yview)

        # http://effbot.org/tkinterbook/grid.htm
        self.textDNA.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def translateDNA(self):
        print("translateDNA")

        if self.source != None:
            brin = self.source.getDNA()
            print("translateDNA brin:", brin)
            protein = dnatl.gen_protein(
                brin, self.varOneOr3Letter.get(), self.varPhase.get())

            self.textDNA.config(state=tk.NORMAL)
            self.textDNA.delete("0.0", tk.END)
            self.textDNA.insert(tk.END, "".join(protein))
            self.textDNA.config(state=tk.DISABLED)
            # self.event_generate("<<UpdateProt>>")

    def onUpdateProtEvent(self, event):
        print("onUpdateProtEvent")
        self.source = event.widget
        self.translateDNA()

        print("self.varOneOr3Letter :", self.varOneOr3Letter.get())

    def getDNA(self):
        brin = self.textDNA.get(1.0, tk.END)
        brin = brin.strip(" \n")
        return brin


if __name__ == '__main__':
    import dnagen as dna

    class Appli(tk.Tk):
        def __init__(self):
            tk.Tk.__init__(self)

        def getDNA(self):
            brin = dna.genereDNA(50)
            brin = "".join(brin)
            print("brin de root:<", brin, ">", sep="")
            return brin

    def sendUpdateDnaEvent():
        print("update DNA event")
        root.event_generate("<<UpdateDNA>>")
        root.after(5000, sendUpdateDnaEvent)

    def onUpdateProtEvent(event):
        brin = event.widget.getDNA()
        print("UpdateProtEvent:<", brin, ">", sep="")

    print("in main")
    root = Appli()
    w = WDnaTranslator(root)
    w.pack()
    w.bind_all("<<UpdateDNA>>", w.onUpdateProtEvent)
    root.bind_all("<<UpdateProt>>", onUpdateProtEvent)
    print("In loop")
    root.after(5000, sendUpdateDnaEvent)

    root.mainloop()
