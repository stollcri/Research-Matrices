SCALE = -s
CONTRAST = -c
LETTER_AVG = D
SVDOPTS_A = -k 8
SVDOPTS_PIX = -k 4
SVDOPTS_AVG = -k 8 -s -c

default: svda

all: svda

svda:
	./svd.py ./img/A-png/A-01.png ./out/A-01.png ${SVDOPTS_A} ${SCALE}

svd-pix:
	./svd-pix.py ./img/A-png/A-01.png ./out/A-avg.png ${SVDOPTS_PIX}
	./svd-pix.py ./img/B-png/B-01.png ./out/B-avg.png ${SVDOPTS_PIX}
	./svd-pix.py ./img/C-png/C-01.png ./out/C-avg.png ${SVDOPTS_PIX}
	./svd-pix.py ./img/D-png/D-01.png ./out/D-avg.png ${SVDOPTS_PIX}
	./svd-pix.py ./img/E-png/E-01.png ./out/E-avg.png ${SVDOPTS_PIX}
	./svd-pix.py ./img/F-png/F-01.png ./out/F-avg.png ${SVDOPTS_PIX}

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
	-rm ./out/*.png
