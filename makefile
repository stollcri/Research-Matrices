LETTER_AVG = A

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
	./svd-pix.py ./img/${LETTER_AVG}-png/${LETTER_AVG}-0.png ./out/avg00.png ${SVDOPTS_PIX}
	./svd-avg.py ./out/avg00.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-1.png ./out/avg01.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg01.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-2.png ./out/avg02.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg02.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-3.png ./out/avg03.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg03.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-4.png ./out/avg04.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg04.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-5.png ./out/avg05.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg05.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-6.png ./out/avg06.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg06.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-7.png ./out/avg07.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg07.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-8.png ./out/avg08.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg08.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-9.png ./out/avg09.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg09.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-10.png ./out/avg10.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg10.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-11.png ./out/avg11.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg11.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-12.png ./out/avg12.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg12.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-13.png ./out/avg13.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg13.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-14.png ./out/avg14.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg14.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-15.png ./out/avg15.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg15.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-16.png ./out/avg16.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg16.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-17.png ./out/avg17.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg17.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-18.png ./out/avg18.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg18.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-19.png ./out/avg19.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg19.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-20.png ./out/avg20.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg20.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-21.png ./out/avg21.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg21.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-22.png ./out/avg22.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg22.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-23.png ./out/avg23.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg23.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-24.png ./out/avg24.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg24.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-25.png ./out/avg25.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg25.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-26.png ./out/avg26.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg26.png ./img/${LETTER_AVG}-png/${LETTER_AVG}-27.png ./out/avg27.png ${SVDOPTS_AVG}

train:
	mkdir -p ./img/A-png && ./gen-train.py A ./img/A-png
	mkdir -p ./img/B-png && ./gen-train.py B ./img/B-png
	mkdir -p ./img/C-png && ./gen-train.py C ./img/C-png
	mkdir -p ./img/D-png && ./gen-train.py D ./img/D-png
	mkdir -p ./img/E-png && ./gen-train.py E ./img/E-png
	mkdir -p ./img/F-png && ./gen-train.py F ./img/F-png
	mkdir -p ./img/G-png && ./gen-train.py G ./img/G-png
	mkdir -p ./img/H-png && ./gen-train.py H ./img/H-png
	mkdir -p ./img/I-png && ./gen-train.py I ./img/I-png
	mkdir -p ./img/J-png && ./gen-train.py J ./img/J-png
	mkdir -p ./img/K-png && ./gen-train.py K ./img/K-png
	mkdir -p ./img/L-png && ./gen-train.py L ./img/L-png
	mkdir -p ./img/M-png && ./gen-train.py M ./img/M-png
	mkdir -p ./img/N-png && ./gen-train.py N ./img/N-png
	mkdir -p ./img/O-png && ./gen-train.py O ./img/O-png
	mkdir -p ./img/P-png && ./gen-train.py P ./img/P-png
	mkdir -p ./img/Q-png && ./gen-train.py Q ./img/Q-png
	mkdir -p ./img/R-png && ./gen-train.py R ./img/R-png
	mkdir -p ./img/S-png && ./gen-train.py S ./img/S-png
	mkdir -p ./img/T-png && ./gen-train.py T ./img/T-png
	mkdir -p ./img/U-png && ./gen-train.py U ./img/U-png
	mkdir -p ./img/V-png && ./gen-train.py V ./img/V-png
	mkdir -p ./img/W-png && ./gen-train.py W ./img/W-png
	mkdir -p ./img/X-png && ./gen-train.py X ./img/X-png
	mkdir -p ./img/Y-png && ./gen-train.py Y ./img/Y-png
	mkdir -p ./img/Z-png && ./gen-train.py Z ./img/Z-png

clean:
	-rm ./out/*.png
