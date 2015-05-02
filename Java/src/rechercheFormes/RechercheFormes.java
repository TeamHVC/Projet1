package rechercheFormes;

import java.awt.Color;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;


public class RechercheFormes {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("fichiermodifie.txt")));
		String uneLigne = null;
		//la ligne qu'on lit actuellement
		boolean fini = false;
		//pour arreter l'analyse
		int[] tablargeurhauteur = new int[2];
		//tableau qui recupere la largeur et la hauteur
		
		String schiffre ="";
		//variable servant a faire la concatenation des chiffres, qu'on transformera apres en entier 
		
		
		
		uneLigne = br.readLine();
		
		System.out.println("longueur tab = " + tablargeurhauteur.length);
		
		
		
		//recuperation de la largeur et la hauteur 
		
		
		// ici i =1 car on commence par le deuxieme caractere pour eviter le 1er caractere qui sera un '|'
		int unchiffre = 0;
		for (int i=1; i<= uneLigne.length()-1;i++){
			if(uneLigne.charAt(i)==' '){
			tablargeurhauteur[unchiffre]= Integer.parseInt(schiffre); 
				unchiffre++;
				schiffre = "";

				
			}
			else{
				
				schiffre = schiffre + uneLigne.charAt(i);
				
			}
			
			
		}
		
		int largeur = tablargeurhauteur[0];//tablargeurhauteur[0] sera la largeur,
		int hauteur = tablargeurhauteur[1];//tablargeurhauteur[1] sera la hauteur
		System.out.println("largeur de l'image = " + largeur);
		System.out.println("hauteur de l'image = " + hauteur);
		
		uneLigne = br.readLine();
		
		// recuperation de la valeur maximale pour chaque composante RGB (inutile)
		
		uneLigne = br.readLine();
		
		
		//ajout de toutes les valeurs dans une matrice 
		
		String [][] point = new String[hauteur][largeur];
		String uneCouleur ="";
		int ligne = 0;
		int colonne = 0;
		while (! fini){ 
			
			for (int i=1; i<= uneLigne.length()-1;i++){
				if(uneLigne.charAt(i)=='|'){
					point[colonne][ligne]= uneCouleur;
					colonne ++;
					uneCouleur ="";
					
				}
				else{
					uneCouleur = uneCouleur +uneLigne.charAt(i);
				}
				
	
			}
				ligne++;
				colonne = 0;
			
			
			uneLigne = br.readLine();


			if (uneLigne == null) {
			fini = true;
			}
			else{
			fini = false;
			}
		}
		br.close();	
		
		//recherche des points a gauche
		
		
		ArrayList<Points>tabgauche = new ArrayList<Points>();

		int jg = 0;
		boolean trouveg;
		
		for (int i=0; i< point.length;i++){
			trouveg = false;
			while (! trouveg){
				//System.out.print(point[i][jg]+ "  ");
				jg++;
				if(jg==point.length){
					trouveg = true;
				}
				else if (! point[jg][i].equals("255 255 255")){
					tabgauche.add(new Points(jg,i));
					trouveg = true;
					
				}
				else{
					trouveg = false;
				}
				
				
			}
			
			jg = 0;
			//System.out.println("");
		}
		System.out.println("elements a gauche");
		for (int i=0; i<tabgauche.size();i++){
			System.out.println("coord x = "+tabgauche.get(i).x + " coord y = " + tabgauche.get(i).y);
		}
		
		//recherche des points a droite
		
		
		ArrayList<Points>tabdroite = new ArrayList<Points>();

		int jd = point[0].length;
		boolean trouved;
		
		for (int i=0; i< point.length;i++){
			trouved = false;
			while (! trouved){
				
				jd--;
				
				if(jd==0){
					trouved = true;
				}
				else if (! point[jd][i].equals("255 255 255")){
					
					tabdroite.add(new Points(jd,i));
					trouved = true;
					
				}
				else{
					trouved = false;
				}
				
				
			}
			
			jd = point[0].length;
			//System.out.println("");
		}
		System.out.println("elements a droite");
		for (int i=0; i<tabdroite.size();i++){
			System.out.println("coord x = "+tabdroite.get(i).x + " coord y = " + tabdroite.get(i).y);
		}

		
		//comparaison
		DictionnaireCouleur dico = new DictionnaireCouleur();
		System.out.println("couleur = " + dico.donneCouleur("255 255 255"));

		
		
		boolean droiteverticalegauche = false;
		
		for (int i=0; i<tabgauche.size()-1;i++){
			if (tabgauche.get(i).x==tabgauche.get(i+1).x){
				droiteverticalegauche = true;
			}
			else{
				droiteverticalegauche = false;
			}
			//System.out.println(droiteverticalegauche);

		}
		
		
		boolean droiteverticaledroite = false;
		for (int i=0; i<tabdroite.size()-1;i++){
			if (tabdroite.get(i).x==tabdroite.get(i+1).x){
				droiteverticaledroite = true;
			}
			else{
				droiteverticaledroite = false;
			}
			//System.out.println(droiteverticaledroite);

		}
		
		
		
		boolean memecol = false ;
		
		for (int i=0; i<tabgauche.size();i++){
			if (tabgauche.get(i).x==tabdroite.get(i).x){
				memecol = true;
			}
			else{
				memecol = false;
			}
			System.out.println(memecol);
		}
		
		
		
		if(droiteverticalegauche && droiteverticaledroite){
			if(memecol){
				System.out.println("La forme est un segment vertical du point(x="+tabgauche.get(0).x+",y="+tabgauche.get(0).y+") au point(x="+tabgauche.get(tabgauche.size()-1).x+",y="+tabgauche.get(tabgauche.size()-1).y+")");
			}
		
			else{
				
				System.out.println("La forme est un rectangle qui commence au point(x="+tabgauche.get(0).x+",y="+tabgauche.get(0).y+") de largeur "+(tabdroite.get(0).x-tabgauche.get(0).x)+" pixels, de hauteur "+(tabgauche.get(tabgauche.size()-1).y-tabgauche.get(0).y)+" pixels et de couleur "+ dico.donneCouleur(point[tabgauche.get(0).x][tabgauche.get(0).y]));
			}
		}
	
		else if( droiteverticalegauche ^ droiteverticaledroite){
			System.out.println("La forme est un triangle");
		}
		



	}

}


/*while (! fini){

for (int i=1; i<= uneLigne.length()-1;i++){
	if(uneLigne.charAt(i)=='|'){
		if (tabcouleur1.isEmpty()|| uneCouleur != tabcouleur1.get(0).couleur){
			tabcouleur2.add(new Points(ligne,colonne,uneCouleur));
		}
		else{
			tabcouleur1.add(new Points(ligne,colonne,uneCouleur));
		}	
		uneCouleur = "";
		ligne++;
		

		
	}
	else{
		
		uneCouleur = uneCouleur + uneLigne.charAt(i);
		
	}
}
colonne++;
ligne = 0;
uneLigne = br.readLine();



if (uneLigne == null) {
fini = false;
}
else{
fini = true;
}



} */







/*if(uneLigne.charAt(i)=='|'){
if (tabcouleur1.isEmpty()&& tabcouleur2.isEmpty()){
	tabcouleur1.add(new Points(ligne,colonne,uneCouleur));
}
else{
	if(!tabcouleur1.isEmpty() && uneCouleur.equals(tabcouleur1.get(0).couleur)){
		tabcouleur1.add(new Points(colonne,ligne,uneCouleur));
	}
	else{
		tabcouleur2.add(new Points(colonne,ligne,uneCouleur));

		}
}
uneCouleur = "";
colonne++;



}
else{

uneCouleur = uneCouleur + uneLigne.charAt(i);

}*/