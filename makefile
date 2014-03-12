SCALE = -s

default: svda

all: svda

svda:
	./svd.py ./img/a-pgm/a-00b.pgm ./out/a00b_0-0.pgm ${SCALE}
	./svd.py ./img/a-pgm/a-00b.pgm ./out/a00b_0-2.pgm -k 2 ${SCALE}
	./svd.py ./img/a-pgm/a-00b.pgm ./out/a00b_0-4.pgm -k 4 ${SCALE}
	./svd.py ./img/a-pgm/a-00b.pgm ./out/a00b_1-3.pgm -j 1 -k 3 ${SCALE}

	./svd.py ./img/a-pgm/a-00w.pgm ./out/a00w_0-0.pgm ${SCALE}
	./svd.py ./img/a-pgm/a-00w.pgm ./out/a00w_0-2.pgm -k 2 ${SCALE}
	./svd.py ./img/a-pgm/a-00w.pgm ./out/a00w_0-4.pgm -k 4 ${SCALE}
	./svd.py ./img/a-pgm/a-00w.pgm ./out/a00w_1-3.pgm -j 1 -k 3 ${SCALE}
