package analyse;
import java.util.ArrayList;
import java.io.*;

public class Main {


	
	public static void main(String[] args){
		String chaine="";
		String fichier ="o.ppm";
		ArrayList<X_y> boobasG=new ArrayList<X_y>();
		ArrayList<X_y> boobasD=new ArrayList<X_y>();
		
		//lecture du fichier texte	
		try{
			InputStream ips=new FileInputStream(fichier); 
			InputStreamReader ipsr=new InputStreamReader(ips);
			BufferedReader br=new BufferedReader(ipsr);
			String ligne=br.readLine();
			ligne=br.readLine();
			
			
			String L_H [] ={"",""};
			
			int t=0;
			int l=0;
			for (int i=0 ;i<ligne.length(); i++ ){
				if (ligne.charAt(t) == ' '){
					t++;
					l++;
				}
				else{
					L_H[l]=L_H[l]+ligne.charAt(t);
					
					t++;
				}
				
			}
			int espace=0;
			int k =0;
			int j =0;
			String couleur="";
			String[][] image = new String[ Integer.parseInt(L_H[0])][ Integer.parseInt(L_H[1])];
			ligne=br.readLine();
			ligne=br.readLine();
			
			for (int i=0 ;i<Integer.parseInt(L_H[1]); i++ ){
				while (k<ligne.length()-1){
						while (espace !=3){
							if (ligne.charAt(k)==' '){
								espace++;
							}
							couleur=couleur+ligne.charAt(k);
							k++;
						}
						image[i][j]=couleur;
						j++;
						espace=0;
						couleur="";
						k++;
				}
				j=0;
				ligne=br.readLine();
				k=0;
			}
			br.close();
			
			int booG=0;
			int basG=0;
			int wG=0;
			while(basG<Integer.parseInt(L_H[1])){
				while(booG<Integer.parseInt(L_H[0])){
					if(image[basG][booG].equals("255 255 255 ")){
						booG++;
					}
					else{
						boobasG.add(new X_y(booG,basG));
						wG++;
						basG++;
						booG=0;
					}
				}
				basG++;
				booG=0;
			}
			System.out.println(wG);
			
			int booD=Integer.parseInt(L_H[0])-1;
			int basD=0;
			int wD=0;
			while(basD<Integer.parseInt(L_H[1])-1){
				while(booD>=0){
					if(image[basD][booD].equals("255 255 255 ")){
						booD--;
					}
					else{
						boobasD.add(new X_y(booD,basD));
						wD++;
						basD++;
						booD=Integer.parseInt(L_H[0])-1;
					}
				}
				basD++;
				booD=Integer.parseInt(L_H[0])-1;
			}
			
			for(int u=0;u<wG;u++){
				System.out.println(boobasG.get(u).getx()+" "+boobasG.get(u).gety()+" - "+boobasD.get(u).getx()+" "+boobasD.get(u).gety());
			}
			
			int larg=0;
			int haut=0;
			int o=0;
			int b=0;
			int x=o;
			int y=b;
			String coul=image[0][0];

			while (b<Integer.parseInt(L_H[1])){
				while (o<Integer.parseInt(L_H[0])){
					if(image[b][o].equals("255 255 255 ")){
						
					}
					else{
						x=o;
						y=b;
						String p = image[b][o];
						coul=image[b][o];
						
						while (image[b][o].equals(p) && o<Integer.parseInt(L_H[0])){
							larg++;
							o++;
						}
						o--;
						while (image[b][o].equals(p) && b<Integer.parseInt(L_H[1])){
							haut++;
							b++;
						}
						
					}
					o++;
				}
				o=0;
				b++;
			}
			System.out.println("x= "+x+" y= "+y+" largeur= "+larg +" hauteur= "+ haut+" couleur= "+coul);
		}		
		catch (Exception e){
			System.out.println(e.toString());
		}
		
	}
}