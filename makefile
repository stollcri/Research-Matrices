SCALE = -s
AVG_OPTS = -k 16 -s

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

svd-avg:
	./svd-avg.py ./img/a-pgm/a-01.pgm ./img/a-pgm/a-02.pgm ./out/aAvg1.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg1.pgm ./img/a-pgm/a-03.pgm ./out/aAvg2.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg2.pgm ./img/a-pgm/a-04.pgm ./out/aAvg1.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg1.pgm ./img/a-pgm/a-05.pgm ./out/aAvg2.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg2.pgm ./img/a-pgm/a-06.pgm ./out/aAvg1.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg1.pgm ./img/a-pgm/a-07.pgm ./out/aAvg2.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg2.pgm ./img/a-pgm/a-08.pgm ./out/aAvg1.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg1.pgm ./img/a-pgm/a-09.pgm ./out/aAvg2.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg2.pgm ./img/a-pgm/a-10.pgm ./out/aAvg1.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg1.pgm ./img/a-pgm/a-11.pgm ./out/aAvg2.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg2.pgm ./img/a-pgm/a-12.pgm ./out/aAvg1.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg1.pgm ./img/a-pgm/a-13.pgm ./out/aAvg2.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg2.pgm ./img/a-pgm/a-14.pgm ./out/aAvg1.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg1.pgm ./img/a-pgm/a-15.pgm ./out/aAvg2.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg2.pgm ./img/a-pgm/a-16.pgm ./out/aAvg1.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg1.pgm ./img/a-pgm/a-17.pgm ./out/aAvg2.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg2.pgm ./img/a-pgm/a-18.pgm ./out/aAvg1.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg1.pgm ./img/a-pgm/a-19.pgm ./out/aAvg2.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg2.pgm ./img/a-pgm/a-20.pgm ./out/aAvg1.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg1.pgm ./img/a-pgm/a-21.pgm ./out/aAvg2.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg2.pgm ./img/a-pgm/a-22.pgm ./out/aAvg1.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg1.pgm ./img/a-pgm/a-23.pgm ./out/aAvg2.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg2.pgm ./img/a-pgm/a-24.pgm ./out/aAvg1.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg1.pgm ./img/a-pgm/a-25.pgm ./out/aAvg2.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg2.pgm ./img/a-pgm/a-26.pgm ./out/aAvg1.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg1.pgm ./img/a-pgm/a-27.pgm ./out/aAvg2.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg2.pgm ./img/a-pgm/a-28.pgm ./out/aAvg1.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg1.pgm ./img/a-pgm/a-29.pgm ./out/aAvg2.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg2.pgm ./img/a-pgm/a-30.pgm ./out/aAvg1.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg1.pgm ./img/a-pgm/a-31.pgm ./out/aAvg2.pgm ${AVG_OPTS}
	./svd-avg.py ./out/aAvg2.pgm ./img/a-pgm/a-32.pgm ./out/aAvg1.pgm ${AVG_OPTS}

	./svd-avg.py ./out/aAvg1.pgm ./img/a-pgm/a-01.pgm ./out/aAvg2.pgm ${AVG_OPTS}

