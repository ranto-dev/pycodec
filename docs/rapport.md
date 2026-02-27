# RAPPORT SUR LE PROJET PYCODEC

## I. Description

**PYCODEC** est une application **CLI (Command Line Interface)** développée en **Python**, permettant la **compression et la décompression sans perte** de fichiers texte.

L’objectif du projet est d’implémenter et d’étudier des **algorithmes fondamentaux de compression de données**, tout en garantissant :

- Une reconstruction **bit-à-bit identique** du fichier original
- Une gestion correcte des fichiers volumineux
- Une interface terminal élégante avec affichage des statistiques

Le programme fonctionne exclusivement sur des **fichiers texte**, et assure une décompression parfaitement fidèle grâce à la gestion explicite de la taille originale des données.

## II. Algorithmes utilisés

Le système repose sur la combinaison de deux algorithmes classiques :

### 1. LZ77 (Lempel-Ziv 1977)

LZ77 est un algorithme de compression basé sur la détection de répétitions dans une fenêtre glissante.

Il remplace les séquences répétées par des triplets :

(offset, longueur, caractère_suivant)

Son rôle dans PYCODEC est :

- Supprimer les redondances locales
- Réduire les répétitions fréquentes dans le texte

### 2. Codage de Huffman

Le codage de Huffman est un algorithme de compression entropique basé sur :

- La fréquence d’apparition des symboles
- La construction d’un arbre binaire optimal

Son rôle dans PYCODEC est :

- Encoder efficacement les données produites par LZ77
- Réduire davantage la taille en utilisant des codes binaires variables

### 3. Pourquoi combiner LZ77 + Huffman ?

La combinaison permet :

- LZ77 → suppression des répétitions
- Huffman → compression statistique des symboles restants

Cette approche est similaire aux principes utilisés dans des formats réels comme ZIP ou DEFLATE.

## III. Architecture du système

Le pipeline de compression suit les étapes suivantes :

### 1. Compression

Fichier texte original
→ Compression LZ77
→ Sérialisation des données
→ Compression Huffman
→ Écriture du fichier compressé avec en-tête

Le fichier compressé contient :

- La taille exacte du fichier original
- Les données encodées
- La structure de l’arbre de Huffman

### 2. Décompression

Fichier compressé
→ Lecture de la taille originale
→ Décompression Huffman
→ Reconstruction des données LZ77
→ Décompression LZ77
→ Troncature à la taille exacte originale
→ Fichier restauré

Cette étape de troncature permet d’éliminer les bits de padding ajoutés lors de l’alignement binaire.

## IV. Résultats expérimentaux

Des tests ont été effectués sur plusieurs fichiers texte.

Exemple :

Taille initiale : 70.07 KB
Taille compressée : 10.05 KB
Taux de compression : 85.65 %

Après décompression :

- Vérification via SHA-256
- Les empreintes sont identiques
- Reconstruction parfaite du fichier

Formule utilisée pour le taux de compression :

Taux (%) = (1 - (taille_compressée / taille_initiale)) × 100

## V. Analyse et discussion

### 1. Performance

La combinaison LZ77 + Huffman offre :

- Un bon taux de compression sur les fichiers texte
- Une efficacité accrue lorsque le texte contient des répétitions fréquentes

Les performances dépendent fortement :

- De la taille de la fenêtre LZ77
- De la distribution statistique des caractères

### 2. Limites

- Le projet prend du temps pour compresser, c'est normale parceque le programme est programme en python qui peu lent compare aux autres languages de programmations comme le C ou encore C++
- Pour la compression, le programme est gourmande de ressource materielle (CPU, RAM) malgres nos effort a l'optimisation des algorithmes et des codes sources

### 3. Problèmes rencontrés

Durant les phases de test :

- Gestion des bits de padding dans Huffman
- Apparition d’un caractère NULL (`\x00`) à la fin du fichier
- Correction via stockage explicite de la taille originale

Ce correctif garantit une décompression parfaitement fidèle.

## VI. Conclusion

PYCODEC démontre l’efficacité de la combinaison LZ77 + Huffman pour la compression sans perte de fichiers texte.

Le projet met en évidence :

- Les principes fondamentaux de la compression
- L’importance de la gestion des flux binaires
- Les subtilités liées au padding et à la reconstruction exacte

Ce travail constitue une base solide pour des nuvelles perpectives innovante comme l’ajout d’optimisations avancées ou encore l’implémentation d’autres algorithmes (BWT, Arithmetic Coding) sans oublie l’amélioration des performances.
