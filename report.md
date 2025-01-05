
      # Rapport Final - Carnet de Voyage

      ## Ressenti Général sur le Projet

      Le projet "Carnet de Voyage" a été une expérience enrichissante et stimulante. Il a permis de mettre en pratique plusieurs concepts clés du développement web avec Django, allant de la création de modèles de données à la gestion de l'authentification et à l'amélioration de l'interface utilisateur. Le projet a permis de comprendre l'importance d'une bonne organisation du code, de la gestion des migrations, et de la création de tests pour assurer la qualité de l'application.

      ## Tâches Principales Réalisées

      1.  **Mise en place du projet Django :**
          -   Création du projet Django "carnet_voyage" avec deux applications : "users" et "voyages".
          -   Configuration des répertoires standards (migrations, templates, static).

      2.  **Création des modèles de données :**
          -   Définition des modèles "Destination", "Lieu", "Avis", et "Favori" dans l'application "voyages".
          -   Implémentation des relations entre les modèles (OneToMany, ManyToMany).
          -   Configuration des modèles pour la migration.

      3.  **Interface d'administration Django :**
          -   Enregistrement des modèles dans `admin.py`.
          -   Personnalisation de l'affichage des champs dans l'admin (list_display, search_fields).
          -   Création d'un superutilisateur pour tester l'accès à l'admin.

      4.  **Création des vues de base :**
          -   Implémentation des vues pour la liste des destinations et le détail d'une destination.
          -   Création des templates correspondants.
          -   Configuration des vues avec `path()` dans `urls.py`.

      5.  **Système de favoris :**
          -   Implémentation de la fonctionnalité pour ajouter/retirer une destination des favoris d'un utilisateur.
          -   Création de la vue `ajouter_favori`.
          -   Ajout d'un bouton dans le template de détail de destination.

      6.  **Tests unitaires :**
          -   Création de tests pour vérifier le bon fonctionnement des modèles "Destination" et "Lieu".
          -   Tests pour l'ajout/retrait de favoris.
          -   Tests pour l'appel d'une API externe (avec un mock).

      7.  **Authentification simplifiée :**
          -   Ajout d'un champ `isLoggedIn` au modèle `User` dans l'application "users".
          -   Possibilité d'activer la connexion via l'interface admin.
          -   Restriction de l'accès à certaines pages (favoris, ajout d'avis) aux utilisateurs connectés.

      8.  **Stylisation avec Bootstrap :**
          -   Intégration de Bootstrap dans les templates.
          -   Amélioration de l'esthétique des pages (barre de navigation, cartes, boutons, messages d'alerte).

      9.  **Déploiement et documentation :**
          -   Création d'un fichier `README.md` avec la présentation du projet, les instructions d'installation et de lancement, et les technologies utilisées.
          -   Préparation du dépôt Git (vérification de la clarté du code, commit de tous les fichiers nécessaires).

      ## Problèmes Rencontrés et Solutions Appliquées

      1.  **Problème de chemin d'accès à `manage.py` :**
          -   **Problème :** Les commandes `python manage.py` échouaient car le chemin d'accès était incorrect.
          -   **Solution :** Correction du chemin d'accès en exécutant les commandes directement depuis le répertoire `carnet_voyage`.

      2.  **Erreurs de migration :**
          -   **Problème :** Des erreurs lors de l'application des migrations.
          -   **Solution :** Vérification des modèles et des relations, puis application des migrations avec `python manage.py makemigrations` et `python manage.py migrate`.

      3.  **Gestion de l'authentification :**
          -   **Problème :** Implémentation d'une authentification simplifiée avec un champ `isLoggedIn`.
          -   **Solution :** Création d'un modèle `User` personnalisé étendant le modèle `AbstractUser` de Django, et ajout du champ `isLoggedIn`.

      4.  **Tests unitaires :**
          -   **Problème :** Difficulté à tester l'appel d'une API externe.
          -   **Solution :** Utilisation de `unittest.mock` pour simuler la réponse de l'API.

      ## Conclusion

      Le projet "Carnet de Voyage" a permis de consolider mes compétences en développement web avec Django. Les défis rencontrés ont été l'occasion d'apprendre et de mettre en pratique des solutions concrètes. Le résultat est une application fonctionnelle et bien structurée, prête à être déployée.
    </file>
