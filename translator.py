from random import randint


def gen_protein(stringAdn, mode, phase):
    stringProtein = ""
    codon = ""
    for i in range(phase, len(stringAdn)):
        if stringAdn[i] == "T":
            codon += "U"
        else:
            codon += stringAdn[i]

        if len(codon) == 3:
            stringProtein += get_code_genetique(codon, mode)
            stringProtein += " "
            codon = ""

    return stringProtein


def get_code_genetique(codon, mode):

    dico_codeGenetique = {
        'AUA': ('Ile', 'I'), 'AUC': ('Ile', 'I'), 'AUU': ('Ile', 'I'), 'AUG': ('Met', 'M'),
        'ACA': ('Thr', 'T'), 'ACC': ('Thr', 'T'), 'ACG': ('Thr', 'T'), 'ACU': ('Thr', 'T'),
        'AAC': ('Asn', 'N'), 'AAU': ('Asn', 'N'), 'AAA': ('Lys', 'K'), 'AAG': ('Lys', 'K'),
        'AGC': ('Ser', 'S'), 'AGU': ('Ser', 'S'), 'AGA': ('Arg', 'R'), 'AGG': ('Arg', 'R'),
        'CUA': ('Leu', 'L'), 'CUC': ('Leu', 'L'), 'CUG': ('Leu', 'L'), 'CUU': ('Leu', 'L'),
        'CCA': ('Pro', 'P'), 'CCC': ('Pro', 'P'), 'CCG': ('Pro', 'P'), 'CCU': ('Pro', 'P'),
        'CAC': ('His', 'H'), 'CAU': ('His', 'H'), 'CAA': ('Gln', 'Q'), 'CAG': ('Gln', 'Q'),
        'CGA': ('Arg', 'R'), 'CGC': ('Arg', 'R'), 'CGG': ('Arg', 'R'), 'CGU': ('Arg', 'R'),
        'GUA': ('Val', 'V'), 'GUC': ('Val', 'V'), 'GUG': ('Val', 'V'), 'GUU': ('Val', 'V'),
        'GCA': ('Ala', 'A'), 'GCC': ('Ala', 'A'), 'GCG': ('Ala', 'A'), 'GCU': ('Ala', 'A'),
        'GAC': ('Asp', 'D'), 'GAU': ('Asp', 'D'), 'GAA': ('Glu', 'E'), 'GAG': ('Glu', 'E'),
        'GGA': ('Gly', 'G'), 'GGC': ('Gly', 'G'), 'GGG': ('Gly', 'G'), 'GGU': ('Gly', 'G'),
        'UCA': ('Ser', 'S'), 'UCC': ('Ser', 'S'), 'UCG': ('Ser', 'S'), 'UCU': ('Ser', 'S'),
        'UUC': ('Phe', 'F'), 'UUU': ('Phe', 'F'), 'UUA': ('Leu', 'L'), 'UUG': ('Leu', 'L'),
        'UAC': ('Tyr', 'Y'), 'UAU': ('Tyr', 'Y'), 'UAA': ('Stop', '_'), 'UAG': ('Stop', '_'),
        'UGC': ('Cys', 'C'), 'UGU': ('Cys', 'C'), 'UGA': ('Stop', '_'), 'UGG': ('Trp', 'W'),
    }

    return dico_codeGenetique[codon][mode]


if __name__ == '__main__':
    adnTest = "ACTGCTTTCGGCGATATTGGCGGCTATA"
    print("ADN :", adnTest)
    print("Chaine prot :", gen_protein(adnTest, 3))
