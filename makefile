LETTER_AVG = 3

SVDOPTS_A = -k 8 -c
SVDOPTS_PIX = -k 8
SVDOPTS_AVG = -k 8 -s -c

default: svdbw

all: deepclean trainingset train

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


trainingset:
	@for letter in A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ; do \
		mkdir -p ./img/$$letter-png ; \
		./gen-train.py $$letter ./img/$$letter-png ; \
	done
	@echo $@ complete


pretr_set := $(foreach i,A B C D E F G H I J K L M N O P Q R S T U V W X Y Z,pre-$i)
train_set := $(foreach i,A B C D E F G H I J K L M N O P Q R S T U V W X Y Z,$(foreach j,1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27,job-$i-$j))
psttr_set := $(foreach i,A B C D E F G H I J K L M N O P Q R S T U V W X Y Z,pst-$i)
i = $(firstword $(subst -, ,$*))
j = $(lastword $(subst -, ,$*))

.PHONY: pretr train psttr
pretr: ${pretr_set}
train: pretr ${train_set} psttr; @echo $@ complete
psttr: ${psttr_set}

.PHONY: ${pretr_set}
${pretr_set}: pre-%:
	./svd-pix.py ./img/$*-png/$*-0.png ./out/$*-0.png ${SVDOPTS_PIX}

.PHONY: ${train_set}
${train_set}: job-%:
	./svd-avg.py ./out/$i-$$(($j-1)).png ./img/$i-png/$i-$j.png ./out/$i-$j.png ${SVDOPTS_AVG} ; \

.PHONY: ${psttr_set}
${psttr_set}: pst-%:
	-mv ./out/$*-27.png ./out/avg_$*.png
	-rm ./out/$*-*.png


.PHONY: deepclean clean cleantrain
deepclean: clean cleantrain
clean:
	@-rm ./out/*.png
	@echo $@ complete
cleantrain:
	@for letter in A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ; do \
		rm -r ./img/$$letter-png ; \
	done
	@echo $@ complete
