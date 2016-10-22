python main.py
python animate.py
pdflatex 153070018.tex
pdflatex 153070018.tex
bibtex 153070018.aux
pdflatex 153070018.tex
pdflatex 153070018.tex

mkdir output
cp *.png output/
cp *.pdf output/
cp *.html output/
cp *.mp4 output/
cp *.txt output/
