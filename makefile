
all: arguments_python

arguments_python: Synthese.py
	python -m py_compile Synthese.py

clean:
	rm -f arguments.o
	rm -f arguments
	rm -f arguments.ali
	rm -f arguments.class
	rm -f arguments.pyc



