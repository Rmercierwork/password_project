import random

class GenerationCaractere:
    """
        Classe de génération de caractère pour le mot de passe
    """

    def majuscul_aleatoire(self):
        """ Génération d'une lettre majuscule aléatoire """
        lettre_majuscule = chr(random.randint(65,90)) #Génère une lettre en majucule aléatoire (basé sur le code ASCII)
        return lettre_majuscule

    def minuscule_aleatoire(self):
        """ Génération d'une lettre minuscule aléatoire """
        lettre_minuscule = chr(random.randint(97,122)) #Génère une lettre en minuscule aléatoire (basé sur le code ASCII)
        return lettre_minuscule

    def chiffre_aleatoire(self):
        """ Génération d'un chiffre aléatoire """
        chiffre = chr(random.randint(48,57)) #Génère un chiffre aléatoire (basé sur le code ASCII)
        return chiffre

    def symbole__aleatoire(self):
        """ Génération d'un symbole aléatoire """
        list_symbole = list(range(33,47)) + list(range(58,65)) + list(range(91,97)) + list(range(123,127))  + [161,163,165,169,176,191]
        symbole = chr(random.choice(list_symbole)) #Génère un symbole aléatoire (basé sur le code ASCII)
        return symbole

