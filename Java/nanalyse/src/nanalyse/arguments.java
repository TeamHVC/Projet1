package nanalyse;

public class arguments {
	public static void main(String[] args) {
		System.out.println("Il y a " + args.length + " arguments.");
		for(int i = 0; i < args.length; i++) 
			System.out.println("L'argument #" + (i+1) + " est " + args[i] );
	}
}
