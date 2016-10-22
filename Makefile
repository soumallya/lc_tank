start: source
	cp source/* .
	chmod a+x execute.sh
	./execute.sh
	rm *.bbl *.blg *.lof *.log *.out *.toc *.aux *.pdf *.png *.pyc *.py *.html *.tex *.sh *.bib *.ipynb *.txt


clean:
	rm -r *.py *.pyc output


test: source
	cp source/test_code.py .
	cp source/LC_tank_both.py .
	python test_code.py
	rm *.py *.pyc

