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
build/plotc.pdf: plotc.py matplotlibrc header-matplotlib.tex Datencd.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python plotc.py

build/plota1.pdf: plota1.py matplotlibrc header-matplotlib.tex Datena1.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python plota1.py

build/plota2.pdf: plota2.py matplotlibrc header-matplotlib.tex Datena2.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python plota2.py

build/plotd.pdf: plotd.py matplotlibrc header-matplotlib.tex Datencd.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python plotd.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plotc.pdf build/plota1.pdf build/plota2.pdf build/plotd.pdf

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
