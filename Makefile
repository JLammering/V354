ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  # Unix
  pwd := $$(pwd)
  translate = $1
else
  # Windows mit MSys2/Cygwin
  pwd := $$(cygpath -m "$$(pwd)")
  translate = $(shell echo '$1' | sed 's/:/;/g')
endif

all: build/main.pdf

# hier Python-Skripte:

build/plota.pdf: plota.py matplotlibrc header-matplotlib.tex Datena1.txt Datena2.txt Datena3.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python plota.py

build/plotc1.pdf: plotc1.py matplotlibrc header-matplotlib.tex Datencd.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python plotc1.py

build/plotc2.pdf: plotc2.py matplotlibrc header-matplotlib.tex Datencd.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python plotc2.py

build/plotd1.pdf: plotd1.py matplotlibrc header-matplotlib.tex Datencd.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python plotd1.py

build/plotd2.pdf: plotd2.py matplotlibrc header-matplotlib.tex Datencdh.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python plotd2.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf:  build/plota.pdf build/plotc1.pdf build/plotc2.pdf build/plotd1.pdf build/plotd2.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS="$(call translate,build:)" \
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
