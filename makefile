
run: main.py display.py draw.py matrix.py parse.py mypic.py
	python mypic.py
	python main.py
	convert -delay 5 *.jpg orbit.gif

clean:
	rm *.pyc
	rm *~
