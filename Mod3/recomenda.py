from db import avaliacoes
from math import sqrt

def euclidiana(usuario1, usuario2):
    si={}
    for item in avaliacoes[usuario1]:
        if item in avaliacoes[usuario2]: si[item] = 1
    
    if len(si) == 0: return 0

    soma = sum([pow(avaliacoes[usuario1][item] - avaliacoes[usuario2][item],2) for item in avaliacoes[usuario1] if item in avaliacoes[usuario2]])
    return 1 / (1  + sqrt(soma))


def getSimilares(usuario):
    similaridade = [(euclidiana(usuario,outro),outro) for outro in avaliacoes if outro != usuario]
    similaridade.sort()
    similaridade.reverse()
    return similaridade

print(getSimilares('Ana'))