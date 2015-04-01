public class Main {


	public static void main(String[] args) {
		int choix;
		boolean fini = false;
while (fini == false){
			
			System.out.println("Que voulez-vous faire?");
			choix = Keyboard.getInt();
			
			switch(choix){
			
				case 1 :
					File image = new File("ot.pgm");
					Fichier.ConvertirMatrice("ot.pgm");
					break;}
			
		}
					
				

	}

}
