# TechnoWeb Project

Bienvenue dans le projet de **TechnoWeb** ! Ce projet est une API construite avec [FastAPI](https://fastapi.tiangolo.com/).

## Table des matières

- [Installation](#installation)
- [Démarrage](#démarrage)
- [Utilisation](#utilisation)

## Installation

1. **Installer Python et Git**

   - **Windows :** Téléchargez et installez [Python](https://www.python.org/downloads/) et [Git](https://git-scm.com/downloads).
   - **Linux (Debian/Ubuntu) :**
     ```bash
     sudo apt update && sudo apt install python3 python3-pip git
     ```
   - **macOS :**
     ```bash
     brew install python git
     ```

2. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/Wendri23/TechnoWeb_project.git
   cd TechnoWeb_project
   ```

3. **Installer les dépendances :**

   ```bash
   pip install "fastapi[standard]"   
   ```

## Démarrage

**Pour lancer l'API en mode développement :**

  ```bash
  fastapi dev main.py
  ```

L'API sera accessible par défaut à l'adresse [http://127.0.0.1:8000](http://127.0.0.1:8000).

