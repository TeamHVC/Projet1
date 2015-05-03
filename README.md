TELECHARGER NOTRE PROJET VIA GIT

- Ouvrir un terminal UNIX.
- Créer (avec la commande mkdir <nom>) ou aller dans un dossier où le Projet sera déposé.
- Initialiser le dossier en git (avec la commande git init).
- Choisir sur quel répertoire en ligne nous allons travailler (à l'aide de la commande
  git remote add origin <adressedurépertoire.git>).
- Confirmer le répertoire (avec la commande remote -v).
- Récupérer en local le répertoire en ligne (avec la commande git clone <adressedurépertoire>)
- Pour mettre à jour le répertoire local à partir des modifications faites en ligne, effectuer
  la commande git pull origin master.


COMPILER LE CODE

- Générateur (Synthèse d'images) - Python :
  Dans un terminal UNIX, aller dans le répertoire du projet à partir de la commande cd.
  (Dans ce même répertoire à été créé un fichier makefile, contenant les lignes nécessaires
  à la compilation du code à partir de la commande make.)
  Effectuer la commande make.
  (En Python, make ne compile pas vraiment. Il vérifie surtout les erreurs de syntaxe.)
  Les éventuelles erreurs de syntaxe s'affichent dans le terminal.

- Analyseur (Analyse d'images) - Java :
  Dans un terminal UNIX, aller dans le répertoire du projet à partir de la commande cd.
  (Dans ce même répertoire à été créé un fichier makefile, contenant les lignes nécessaires
  à la compilation du code à partir de la commande make.)
  Effectuer la commande make.
  Les éventuelles erreurs détectées à la compilation s'affichent dans le terminal.  


LANCER LE GENERATEUR (Synthèse d'images) VIA LE TERMINAL

1 - Se mettre dans le dossier du programme avec la commande cd
2 - Se donner les droits avec la commande chmod +x NomduFichier.py
3 - Effectuer la commande make afin de vérifier qu'il n'y ait pas d'erreurs de syntaxe
4 - Taper ./NomduFichier.py suivi des arguments correspondant à l'action désirée.

Les arguments sont les suivants :
- POINT : --point <nom de l'image à créer>
	  <coordonnéeX> <coordonnéeY> <Couleur**>
	  <largeurImageàCréer> <hauteurImageàCréer>
- SEGMENT : --segment <nom de l'image à créer>
	    <coordonnéeX 1erpoint> <coordonnéeY 1erpoint> <coordonnéeX 2emepoint> <coordonnéeY 2emepoint> <Couleur**>
	    <largeurImageàCréer> <hauteurImageàCréer>
- RECTANGLE : --rectangle <nom de l'image à créer>
              <coordonnéeX Pointdedépart> <coordonnéeYPointdedépart> <hauteur> <largeur> <Booléen*> <Couleur**>
	      <largeurImageàCréer> <hauteurImageàCréer>
- TRIANGLE : --triangle <nom de l'image à créer>
	     <X 1erpoint> <Y 1erpoint> <X 2emepoint> <Y 2emepoint> <X 3emepoint> <Y 3emepoint> <Booléen*> <Couleur**>
	     <largeurImageàCréer> <hauteurImageàCréer>
- CERCLE : --cercle <nom de l'image à créer>
	   <coordonnéeX Centre> <coordonnéeY Centre> <rayon> <Booléen*> <Couleur**>
	   <largeurImageàCréer> <hauteurImageàCréer>

*Booléen : True pour Plein
	   False pour Vide

**425 couleurs disponibles
  Précéder le nom de la couleur par une majuscule
  Pour les couleurs composées, les deux mots ne sont pas séparés d'un espace
  (Ex : Rosebonbon)

Une image est donc ensuite créée dans le même répertoire que le projet.
La forme par défaut est le Cercle de centre (60,60) et de rayon 30.
La couleur par défaut pour toutes les formes est le Bleu.

LANCER L'ANALYSEUR (Analyse d'images) VIA LE TERMINAL

1 - Se mettre dans le dossier du programme avec la commande cd
2 - Disposer d'un fichier .PPM à analyser dans le même dossier
    (Sinon, en créer un grâce au Générateur)
3 - Se donner les droits avec la commande chmod +x NomduFichier.java
4 - Effectuer la commande make afin de compiler le programme
5 - Taper java analyse.Analyse <NomImage.ppm >NomFichierTransformé.txt
    ce qui va transformer le .ppm en .txt afin de pouvoir mieux l'analyser
6 - Taper java rechercheFormes.RechercheFormes <NomFichierTransformé.txt
    Les résultats de l'analyse s'affichent dans le terminal.

Il est possible de stocker les résultats de l'analyse dans un fichier.txt
Pour celà, rajouter à la fin de la ligne de commande de l'étape 6 :
  >NomFichierOùStockerLeRésultat.txt 

