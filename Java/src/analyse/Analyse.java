package analyse;
import java.io.*;
//import java.util.Scanner;

public class Analyse {
	
	
	public static void main(String[] args) throws IOException{
		// On ouvre l'entree standard
				BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
				// uneLigne va stocker la ligne lue
				String uneLigne = null;
				// continuer indique s'il y a encore des choses a  lire ou si on a termine.
				boolean continuer = true;
				int couleur = 0;
				uneLigne = br.readLine();
				while ( continuer ) {
					if (uneLigne.equals("") || uneLigne.charAt(0)=='#'|| uneLigne.charAt(0)=='P'){
						
						
						uneLigne = br.readLine();
					
					
						if (uneLigne == null) {               //On enleve les lignes de commentaires, la ligne "P3" et les lignes vides
							continuer = false;
							br.close();
						}
						else{
							continuer = true;
						}	
					}
					else{
						
						
							//test si on a une ligne de commentaire
							
								
										// on supprime les espaces multiples
										uneLigne.replaceAll( "\\s+", " " ); 
										// On va maintenant la reafficher en separant les mots.
										System.out.print( "|" );
										
										
										
										for ( String s : uneLigne.split( " " ) ) {
											if ( s.length() > 0 ) {
												if (couleur ==2) {
													System.out.print( s + "|" );
													couleur = 0;
												}
												else{System.out.print( s + " " );
													couleur++;
												}
											}
										}
										
										
									
									System.out.println( "" );
									uneLigne = br.readLine();
									
									
									if (uneLigne == null) {
										continuer = false;
									}
									else{
										continuer = true;
									}
					}
								
								couleur = 0;
								
								
								
							}
							
				br.close();

	}
	
} 
	
	
