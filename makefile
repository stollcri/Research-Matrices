SCALE = -s
CONTRAST = -c

SVDOPTS_A = -k 8
SVDOPTS_AVG = -k 4 -s -c

LETTER_PIX = D
SVDOPTS_PIX = -k 8 -s -c

default: svda

all: svda

svda:
	./svd.py ./img/A-pgm/A-01.pgm ./out/A-01.pgm ${SVDOPTS_A} ${SCALE}
	./svd.py ./img/A-pgm/A-01.pgm ./out/A-01c.pgm ${SVDOPTS_A} ${SCALE} ${CONTRAST}

svdasmalls:
	./svd.py ./img/A-pgm/A-00b.pgm ./out/a00b_0-0.pgm ${SCALE} ${CONTRAST}
	./svd.py ./img/A-pgm/A-00b.pgm ./out/a00b_0-2.pgm -k 2 ${SCALE} ${CONTRAST}
	./svd.py ./img/A-pgm/A-00b.pgm ./out/a00b_0-4.pgm -k 4 ${SCALE} ${CONTRAST}
	./svd.py ./img/A-pgm/A-00b.pgm ./out/a00b_1-3.pgm -j 1 -k 3 ${SCALE} ${CONTRAST}

	./svd.py ./img/A-pgm/A-00w.pgm ./out/a00w_0-0.pgm ${SCALE} ${CONTRAST}
	./svd.py ./img/A-pgm/A-00w.pgm ./out/a00w_0-2.pgm -k 2 ${SCALE} ${CONTRAST}
	./svd.py ./img/A-pgm/A-00w.pgm ./out/a00w_0-4.pgm -k 4 ${SCALE} ${CONTRAST}
	./svd.py ./img/A-pgm/A-00w.pgm ./out/a00w_1-3.pgm -j 1 -k 3 ${SCALE} ${CONTRAST}

svd-pix:
	./svd-pix.py ./img/${LETTER_PIX}-pgm/${LETTER_PIX}-01.pgm ./out/avg1.pgm ${SVDOPTS_PIX}

svd-avg:
	# ./svd-pix.py ./img/A-pgm/A-01.pgm ./out/A-01.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-02.pgm ./out/A-02.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-03.pgm ./out/A-03.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-04.pgm ./out/A-04.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-05.pgm ./out/A-05.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-06.pgm ./out/A-06.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-07.pgm ./out/A-07.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-08.pgm ./out/A-08.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-09.pgm ./out/A-09.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-10.pgm ./out/A-10.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-11.pgm ./out/A-11.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-12.pgm ./out/A-12.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-13.pgm ./out/A-13.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-14.pgm ./out/A-14.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-15.pgm ./out/A-15.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-16.pgm ./out/A-16.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-17.pgm ./out/A-17.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-18.pgm ./out/A-18.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-19.pgm ./out/A-19.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-20.pgm ./out/A-20.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-21.pgm ./out/A-21.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-22.pgm ./out/A-22.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-23.pgm ./out/A-23.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-24.pgm ./out/A-24.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-25.pgm ./out/A-25.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-26.pgm ./out/A-26.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-27.pgm ./out/A-27.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-28.pgm ./out/A-28.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-29.pgm ./out/A-29.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-30.pgm ./out/A-30.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-31.pgm ./out/A-31.pgm ${SVDOPTS_AVG}
	# ./svd-pix.py ./img/A-pgm/A-32.pgm ./out/A-32.pgm ${SVDOPTS_AVG}

	./svd-avg.py ./out/A-01.pgm   ./out/A-02.pgm ./out/aAvg00.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg00.pgm ./out/A-03.pgm ./out/aAvg01.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg01.pgm ./out/A-01.pgm ./out/aAvg02.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg02.pgm ./out/A-01.pgm ./out/aAvg03.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg03.pgm ./out/A-01.pgm ./out/aAvg04.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg04.pgm ./out/A-01.pgm ./out/aAvg05.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg05.pgm ./out/A-08.pgm ./out/aAvg06.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg06.pgm ./out/A-09.pgm ./out/aAvg07.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg07.pgm ./out/A-01.pgm ./out/aAvg08.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg08.pgm ./out/A-01.pgm ./out/aAvg09.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg09.pgm ./out/A-12.pgm ./out/aAvg10.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg10.pgm ./out/A-13.pgm ./out/aAvg11.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg11.pgm ./out/A-14.pgm ./out/aAvg12.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg12.pgm ./out/A-15.pgm ./out/aAvg13.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg13.pgm ./out/A-01.pgm ./out/aAvg14.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg14.pgm ./out/A-01.pgm ./out/aAvg15.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg15.pgm ./out/A-18.pgm ./out/aAvg16.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg16.pgm ./out/A-19.pgm ./out/aAvg17.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg17.pgm ./out/A-20.pgm ./out/aAvg18.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg18.pgm ./out/A-21.pgm ./out/aAvg19.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg19.pgm ./out/A-22.pgm ./out/aAvg20.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg20.pgm ./out/A-23.pgm ./out/aAvg21.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg21.pgm ./out/A-24.pgm ./out/aAvg22.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg22.pgm ./out/A-25.pgm ./out/aAvg23.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg23.pgm ./out/A-26.pgm ./out/aAvg24.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg24.pgm ./out/A-27.pgm ./out/aAvg25.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg25.pgm ./out/A-28.pgm ./out/aAvg26.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg26.pgm ./out/A-29.pgm ./out/aAvg27.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg27.pgm ./out/A-30.pgm ./out/aAvg28.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg28.pgm ./out/A-31.pgm ./out/aAvg29.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/aAvg29.pgm ./out/A-32.pgm ./out/aAvg30.pgm ${SVDOPTS_AVG}


stuff:
	./svd-avg.py ./img/stuff.pgm ./img/stuff.pgm ./out/stuff.pgm ${SVDOPTS_AVG}

clean:
	-rm ./out/*.pgm
