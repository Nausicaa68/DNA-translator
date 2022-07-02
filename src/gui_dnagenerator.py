import tkinter as tk
import dnagen as dna


class WDnaGenerator(tk.Frame):
    def __init__(self, racine=None):
        "Le constructeur du générateur de séquence d'ADN"
        tk.Frame.__init__(self, racine)
        self.racine = racine
        self.brin = None
        self.createWidget()

    def createWidget(self):
        "La création des éléments graphiques"
        self.genBut = tk.Button(self, text="Génère", command=self.genereCmd)
        self.genBut.grid(row=0, column=0, rowspan=2)

        self.textLbl = tk.Label(self, text="Longueur de la chaine :")
        self.textLbl.grid(row=0, column=1, rowspan=2)

        self.cmdValider = (self.racine.register(self.validerCmd), '%S')
        self.cmdErreur = (self.racine.register(self.erreurCmd), '%S')
        self.dnaLenStr = tk.StringVar()
        self.dnaLenStr.set("50")

        self.chiffreEnt = tk.Entry(self, width=10, justify=tk.RIGHT)
        self.chiffreEnt['textvariable'] = self.dnaLenStr
        self.chiffreEnt['validate'] = "key",
        self.chiffreEnt['invcmd'] = self.cmdErreur
        self.chiffreEnt['vcmd'] = self.cmdValider

        self.chiffreEnt.grid(row=0, column=2, rowspan=2)

    def genereCmd(self):
        self.dnaLen = int(self.dnaLenStr.get())
        print("dna length:", self.dnaLen)
        self.brin = dna.genereDNA(self.dnaLen)
        print("DNAgenerator:generate event <<NewDNA>>")
        self.event_generate("<<NewDNA>>")

    def getDNA(self):
        return self.brin

    def validerCmd(self, s):
        print(s)
        print("dans validerCmd")
        return s.isdigit()

    def erreurCmd(self, s):
        self.t = tk.Toplevel(self.racine)
        tk.Label(self.t, text="Error: Invalid input %s" %
                 s).pack(padx=5, pady=5)
        tk.Button(self.t, text="Ok", command=self.t.destroy).pack(
            padx=5, pady=5)


# ========================================code de test
if __name__ == '__main__':
    def onNewDNA(event):
        # print(type(event))
        # print(dir(event))
        # print(event.__dict__)
        print(event.widget.getDNA())

    print("in main")
    root = tk.Tk()
    wgen = WDnaGenerator(root)
    wgen.pack()
    wgen.bind("<<NewDNA>>", onNewDNA)
    root.mainloop()
