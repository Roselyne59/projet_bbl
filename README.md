Requirements: 
************
  avoir python3.10 installé 
  1 - git clone https://github.com/Q3DER/projet_bbl 
  2 - créer un environnement virutel: python3 -m venv venv_projet_bbl 
  3 - activer l'environnement virtuel: source ~ /venv_projet_bbl/bin/activate 
  4 - installer les requirements: cd requirements && pip install -r requirements.txt

Diagramme des classes:
**********************
  nom: diagramme_bbl_1.4.drawio
  
  Se rendre sur : https://app.diagrams.net/, et charger un fichier depuis perepherique, et indiquer l'emplacement du fichier.


Description:
************
Cette application a pour but de gérer une bibliothèque.
En tant qu'Administrateur, elle permet l'ajout, la consultation, la modification, et la suppression des utilisateurs, des livres, des etagères, des reservations et des emprunts des livres.
Elle inclue, également, des fonctionnalités de recherche, de calcul de jours de retard, et d'amendes. 

Page de connexion:
******************
Au lancement de l'application en executant la page main.py, une fenêtre de connexion s'affiche à l'écran.

  Profil administrateur:
  **********************
    Login : admin
    mot de passe : admin

  Profil membre (exemple de membre = "member"):
  *********************************************
    Login : member
    mot de passe : Member22/*
  
Ps: Il est conseillé de changer le mot de passe lors de la premiere connexion

*******************************************************************************

Page Espace administrateur:
***************************

Bouton Utilisateurs: sert à afficher la page "Gestion des utilisateurs"
*******************
  Gestion des utilisateurs: 
  *************************
  
    Fenêtre principale : Affiche la liste des utilisateurs.
    ******************
    Bouton Recherche par nom: sert à effectuer une recherche par nom d'utilisateur
    *************************
    Bouton Actualiser la liste: sert à rafraîchir la liste des utilisateurs après une recherche
    **************************
    Bouton ajouter utilisateur: sert à afficher le formulaire de saisie d'un nouvel utilisateur
    **************************
      Encodage : 
      *********
        * Saisir le nom
        * Saisir le prénom
        * Saisir la date de naissance
        * Saisir l'adresse mail
        * Saisir la Rue et le N°
        * Saisir le code postal et la localité
        * Saisir le login
        * Saisir le mot de passe
        * Spécifier si le nouvel utilisteur est administrateur (Simple membre par défaut)
        * Bouton "valider" : Valider l'inscription
        
    Bouton modifier utilisateur: sert à modifier un utilisateur existant.
    ***************************
    Bouton supprimer un utilisateur: sert à supprimer un utilisateur existant.
    *******************************
     

Bouton Livres: sert à afficher la page "Gestion des livres"
**************

    Fenêtre principale : Affiche le catalogue des livres.
    ******************
    Bouton Recherche par titre: sert à effectuer une recherche par titre de livre
    **************************
    Bouton Recherche par N° ISBN: sert à effectuer une recherche par N° ISBN ( Les trois premieres chiffres sont identiques pour tous les livres "978....")
    ****************************
    Bouton Recherche par auteurs: sert à effectuer une recherche par auteur
    ****************************
    Bouton Actualiser la liste: sert à rafraîchir la liste des livres après une recherche
    **************************
    Bouton ajouter livre: sert à afficher le formulaire de saisie d'un nouveau livre
    *********************
      Encodage : 
      *********
        * Saisir le titre (première lettre en majuscule)
        * Saisir le/les auteur(s)
        * Saisir l'année de publication
        * Saisir le numero ISBN
        * Sélectionner le/les éditeur(s)
        * Sélectionner la/les collection(s)
        * Sélectionner le/les genres(s)
        * Spécifier si le livre est disponible (par défaut indisponible)
        * Bouton "valider" : Valider l'inscription
        
    Bouton modifier un livre: sert à modifier un livre existant.
    ************************
    Bouton supprimer un livre: sert à supprimer un livre existant.
    **************************

Bouton Etagères: sert à afficher la page "Gestion des étagères"
***************

    (Une allée représente un couloir, et représentée par un chiffre, une allée contient des rayons représentés par des lettres)
    
    Fenêtre principale : affiche toutes les étagères.
    ******************
    Bouton Recherche par allée: sert à effectuer une recherche par numéro d'allée 
    **************************
    Bouton Recherche par rayon: sert à effectuer une recherche par lettre de rayon
    **************************
    Bouton Actualiser la liste: sert à rafraîchir la liste des étagères après une recherche
    **************************
    Bouton ajouter une étagère: sert à afficher le formulaire de saisie d'une nouvelle étagère
    **************************
    
      Encodage : 
      *********
        * Saisir le numéro de l'allée
        * Saisir la lettre du rayon de l'allée
        * Bouton de validation: valider
        
    Bouton modifier une étagère: sert à modifier une étagère.
    ***************************
    Bouton supprimer une étagère: sert à supprimer une étagère existante.
    ****************************
    Bouton ajouter un livre à une étagère: sert à ajouter un livre à une étagère.
    *************************************
      * Choisir le livre dans la liste
      * Bouton ajouter : Valider
    Bouton enlever un livre d'une étagère: sert à retirer un livre d'une étagère.
    *************************************
      * Choisir le livre dans l'étagère
      * Bouton supprimer : Valider le retrait du livre de l'étagère

Bouton Réservations: sert à afficher la page "Gestion des résérvations"
*******************
  Fenêtre pricipale: Affiche toutes les demandes de réservation soumises par les membres
  *****************
  Bouton accepter : permet d'accepter une demande de réservation
  ****************
  Bouton refuser : permet de refuser une demande de réservation
  **************
  Bouton supprimer : permet de supprimer une demande de réservation
  ****************

Bouton Emprunts: sert à afficher la page "Gestion des emprunts"
****************
  Fenêtre pricipale: Affiche tous les emprunts
  *****************
    Retard et Amende: affichés sur la fenêtre principale avec le reste des informations concernant l'emprunt.
    *****************
  Bouton Recherche des emprunts par utilisateur: sert à afficher l'historique des empruts efféctué par un utilisateur.
  *********************************************
    
    Ps: La fonction d'affichage d'historique des emprunts par utilisateur fonctionne parfaitement lorsque l'interface borrowApp est executé seule,
        mais cette dernière ne fonctionne pas une fois borrwApp liée au programme principale ( apelée depuis adminHomePage) 
  
  Bouton Actualiser la liste: sert à rafraîchir la liste des emprunts après une recherche
  **************************
  Bouton ajouter emprunt: sert à afficher le formulaire de saisie d'un nouvel emprunt
  **********************
      Encodage : 
      *********
        * Sélectionner un utilisateur
        * Sélectionner un livre
        * Saisir une date d'emprunt
        * Saisir une date de retour
        * Bouton "valider" : Valider l'emprunt
        
    Bouton modifier un emprunt: sert à modifier un emprunt existant (Fonction à optimiser)
    **************************
    Bouton supprimer un emprunt: sert à supprimer un emprunt existant.
    ***************************
      
Bouton "se deconnecter" : sert à quitter la page "Espace administrateur", et retourner à la page de connexion.
***********************

***************************************************************************************************************

Page Espace membre:
*******************

Bouton Recherche par titre: sert à effectuer une recherche par titre de livre
**************************

Bouton Recherche par N° ISBN: sert à effectuer une recherche par N° ISBN ( Les trois premieres chiffres sont identiques pour tous les livres "978....")
****************************

Bouton Recherche par auteurs: sert à effectuer une recherche par auteur
****************************

Bouton Actualiser la liste: sert à rafraîchir la liste des livres après une recherche
**************************

Bouton Faire une réservation: sert à effectuer une demande de réservation d'un livre 
****************************

  Page Application de réservation:
  ********************************
  
  Fenêtre principale : Affiche le catalogue des livres disponible.
  ******************
 
  Encodage : 
  *********
    * Séléctionner un livre
    * Date de début : Date souhaitée pour le début de la réservation ( ne peut être anterieure à la date du jour)
    * Date de fin : date de fin de la période de réservation.
    * Bouton soumettre la réservation : Valider la demande.  

Bouton "se deconnecter" : sert à quitter la page "Espace membre", et retourner à la page de connexion.
***********************

Fenêtre principale : Affiche le catalogue des livres disponible.
******************

************************************************************************************************************

Auteurs:
********
  * Rolande DJERI
  * Abdelkadir KIRATLI
  * Farid ASLOUN
  * Néhémie MUBENGA MAWEJA

Remérciements:
*************
Merci à Monsieur BURNIAUX François pour nous avoir assistés, orientés et guidés pour la réalisation de ce projet.











  
