
all: arguments.class arguments_python

arguments.class: 
	javac rechercheFormes\RechercheFormes.java rechercheFormes\DictionnaireCouleur.java rechercheFormes\Couleur.java rechercheFormes\Points.java analyse\Analyse.java
arguments_python: Synthese.py
	python -m py_compile Synthese.py
	
clean:

	rm -f arguments.o

	rm -f arguments

	rm -f arguments.ali

	rm -f arguments.class

	rm -f arguments.pyc