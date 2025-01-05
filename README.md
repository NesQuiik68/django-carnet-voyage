<file>
      # Carnet de Voyage

      ## Présentation du projet

      Carnet de Voyage est une application web Django permettant de gérer des destinations de voyage, des lieux associés, des avis, et des favoris. Les utilisateurs peuvent explorer différentes destinations, consulter les lieux d'intérêt, lire les avis, et ajouter des destinations à leur liste de favoris.

      ## Instructions d'installation et de lancement

      1. **Cloner le dépôt** (si applicable)
         ```bash
         git clone <repository_url>
         cd carnet_voyage
         ```

      2. **Créer un environnement virtuel**
         ```bash
         python3 -m venv venv
         source venv/bin/activate
         ```

      3. **Installer les dépendances**
         ```bash
         pip install -r requirements.txt
         ```
         (Note: You'll need to create a `requirements.txt` file with `pip freeze > requirements.txt` after installing dependencies)

      4. **Appliquer les migrations**
         ```bash
         python3 manage.py makemigrations
         python3 manage.py migrate
         ```

      5. **Créer un superutilisateur**
         ```bash
         python3 manage.py createsuperuser
         ```

      6. **Lancer le serveur de développement**
         ```bash
         python3 manage.py runserver
         ```

      7. **Accéder à l'application**
         Ouvrez votre navigateur et accédez à `http://127.0.0.1:8000/`.

      ## Technologies utilisées

      - **Python**
      - **Django**
      - **SQLite** (pour le développement)
      - **HTML**
      - **CSS**
      - **Bootstrap**
    </file>
