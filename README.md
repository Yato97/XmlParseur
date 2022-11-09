# XmlParser
<a href="#license"><img src="https://img.shields.io/badge/License-MIT-green" alt="License"></a>

## Install dependencies

```bash
pip install colorama
```

## Usage

```bash
py ./Xmpparser.py
```

Lancer le script dans une console récente type powershell, vscode pour permettre l'affichage des couleurs

Entrer le numéro correspondant a la fonction voulue.

## Menu

1) **Ajouter header XML recursif** : Ajoute les header XML manquants récursivement dans un répertoire passer en paramètre, (explore tous les sous répertoire)

2) **Rechercher un fichier du workspace** : Recherche un fichier a l'image de l'explorateur windows (un peu plus rapide)

3) **Parseur XML** : Parse un fichier XML et retourne l'arborescence de celui-ci, permet de, voire les nœud et leurs attributs, utile quand on cherche une valeur manquante ou pour apprendre les métas-models Logicells      

4) **Analyseur XML** : Vérifie un fichier XML, s'il manque le header xml ou si il y a une erreur dans le fichier, exemple balise manquante, mal fermé etc

5) Analyseur XML Récursif : Vérifie récursivement les fichiers XML, s'il manque le header xml ou s'il y a une erreur dans le fichier, exemple balise manquante, mal fermé, encodage, etc, les chemins des fichiers sont retournés avec les erreurs correspondantes

6) **Analyseur XML Récursif** : Vérifie récursivement les fichiers XML, s'il manque le header xml ou s'il y a une erreur dans le fichier, exemple balise manquante, mal fermé etc, les chemins des fichiers sont retournés et les erreurs correspondantes

## License
Released under <a href="/LICENSE">MIT</a> by <a href="https://github.com/Yato97">@Yato97</a>.