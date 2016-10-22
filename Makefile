start: source
	cp source/* .
	chmod a+x execute.sh
	./execute.sh
	rm *.bbl *.blg *.lof *.log *.out *.toc *.aux *.pdf *.png *.pyc *.py *.html *.tex *.sh *.bib *.ipynb *.txt


clean:
	rm -r output


test: source
	python source/test_code.py
	

