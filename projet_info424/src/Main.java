import java.io.FileInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {



	public int [][] convertirMatrice (Fichier f) throws IOException{
		// fonction qui prend l'image en paramètre et retourne la matrice 
			FileInputStream image= new FileInputStream("f");
			InputStreamReader lire =new InputStreamReader(image);
			BufferedReader contenu = new BufferedReader (lire);
			String ligne = contenu.readLine();
			
			
			int largeur=10;int hauteur=10;
			
			
			//if (ligne =="P2"){
				//ligne = contenu.readLine();
				//if (ligne.charAt(0)=='#')
				//{ligne= contenu.readLine();}
				//else {}
			int [][] matrice = new int[largeur][hauteur];
					while (ligne!=null){
						for (int i=0; i<(largeur*2)-1; i++){
							for (int j=0; j<(hauteur*2)-1; j++){
								if (ligne.charAt(j)!=' '){matrice [i][j]=Integer.parseInt((ligne.charAt(j)));}
							}
							ligne = contenu.readLine();
							
						}
					}
			contenu.close();
			
		return matrice;	
		
	}
}
		

