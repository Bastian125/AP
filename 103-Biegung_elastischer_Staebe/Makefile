all: build/main.pdf

# hier Python-Skripte:

build/plot1.pdf: Rechnung.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Rechnung.py
build/plot5.pdf: plot1.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot1.py
build/plot6.pdf: plot2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot2.py
build/plot7.pdf: plot3.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot3.py
build/plot8.pdf: plot4.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot4.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:

build/main.pdf: build/plot1.pdf
build/main.pdf: build/plot5.pdf
build/main.pdf: build/plot6.pdf
build/main.pdf: build/plot7.pdf
build/main.pdf: build/plot8.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
