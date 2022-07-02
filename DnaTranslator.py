import tkinter as tk
from gui_dnagenerator import *
from gui_dnamenu import *
from gui_dnapresenter import *
from gui_nucleotidecounter import *
from gui_dnaConRev import *
from gui_dnaTranslator import *

# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/extra-args.html


def test(event):
    print("==================TEST=================")


if __name__ == '__main__':
    print("in main")
    root = tk.Tk()
# le menu
    wmen = WDnaMenu(root)
    wmen.pack()

# le menu du haut
    ftop = tk.Frame()
    ftop.pack(side=tk.TOP, fill=tk.X)

    wgen = WDnaGenerator(ftop)
    wcnt = WNucleotideCounter(ftop)

    wgen.pack(side=tk.LEFT)
    wcnt.pack(side=tk.RIGHT)

    wpres = WDnaPresenter(root)
    wpres.pack(fill=tk.BOTH, expand=1)

    wcr = WDnaConRev(root)
    wcr.pack(fill=tk.BOTH, expand=1)

    wtranslator = WDnaTranslator(root)
    wtranslator.pack(fill=tk.BOTH, expand=1)

    root.bind_all("<<NewDNA>>", wpres.onNewDnaSequenceEvent)
    root.bind_all("<<UpdateDNA>>", wcnt.onUpdateDnaSequenceEvent)

    root.bind_all("<<UpdateDNA>>", wcr.onUpdateDnaSequenceEvent, add="+")
    root.bind_all("<<UpdateProt>>", wtranslator.onUpdateProtEvent)

    root.mainloop()
