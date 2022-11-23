
def enter_poly(degre):
    list_coeff = []
    for coeff in range(0, degre+1):
        list_coeff.append(int(input("Entrer le coefficient du degré " + str(coeff) + " : ")))
    return list_coeff


def calc_f_a(list_coeff, degre, a):
    f_a = list_coeff[degre]*a+list_coeff[degre-1]
    for i in range(degre-2, -1, -1):
        f_a = f_a*a+list_coeff[i]
    return f_a


def search_a(list_coeff, degre):
    search_intervalle = True
    a = 1
    intervalle = [a, a]
    while search_intervalle:
        f_a = calc_f_a(list_coeff, degre, a)
        f_a_neg = calc_f_a(list_coeff, degre, -a)
        prod_f_a = f_a * f_a_neg
        if prod_f_a < 0:
            search_intervalle = False
            intervalle = [-a, a]
        elif prod_f_a == 0:
            search_intervalle = False
            if f_a == 0:
                intervalle = [a, a]
            else:
                intervalle = [-a, -a]
        else:
            a += 1
    return intervalle


def dichotomie(list_coeff, degre, intervalle):
    distance = abs(intervalle[1]-intervalle[0])
    new_intervalle = [intervalle[0], intervalle[1]-distance/2]
    f_a = calc_f_a(list_coeff, degre, new_intervalle[1])
    f_a_neg = calc_f_a(list_coeff, degre, new_intervalle[0])
    prod_f_a = f_a*f_a_neg
    if prod_f_a<0:
        return new_intervalle
    elif prod_f_a == 0:
        if f_a == 0:
            return [new_intervalle[1], new_intervalle[1]]
        else:
            return [new_intervalle[0], new_intervalle[0]]
    else:
        new_intervalle = [intervalle[0]+distance/2, intervalle[1]]
        return new_intervalle


def boucle_dichotomie(list_coeff, degree, intervalle):
    continue_boucle = True
    if intervalle[0] == intervalle[1]:
        continue_boucle = False
        print("Le zéro se trouve exactement en x=", intervalle[0])
    else:
        new_intervalle = dichotomie(list_coeff, degree, intervalle)
    while continue_boucle:
        delta = abs(new_intervalle[1]-new_intervalle[0])
        if delta == 0:
            continue_boucle = False
            print("Le zéro se trouve exactement en x=", new_intervalle[0])
        elif delta<=0.001:
            continue_boucle = False
            print("Le zéro se trouve dans l'intervalle : ", new_intervalle)
        else:
            new_intervalle = dichotomie(list_coeff, degree, new_intervalle)




def degre():
    degre = -1
    while degre<0 or degre%2 == 0:
        degre = int(input("Entrez un degré pour le polynôme. \nRAPPEL : le degré est un entier positif et impair\nEcrire ici : "))
    return degre


degre = degre()
list_coeff = enter_poly(degre)
intervalle = search_a(list_coeff, degre)
boucle_dichotomie(list_coeff, degre, intervalle)
