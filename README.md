# TP Python — MVC + Tkinter

Ce projet contient plusieurs **TP de Python** organisés avec le modèle **MVC** et une interface graphique simple avec **Tkinter**.  
Chaque TP est rangé dans son dossier (`TP1.1`, `TP1.2`, …) et un **lanceur** (`launcher.py`) permet de choisir lequel exécuter facilement.

---

## Organisation du projet

Chaque TP suit la même structure :

```
TPx.x/
 ├── Controller/
 │    └── controller.py     # La logique et les calculs
 ├── View/
 │    └── menu.py           # L’interface Tkinter
 ├── Model/
 │    └── fichier.py        # Fait le lien entre Model et View
 ├── main.py                # Point d’entrée du TP
 └── README.md              # Explications propres au TP
```

---

## Le lanceur

Le fichier **`launcher.py`** affiche un petit menu pour choisir quel TP ouvrir.  
Chaque TP s’ouvre ensuite dans **sa propre fenêtre**.

👉 Lancer le menu principal :

```bash
python launcher.py
```

---

## Les TP

- **TP1.1 – Convertisseur Celsius/Fahrenheit**  
  Saisir une température et la convertir d’une unité à l’autre.

- **TP1.2 – Somme et produit des nombres pairs**  
  Entrer un entier `N` et calculer la somme et le produit des nombres pairs jusqu’à `N`.

- **TP1.3 – Messages d’accueil personnalisés**  
  Générer des phrases de bienvenue pour une liste de prénoms.

- **TP1.4 – Jeu de calcul mental**  
  S’entraîner avec des additions, soustractions, multiplications ou divisions.

- **TP1.5 – Année bissextile**  
  Vérifier si une année est bissextile ou non.


## Objectifs pédagogiques

- Comprendre le modèle **MVC** (Model – View – Controller)  
- Apprendre à séparer la logique du code de l’interface graphique  
- Manipuler **Tkinter** pour créer des fenêtres  
- S’entraîner sur des exercices classiques de programmation Python  

