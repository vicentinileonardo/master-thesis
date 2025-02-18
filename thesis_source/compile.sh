setopt NULL_GLOB
rm -f *.aux *.bbl *.blg *.lof *.log *.lot *.out *.toc *.fls *.fdb_latexmk
unsetopt NULL_GLOB

pdflatex -interaction=nonstopmode vicentini_leonardo_cs_23-24.tex
bibtex vicentini_leonardo_cs_23-24
pdflatex -interaction=nonstopmode vicentini_leonardo_cs_23-24.tex
pdflatex -interaction=nonstopmode vicentini_leonardo_cs_23-24.tex
