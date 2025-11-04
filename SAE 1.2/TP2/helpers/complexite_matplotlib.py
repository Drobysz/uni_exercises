#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Initiation au développement: fichier de base pour le TP sur la 
complexité."""

import matplotlib.pyplot as plt

def tracer(nom_fichier, *listes_et_titres):
    """Trace un graphique avec les données fournies en ordonnées, et sauve le
    résultat au format png dans nom_fichier.png. listes_et_titres est une liste
    d'arguments au format suivant:

        liste_1, titre_1, liste_2, titre_2, ...

    Les listes ne doivent pas toutes avoir la même longueur.
    """
    # vérification du format: l'argument listes_et_titres doit être de longueur
    # paire, et on doit alterner listes et chaînes dans cet ordre
    assert(not len(listes_et_titres) % 2), \
           "la liste d'arguments n'est pas de longueur paire"
    assert(all(type(elem) is list for elem in listes_et_titres[::2])), \
           "les arguments en positions paires doivent être des listes"
    assert(all(type(elem) is str for elem in listes_et_titres[1::2])), \
           "les arguments en positions impaires doivent être des chaînes"

    # construction des légendes
    legend = list()
    for num in range(0, len(listes_et_titres), 2):
        legend.append(
            plt.plot(listes_et_titres[num], label=listes_et_titres[num+1])[0]
        )

    plt.title(nom_fichier)
    plt.legend(handles=legend)  # si erreur avec handles: supprimer "handles="
    plt.xlabel("Taille des données")
    plt.ylabel("Temps d'exécution (secondes)")
    plt.savefig("imgs/" + nom_fichier + ".png")
    #plt.show()  # afficher le résultat à l'écran
    plt.clf()  # effacer le graphique stocké en mémoire
