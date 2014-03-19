SCALE = -s
CONTRAST = -c
LETTER_AVG = D
SVDOPTS_A = -k 8
SVDOPTS_PIX = -k 8
SVDOPTS_AVG = -k 8 -s -c

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
	./svd-pix.py ./img/A-pgm/A-01.pgm ./out/A-avg.pgm ${SVDOPTS_PIX}
	./svd-pix.py ./img/B-pgm/B-01.pgm ./out/B-avg.pgm ${SVDOPTS_PIX}
	./svd-pix.py ./img/C-pgm/C-01.pgm ./out/C-avg.pgm ${SVDOPTS_PIX}
	./svd-pix.py ./img/D-pgm/D-01.pgm ./out/D-avg.pgm ${SVDOPTS_PIX}
	./svd-pix.py ./img/E-pgm/E-01.pgm ./out/E-avg.pgm ${SVDOPTS_PIX}
	./svd-pix.py ./img/F-pgm/F-01.pgm ./out/F-avg.pgm ${SVDOPTS_PIX}

svd-avg:
	cp ./img/${LETTER_AVG}-pgm/${LETTER_AVG}-01.pgm ./out/${LETTER_AVG}-01.pgm
	cp ./img/${LETTER_AVG}-pgm/${LETTER_AVG}-02.pgm ./out/${LETTER_AVG}-02.pgm
	cp ./img/${LETTER_AVG}-pgm/${LETTER_AVG}-03.pgm ./out/${LETTER_AVG}-03.pgm
	cp ./img/${LETTER_AVG}-pgm/${LETTER_AVG}-04.pgm ./out/${LETTER_AVG}-04.pgm
	cp ./img/${LETTER_AVG}-pgm/${LETTER_AVG}-05.pgm ./out/${LETTER_AVG}-05.pgm
	cp ./img/${LETTER_AVG}-pgm/${LETTER_AVG}-06.pgm ./out/${LETTER_AVG}-06.pgm
	cp ./img/${LETTER_AVG}-pgm/${LETTER_AVG}-07.pgm ./out/${LETTER_AVG}-07.pgm
	cp ./img/${LETTER_AVG}-pgm/${LETTER_AVG}-08.pgm ./out/${LETTER_AVG}-08.pgm
	cp ./img/${LETTER_AVG}-pgm/${LETTER_AVG}-09.pgm ./out/${LETTER_AVG}-09.pgm
	cp ./img/${LETTER_AVG}-pgm/${LETTER_AVG}-10.pgm ./out/${LETTER_AVG}-10.pgm
	cp ./img/${LETTER_AVG}-pgm/${LETTER_AVG}-11.pgm ./out/${LETTER_AVG}-11.pgm
	cp ./img/${LETTER_AVG}-pgm/${LETTER_AVG}-12.pgm ./out/${LETTER_AVG}-12.pgm
	cp ./img/${LETTER_AVG}-pgm/${LETTER_AVG}-13.pgm ./out/${LETTER_AVG}-13.pgm
	cp ./img/${LETTER_AVG}-pgm/${LETTER_AVG}-14.pgm ./out/${LETTER_AVG}-14.pgm
	cp ./img/${LETTER_AVG}-pgm/${LETTER_AVG}-15.pgm ./out/${LETTER_AVG}-15.pgm
	cp ./img/${LETTER_AVG}-pgm/${LETTER_AVG}-16.pgm ./out/${LETTER_AVG}-16.pgm

	./svd-pix.py ./out/${LETTER_AVG}-01.pgm ./out/avg00.pgm ${SVDOPTS_PIX}
	./svd-avg.py ./out/avg00.pgm ./out/${LETTER_AVG}-02.pgm ./out/avg01.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg01.pgm ./out/${LETTER_AVG}-03.pgm ./out/avg02.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg02.pgm ./out/${LETTER_AVG}-04.pgm ./out/avg03.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg03.pgm ./out/${LETTER_AVG}-05.pgm ./out/avg04.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg04.pgm ./out/${LETTER_AVG}-06.pgm ./out/avg05.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg05.pgm ./out/${LETTER_AVG}-07.pgm ./out/avg06.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg06.pgm ./out/${LETTER_AVG}-08.pgm ./out/avg07.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg07.pgm ./out/${LETTER_AVG}-09.pgm ./out/avg08.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg08.pgm ./out/${LETTER_AVG}-10.pgm ./out/avg09.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg09.pgm ./out/${LETTER_AVG}-11.pgm ./out/avg10.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg10.pgm ./out/${LETTER_AVG}-12.pgm ./out/avg11.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg11.pgm ./out/${LETTER_AVG}-13.pgm ./out/avg12.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg12.pgm ./out/${LETTER_AVG}-14.pgm ./out/avg13.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg13.pgm ./out/${LETTER_AVG}-15.pgm ./out/avg14.pgm ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg14.pgm ./out/${LETTER_AVG}-16.pgm ./out/avg15.pgm ${SVDOPTS_AVG}

stuff:
	./svd-avg.py ./img/stuff.pgm ./img/stuff.pgm ./out/stuff.pgm ${SVDOPTS_AVG}

clean:
	-rm ./out/*.pgm
