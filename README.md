# PYCODEC 📦

**Lossless Text Compression CLI (LZ77 + Huffman)**

PYCODEC est une application **CLI (Command Line Interface)** de compression de données texte **sans perte**, développée en **Python**.  
Elle est conçue pour traiter **uniquement des fichiers texte volumineux (≥ 100 Mo)** et repose sur une **combinaison d’algorithmes classiques de compression sans perte**.

## 🎯 Objectif du projet

L’objectif principal est de :

- Concevoir un **programme de compression sans perte**
- Gérer efficacement des **fichiers texte de grande taille**
- Implémenter des **algorithmes étudiés en cours**
- Fournir une **interface CLI élégante et professionnelle**
- Garantir une **décompression bit-à-bit identique** au fichier original

## 🧠 Algorithmes utilisés

Le projet utilise la combinaison suivante :

| Algorithme         | Rôle                                    |
| ------------------ | --------------------------------------- |
| **LZ77**           | Suppression des redondances locales     |
| **Huffman Coding** | Compression entropique (codage optimal) |

👉 Cette combinaison permet un bon compromis entre **taux de compression**, **simplicité** et **fiabilité**.

## ✨ Fonctionnalités

✔ Compression sans perte  
✔ Décompression correcte et fiable  
✔ Vérification automatique de la taille minimale (≥ 100 Mo)  
✔ Interface CLI avec :

- Banner ASCII stylé (pyfiglet)
- Barre de progression en pourcentage
  ✔ Statistiques détaillées après compression  
  ✔ Vérification d’intégrité après décompression

## ⚙️ Installation

### 1️⃣ Cloner le projet

```bash
git clone git@github.com:ranto-dev/pycodec.git
cd pycodec
```

### 2️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

## ▶️ Utilisation

### 🔹 Afficher l’aide

```bash
python main.py --help
```

### 🔹 Compression

```bash
python main.py compress fichier.txt fichier.rnt
```

📌 Conditions :

- Le fichier **doit être un fichier texte**
- Taille minimale : **≥ 100 Mo**
- Sinon → erreur explicite affichée

### 🔹 Décompression

```bash
python main.py decompress fichier.rnt fichier.txt
```

## 📊 Statistiques affichées après compression

À la fin de la compression, le programme affiche :

- 📏 Taille du fichier initial
- 📦 Taille du fichier compressé
- 📉 Taux de compression (%)
- ✅ Confirmation de réussite

Exemple :

```
Compression terminée ✔
Taille initiale      : 152.34 MB
Taille compressée   : 61.82 MB
Taux de compression : 59.42 %
```

## 🔍 Vérification d’intégrité

Après décompression :

- Le fichier reconstruit est **strictement identique** à l’original
- Vérification possible via hash (SHA-256)

## 🧪 Tests expérimentaux

Les tests doivent être réalisés sur :

- ✔ Au moins **un fichier texte ≥ 100 Mo**
- Comparaison avant / après compression
- Vérification après décompression

## 🚫 Limitations

- ❌ Ne traite pas les fichiers < 100 Mo
- ❌ Optimisé uniquement pour le **texte**
- ❌ Pas conçu pour les images ou vidéos

## 🎓 Contexte académique

Ce projet est réalisé dans un cadre **pédagogique**, visant à :

- Comprendre les mécanismes de compression
- Implémenter des algorithmes fondamentaux
- Analyser les performances expérimentales

## 👤 Auteur

- **Nom** : Aina Iarindranto
- **Pseudo** : rantodev
- **Projet académique – Compression de données**
