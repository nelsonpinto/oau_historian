
all:
	@echo "This makefile is only for cleaning stuff up. ('make clean')"
	@echo "You can also build the tarball dist with it ('make sdist')"
	@echo "You can also build the win32 binary dist with it ('make windist')"

sdist: 
	python setup.py sdist
	@echo "Look in the dist/ directory"

windist: 
	python setup.py bdist_wininst
	@echo "Look in the dist/ directory"

upload_docs:
	mkdir -p build/docs
	rm -f build/docs/*
	cp docs/* build/docs/
	python setup.py upload_sphinx
	rm build/docs/*
	rmdir build/docs
    
clean:
	@echo "Removing stray logfiles, Pyro URI dumps, .pyo/.pyc files..."
	find . -name \*_log  | xargs  rm -v
	find . -name \*.log  | xargs  rm -v
	find . -name \*_URI  | xargs  rm -v
	find . -name \*.pyo  | xargs  rm -v
	find . -name \*.pyc  | xargs  rm -v
	find . -name \*.class  | xargs  rm -v
	find . -name \*.DS_Store  | xargs  rm -v
	@echo "Removing non-CVS files..."
	rm -fv MANIFEST 
	rm -rf build
	find . -name  '.#*'  | xargs  rm -v 
	find . -name  '#*#'  | xargs  rm -v 

	@echo "clean!"
