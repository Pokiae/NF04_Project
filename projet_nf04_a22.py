"""
Calcul d'une racine d'un polynôme (version 1)
Auteur : Pokiae
Date : A22
Programme de calcul d'un racine d'un polynôme de degré impair saisi par l'utilisateur
par dichotomie
Entrée : le degré et les coefficients du polynôme, la taille de l'intervalle souhaitée 
(précision demandée)
Résultat : affiche un intervalle qui contient une racine du polynôme, selon la précision demandée
"""


def enter_poly(nb_coeff:int):
    """
    Stocke les coefficients du polynôme saisis par l'utilisateur
    Entrée : le nombre de coefficients (moins un) à demander
    Résultat : une liste contenant tous les coefficients du polynômes, classé par degré croissant
    """
    coeff_entrees = []
    for coeff in range(0, nb_coeff+1):
        coeff_entrees.append(float(input("Entrer le coefficient du degré " + str(coeff) + " : ")))
    return coeff_entrees


def calc_f_a(coeffs:float, degre_poly:int, nb_a:float):
    """
    Calcule le polynôme au point a
    Entrée : la liste des coefficients (réels), le degré du polynôme (entier) et la valeur de a (réel)
    Résultat : la valeur du polynôme en a (un réel)
    """
    f_a = coeffs[degre_poly]*nb_a+coeffs[degre_poly-1]
    for i in range(degre_poly-2, -1, -1):
        f_a = f_a*nb_a+coeffs[i]
    return f_a


def search_a(coeffs:float, degre_poly:int):
    """
    Recherche une intervalle [a;-a] dans laquelle une racine du polynôme
    est contenue
    Entrée : liste des coefficients (réels), degré du polynôme (entier)
    Résultat : liste qui contient [a;-a] (réels), soit une intervalle
    """
    search_intervalle = True
    nb_a = 1
    defined_intervalle = [nb_a, nb_a]
    while search_intervalle:
        f_a = calc_f_a(coeffs, degre_poly, nb_a)
        f_a_neg = calc_f_a(coeffs, degre_poly, -nb_a)
        prod_f_a = f_a * f_a_neg
        if prod_f_a < 0:
            search_intervalle = False
            defined_intervalle = [-nb_a, nb_a]
        elif prod_f_a == 0:
            search_intervalle = False
            if f_a == 0:
                defined_intervalle = [nb_a, nb_a]
            else:
                defined_intervalle = [-nb_a, -nb_a]
        else:
            nb_a += 1
    return defined_intervalle


def dichotomie(coeffs:float, degre_poly:int, initial_intervalle:float):
    """
    Applique le principe de dichotomie pour obtenir une plus petite
    intervalle contenant la racine du polynôme
    Donnée : liste des coefficients du polynôme (réels), degré du polynôme (entier), liste
    des bornes de l'intervalle dans laquelle se trouve la racine et qu'on veut réduire (deux réel)
    Résultat : liste des bornes de la nouvelle intervalle contenant la racine (deux réels)
    """
    distance = abs(initial_intervalle[1]-initial_intervalle[0])
    new_intervalle = [initial_intervalle[0], initial_intervalle[1]-distance/2]
    f_a = calc_f_a(coeffs, degre_poly, new_intervalle[1])
    f_a_neg = calc_f_a(coeffs, degre_poly, new_intervalle[0])
    prod_f_a = f_a*f_a_neg
    if prod_f_a<0:
        return new_intervalle
    elif prod_f_a == 0:
        if f_a == 0:
            return [new_intervalle[1], new_intervalle[1]]
        else:
            return [new_intervalle[0], new_intervalle[0]]
    else:
        new_intervalle = [initial_intervalle[0]+distance/2, initial_intervalle[1]]
        return new_intervalle


def boucle_dichotomie(coeffs:float, degre_poly:int, initial_intervalle:float, precision:float):
    """
    Boucle qui effectue la dichotomie jusqu'à obtenir une intervalle aussi précise que demandée
    Donnée : liste des coefficients (réels), degré du polynôme (entier), liste des bornes du
    l'intervalle où se trouve la racine (réels), la précision demandée (réel)
    Résultat : affichage d'une intervalle correspondant à la précision demandée pour la racine
    """
    continue_boucle = True
    if initial_intervalle[0] == initial_intervalle[1]:
        continue_boucle = False
        print("Le zéro se trouve exactement en x=", initial_intervalle[0])
    else:
        new_intervalle = dichotomie(coeffs, degre_poly, initial_intervalle)
    while continue_boucle:
        delta = abs(new_intervalle[1]-new_intervalle[0])
        if delta == 0:
            continue_boucle = False
            print("Le zéro se trouve exactement en x=", new_intervalle[0])
        elif delta<=precision:
            continue_boucle = False
            print("Le zéro se trouve dans l'intervalle : ", new_intervalle)
        else:
            new_intervalle = dichotomie(coeffs, degre_poly, new_intervalle)


def get_degre():
    """
    Récupère le degré du polynôme entré par l'utilisateur
    Donnée : vide
    Résultat : degré du polynôme (entier)
    """
    entered_degre = -1
    while entered_degre<0 or entered_degre%2 == 0:
        entered_degre = int(input("""Entrez un degré pour le polynôme.
        \nRAPPEL : le degré est un entier positif et impair\nEcrire ici : """))
    return degre


degre = get_degre()
list_coeff = enter_poly(degre)
intervalle = search_a(list_coeff, degre)
boucle_dichotomie(list_coeff, degre, intervalle,
    float(input("Entrez la précision demandée pour la racine : ")))
    