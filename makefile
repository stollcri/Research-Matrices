default: svd

all: svd

svd:
	./svd.py ./img/a-pgm/a-00b.pgm > ./out/a00b_0-0.pgm
	./svd.py ./img/a-pgm/a-00b.pgm -k 2 > ./out/a00b_0-2.pgm
	./svd.py ./img/a-pgm/a-00b.pgm -k 4 > ./out/a00b_0-4.pgm
	./svd.py ./img/a-pgm/a-00b.pgm -j 1 -k 3 > ./out/a00b_1-3.pgm

	./svd.py ./img/a-pgm/a-00w.pgm > ./out/a00w_0-0.pgm
	./svd.py ./img/a-pgm/a-00w.pgm -k 2 > ./out/a00w_0-2.pgm
	./svd.py ./img/a-pgm/a-00w.pgm -k 4 > ./out/a00w_0-4.pgm
	./svd.py ./img/a-pgm/a-00w.pgm -j 1 -k 3 > ./out/a00w_1-3.pgm
