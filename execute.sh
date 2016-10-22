python main.py
pdflatex 153070018.tex
pdflatex 153070018.tex
bibtex 153070018.aux
pdflatex 153070018.tex
pdflatex 153070018.tex
ipython nbconvert 153070018.ipynb

mkdir output
cp *.png output/
cp *.pdf output/
cp *.html output/
cp *.txt output/

