from poset import Poset
from fmc-poset import all_fmc

def all_fcontinuas(poset1, poset2):
    crecientes = all_fmc(poset1, poset2)
    dirigidos = poset1.allDirigidos()
    continuas = []
    for f in crecientes:
        isContinua = True
        for M in dirigidos:
            supM = min(poset1.cotaSuperior(M))
            imgM = {b for (a,b) in f if a in M}
            supImgM = min(poset2.cotaSuperior(fM))
            if supM != supImgM:
                isContinua = False
                break
        if isContinua:
            continuas.append(f)
    return continuas

