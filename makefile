LETTER_AVG = F

SVDOPTS_A = -k 8 -c
SVDOPTS_PIX = -k 8
SVDOPTS_AVG = -k 8 -s -c

default: svdbw

all: clean svdbw

svdbw:
	./svd.py ./img/stuff-bw.png ./out/stuff-bw.png ${SVDOPTS_A}

svdrgb:
	./svd-rgb.py ./img/stuff-rgb.png ./out/stuff-rgb.png ${SVDOPTS_A}

svd-pix:
	./svd-pix.py ./img/A-png/A-01.png ./out/A-avg.png ${SVDOPTS_PIX}
	./svd-pix.py ./img/B-png/B-01.png ./out/B-avg.png ${SVDOPTS_PIX}
	./svd-pix.py ./img/C-png/C-01.png ./out/C-avg.png ${SVDOPTS_PIX}
	./svd-pix.py ./img/D-png/D-01.png ./out/D-avg.png ${SVDOPTS_PIX}
	./svd-pix.py ./img/E-png/E-01.png ./out/E-avg.png ${SVDOPTS_PIX}
	./svd-pix.py ./img/F-png/F-01.png ./out/F-avg.png ${SVDOPTS_PIX}

svd-avg:
	./svd-pix.py ./img/${LETTER_AVG}-png/${LETTER_AVG}-01.png ./out/avg00.png ${SVDOPTS_PIX}
	./svd-avg.py ./out/avg00.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-02.png ./out/avg01.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg01.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-03.png ./out/avg02.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg02.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-04.png ./out/avg03.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg03.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-05.png ./out/avg04.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg04.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-06.png ./out/avg05.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg05.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-07.png ./out/avg06.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg06.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-08.png ./out/avg07.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg07.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-09.png ./out/avg08.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg08.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-10.png ./out/avg09.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg09.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-11.png ./out/avg10.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg10.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-12.png ./out/avg11.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg11.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-13.png ./out/avg12.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg12.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-14.png ./out/avg13.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg13.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-15.png ./out/avg14.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg14.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-16.png ./out/avg15.png ${SVDOPTS_AVG}

clean:
	-rm ./out/*.png
