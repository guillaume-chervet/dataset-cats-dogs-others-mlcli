import os
import json
from pathlib import Path

# Répertoire de base où se trouvent les fichiers JSON
BASE_PATH = Path(__file__).resolve().parent
base_directory = str(BASE_PATH) + "/mlcli_opencv"

# Mot à rechercher et à remplacer
mot_a_rechercher = "pillow"
mot_a_remplacer = "opencv"

def remplace_mot_dans_fichier(fichier):
    with open(fichier, 'r') as file:
        contenu = json.load(file)
    
    # Parcours du contenu pour rechercher et remplacer le mot
    def parcours_contenu(obj):
        if isinstance(obj, dict):
            for cle, valeur in obj.items():
                if isinstance(valeur, str):
                    obj[cle] = valeur.replace(mot_a_rechercher, mot_a_remplacer)
                else:
                    parcours_contenu(valeur)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                if isinstance(item, str):
                    obj[i] = item.replace(mot_a_rechercher, mot_a_remplacer)
                else:
                    parcours_contenu(item)
    
    parcours_contenu(contenu)
    
    # Écriture du contenu modifié dans le fichier
    with open(fichier, 'w') as file:
        json.dump(contenu, file, indent=4)

# Parcours du répertoire et traitement des fichiers JSON
for root, _, fichiers in os.walk(base_directory):
    for fichier in fichiers:
        if fichier.endswith('.json'):
            chemin_fichier = os.path.join(root, fichier)
            remplace_mot_dans_fichier(chemin_fichier)
            print(f'Mot "{mot_a_rechercher}" remplacé par "{mot_a_remplacer}" dans le fichier : {chemin_fichier}')
