SCALE = -s

default: svda

all: svda

svda:
	./svd.py ./img/a-pgm/a-00b.pgm ${SCALE} > ./out/a00b_0-0.pgm
	./svd.py ./img/a-pgm/a-00b.pgm -k 2 ${SCALE} > ./out/a00b_0-2.pgm
	./svd.py ./img/a-pgm/a-00b.pgm -k 4 ${SCALE} > ./out/a00b_0-4.pgm
	./svd.py ./img/a-pgm/a-00b.pgm -j 1 -k 3 ${SCALE} > ./out/a00b_1-3.pgm

	./svd.py ./img/a-pgm/a-00w.pgm ${SCALE} > ./out/a00w_0-0.pgm
	./svd.py ./img/a-pgm/a-00w.pgm -k 2 ${SCALE} > ./out/a00w_0-2.pgm
	./svd.py ./img/a-pgm/a-00w.pgm -k 4 ${SCALE} > ./out/a00w_0-4.pgm
	./svd.py ./img/a-pgm/a-00w.pgm -j 1 -k 3 ${SCALE} > ./out/a00w_1-3.pgm
