import java.io.*;
//import java.util.*;



public class Fichier {
/*	public String [] RecupChar(String line){
		
		String mot;
		ArrayList<String>liste = new ArrayList<String>(); 
		for(int i =0; i< line.length(); i++){
			if (line.charAt(i)==' '){
				liste.add(mot);
				mot='';
				}
			else {
				mot = mot + line.charAt(i)
			}
			
		}
		return liste.toArray();
	}




	public int [][] ConvertirMatrice (File f) throws IOException{
		// fonction qui prend l'image en paramètre et retourne la matrice 
			FileInputStream image = new FileInputStream("f");
			InputStreamReader lire = new InputStreamReader(image);
			BufferedReader contenu = new BufferedReader (lire);
			String ligne = contenu.readLine();
			
			
			int largeur=10;int hauteur=10;String largeurS; String hauteurS;
			
			
			if (ligne =="P2"){
				ligne = contenu.readLine();
				//saut des 1er commentaires avant la ligne contenant la largeur et la hauteur
				while (ligne.charAt(0)=='#'){
					ligne = contenu.readLine();
				}
				//recupération de la largeur et de la hauteur
				String[] larghaut = RecupChar(ligne);
					largeur = Integer.parseInt(larghaut [0]);
					hauteur = Integer.parseInt(larghaut [1]);
					ligne = contenu.readLine();
					
					 			
				//saut des commentaires avant la ligne contenant la valeur maximale pour chaque pixel
				while (ligne.charAt(0)=='#'){
					ligne = contenu.readLine();
				}

			int [][] matrice = new int[largeur][hauteur];
					while (ligne!=null){
						for (int i=0; i<(largeur*2)-1; i++){
							for (int j=0; j<(hauteur*2)-1; j++){
								if (ligne.charAt(j)!=' '){matrice [i][j]=(int)((ligne.charAt(j)));}
							}
							ligne = contenu.readLine();
							
						}
					}
			contenu.close();
			
		return matrice;	
		
	}
}
}


*/
	//test pour la recupération du fichier 
	public String ConvertirMatrice (File f) throws IOException{
			FileInputStream image = new FileInputStream("f");
			InputStreamReader lire = new InputStreamReader(image);
			BufferedReader contenu = new BufferedReader (lire);
			String ligne = contenu.readLine();
			contenu.close();
			return ligne;
	}
}