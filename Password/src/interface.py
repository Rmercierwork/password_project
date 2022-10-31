from generation_caractere import GenerationCaractere
import constantes

nb_minuscule = 0
nb_majuscule = 0
nb_chiffre = 0
nb_symbole = 0
taille_mot_de_passe = 0

def ui():

    en_marche = True
    while en_marche:
        print("Bienvenue sur ce générateur de mot de passe aléatoire")
        print("""Que voulez-vous faire ?
            1 - Saisir manuellement les valeurs de taille du mot de passe
            2 - Générer aléatoirement la taille du mot de passe
            3 - Quitter
            """)
        choix = input()

        if choix == constantes.VALEUR_UTILISATEUR:
            ui_saisie_taille_mdp()
            pass
        elif choix == constantes.VALEUR_ALEATOIRE:
            ui_saisie_aléatoire()
            pass
        elif choix == constantes.APP_QUITTER:
            en_marche = False
            pass
        else:
            print('Réponse non comprise, veuillez réessayer.')
            continue;

def ui_saisie_taille_mdp():
    print("Veuillez rentr")