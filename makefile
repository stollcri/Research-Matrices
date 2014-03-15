SCALE = -s
CONTRAST = -c

SVDOPTS_A = -k 8
SVDOPTS_AVG = -k 4 -s -c

default: svda

all: svda

svda:
	./svd.py ./img/a-pgm/a-01.pgm ./out/a-01.pgm ${SVDOPTS_A} ${SCALE}
	./svd.py ./img/a-pgm/a-01.pgm ./out/a-01c.pgm ${SVDOPTS_A} ${SCALE} ${CONTRAST}

svdasmalls:
	./svd.py ./img/a-pgm/a-00b.pgm ./out/a00b_0-0.pgm ${SCALE} ${CONTRAST}
	./svd.py ./img/a-pgm/a-00b.pgm ./out/a00b_0-2.pgm -k 2 ${SCALE} ${CONTRAST}
	./svd.py ./img/a-pgm/a-00b.pgm ./out/a00b_0-4.pgm -k 4 ${SCALE} ${CONTRAST}
	./svd.py ./img/a-pgm/a-00b.pgm ./out/a00b_1-3.pgm -j 1 -k 3 ${SCALE} ${CONTRAST}

	./svd.py ./img/a-pgm/a-00w.pgm ./out/a00w_0-0.pgm ${SCALE} ${CONTRAST}
	./svd.py ./img/a-pgm/a-00w.pgm ./out/a00w_0-2.pgm -k 2 ${SCALE} ${CONTRAST}
	./svd.py ./img/a-pgm/a-00w.pgm ./out/a00w_0-4.pgm -k 4 ${SCALE} ${CONTRAST}
	./svd.py ./img/a-pgm/a-00w.pgm ./out/a00w_1-3.pgm -j 1 -k 3 ${SCALE} ${CONTRAST}

svd-pix:
	./svd-pix.py ./img/a-pgm/a-01.pgm ./out/aAvg1.pgm ${SVDOPTS_A} ${SCALE} ${CONTRAST}
	./svd-pix.py ./out/aAvg1.pgm ./out/aAvg2.pgm ${SVDOPTS_A} ${SCALE} ${CONTRAST}
	./svd-pix.py ./out/aAvg2.pgm ./out/aAvg1.pgm ${SVDOPTS_A} ${SCALE} ${CONTRAST}
	./svd-pix.py ./out/aAvg1.pgm ./out/aAvg2.pgm ${SVDOPTS_A} ${SCALE} ${CONTRAST}
	./svd-pix.py ./out/aAvg2.pgm ./out/aAvg1.pgm ${SVDOPTS_A} ${SCALE} ${CONTRAST}
	./svd-pix.py ./out/aAvg1.pgm ./out/aAvg2.pgm ${SVDOPTS_A} ${SCALE} ${CONTRAST}

svd-avg:
	# ./svd-pix.py ./img/a-pgm/a-01.pgm ./out/a-01.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-02.pgm ./out/a-02.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-03.pgm ./out/a-03.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-04.pgm ./out/a-04.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-05.pgm ./out/a-05.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-06.pgm ./out/a-06.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-07.pgm ./out/a-07.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-08.pgm ./out/a-08.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-09.pgm ./out/a-09.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-10.pgm ./out/a-10.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-11.pgm ./out/a-11.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-12.pgm ./out/a-12.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-13.pgm ./out/a-13.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-14.pgm ./out/a-14.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-15.pgm ./out/a-15.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-16.pgm ./out/a-16.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-17.pgm ./out/a-17.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-18.pgm ./out/a-18.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-19.pgm ./out/a-19.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-20.pgm ./out/a-20.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-21.pgm ./out/a-21.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-22.pgm ./out/a-22.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-23.pgm ./out/a-23.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-24.pgm ./out/a-24.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-25.pgm ./out/a-25.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-26.pgm ./out/a-26.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-27.pgm ./out/a-27.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-28.pgm ./out/a-28.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-29.pgm ./out/a-29.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-30.pgm ./out/a-30.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-31.pgm ./out/a-31.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/a-pgm/a-32.pgm ./out/a-32.pgm ${SVDOPTS_AVG}

	./svd-avg.py ./out/a-01.pgm   ./out/a-02.pgm ./out/aAvg00.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg00.pgm ./out/a-03.pgm ./out/aAvg01.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg01.pgm ./out/a-01.pgm ./out/aAvg02.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg02.pgm ./out/a-01.pgm ./out/aAvg03.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg03.pgm ./out/a-01.pgm ./out/aAvg04.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg04.pgm ./out/a-01.pgm ./out/aAvg05.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg05.pgm ./out/a-08.pgm ./out/aAvg06.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg06.pgm ./out/a-09.pgm ./out/aAvg07.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg07.pgm ./out/a-01.pgm ./out/aAvg08.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg08.pgm ./out/a-01.pgm ./out/aAvg09.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg09.pgm ./out/a-12.pgm ./out/aAvg10.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg10.pgm ./out/a-13.pgm ./out/aAvg11.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg11.pgm ./out/a-14.pgm ./out/aAvg12.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg12.pgm ./out/a-15.pgm ./out/aAvg13.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg13.pgm ./out/a-01.pgm ./out/aAvg14.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg14.pgm ./out/a-01.pgm ./out/aAvg15.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg15.pgm ./out/a-18.pgm ./out/aAvg16.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg16.pgm ./out/a-19.pgm ./out/aAvg17.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg17.pgm ./out/a-20.pgm ./out/aAvg18.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg18.pgm ./out/a-21.pgm ./out/aAvg19.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg19.pgm ./out/a-22.pgm ./out/aAvg20.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg20.pgm ./out/a-23.pgm ./out/aAvg21.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg21.pgm ./out/a-24.pgm ./out/aAvg22.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg22.pgm ./out/a-25.pgm ./out/aAvg23.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg23.pgm ./out/a-26.pgm ./out/aAvg24.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg24.pgm ./out/a-27.pgm ./out/aAvg25.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg25.pgm ./out/a-28.pgm ./out/aAvg26.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg26.pgm ./out/a-29.pgm ./out/aAvg27.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg27.pgm ./out/a-30.pgm ./out/aAvg28.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg28.pgm ./out/a-31.pgm ./out/aAvg29.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg29.pgm ./out/a-32.pgm ./out/aAvg30.pgm ${SVDOPTS_AVG}


stuff:
	./svd-avg.py ./img/stuff.pgm ./img/stuff.pgm ./out/stuff.pgm ${SVDOPTS_AVG}

clean:
	-rm ./out/*.pgm
