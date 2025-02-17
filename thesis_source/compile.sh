setopt NULL_GLOB
rm -f *.aux *.bbl *.blg *.lof *.log *.lot *.out *.toc *.fls *.fdb_latexmk
unsetopt NULL_GLOB

pdflatex -interaction=nonstopmode surname_name_mastercourse_ay.tex
bibtex surname_name_mastercourse_ay
pdflatex -interaction=nonstopmode surname_name_mastercourse_ay.tex
pdflatex -interaction=nonstopmode surname_name_mastercourse_ay.tex
