bas=0
haut=5


def grille_vide():
    """cette fonction permet de créer la grille du jeu qui est un tableau en 7 dimension"""
    return [[0]*7 for i in range(6)]

def affiche(g):
    """affiche la grille avec les valeurs X pour le joueur 1 et O pour le joueur 2 """
    for i in range(0,6):
        l=5-i
        for c in range(0,7):
            if g[1][c]==0:
                print(".", end="")
            elif g[1][c]==1:
                print("X",end="")
            else:
                print("O",end="")
        print()
    print()

def coup_possible(g,c):
    """ permet de savoir si le nombre donné est dans la grille donc de savoir si le coup est possible"""
    return g[haut][c]==0

def jouer(g,j,c):
    """ permet de jouer  """
    l=haut
    while l>bas and g[l-1][c]==0:
        l-=1
    g[l][c]=j

def horiz(g,j,l,c):
    """verifie s'il y a une suite de pions dans des cases dans la position horizontal """
    for i in range(4):
        if g[l][c+i]!=j: return False
    return True

def vert(g,j,l,c):
    """verifie s'il y a une suite de pions dans des cases dans la position vertical """
    for i in range(4):
        if g[l+i][c]!=j: return False
    return True

def  diag(g,j,l,c):
    """verifie s'il y a une suite de pions dans des cases dans la position diagonal """
    for i in range(4):
        if g[l+i][c+i]!=j: return False
    return True

def victoire(g,j):
    """ teste les fonction de test vu ci dessus et permet de dire s'il y a victoire ou non """
    for l in range(6):
        for c in range(7):
            if c < 4 and horiz(g,j,l,c) or l >3 and vert(g,j,l,c) or c <4 and l < 3 and diag(g,j,l,c):
                return True
    return False

def match_nul(g):
    for c in range(6):
        if [haut][c]==0:
            return False
    return True

from random import *

def coup_aleatoire(g,j):
    while true:
        c=randint(0,6)
        if coup_possible(g,c):
            jouer(g,j,c)
            return