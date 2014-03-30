LETTER_AVG = A_u

SVDOPTS_A = -k 8 -c
SVDOPTS_PIX = -k 8
SVDOPTS_AVG = -c

default: all

.PHONY: all
all: deepclean trainingset train

.PHONY: svdbw
svdbw:
	./svd.py ./img/stuff-bw.png ./out/stuff-bw.png ${SVDOPTS_A}

.PHONY: svdrgb
svdrgb:
	./svd-rgb.py ./img/stuff-rgb.png ./out/stuff-rgb.png ${SVDOPTS_A}

.PHONY: svd-pix
svd-pix:
	./svd-pix.py ./img/train-png/A_u-0.png ./out/pix.png ${SVDOPTS_PIX}


.PHONY: svd-avg
svd-avg:
	./svd-avg.py ./img/train-png/${LETTER_AVG}-0.png ./img/train-png/${LETTER_AVG}-0.png ./out/avg00.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg00.png ./img/train-png/${LETTER_AVG}-1.png ./out/avg01.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg01.png ./img/train-png/${LETTER_AVG}-2.png ./out/avg02.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg02.png ./img/train-png/${LETTER_AVG}-3.png ./out/avg03.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg03.png ./img/train-png/${LETTER_AVG}-4.png ./out/avg04.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg04.png ./img/train-png/${LETTER_AVG}-5.png ./out/avg05.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg05.png ./img/train-png/${LETTER_AVG}-6.png ./out/avg06.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg06.png ./img/train-png/${LETTER_AVG}-7.png ./out/avg07.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg07.png ./img/train-png/${LETTER_AVG}-8.png ./out/avg08.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg08.png ./img/train-png/${LETTER_AVG}-9.png ./out/avg09.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg09.png ./img/train-png/${LETTER_AVG}-10.png ./out/avg10.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg10.png ./img/train-png/${LETTER_AVG}-11.png ./out/avg11.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg11.png ./img/train-png/${LETTER_AVG}-12.png ./out/avg12.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg12.png ./img/train-png/${LETTER_AVG}-13.png ./out/avg13.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg13.png ./img/train-png/${LETTER_AVG}-14.png ./out/avg14.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg14.png ./img/train-png/${LETTER_AVG}-15.png ./out/avg15.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg15.png ./img/train-png/${LETTER_AVG}-16.png ./out/avg16.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg16.png ./img/train-png/${LETTER_AVG}-17.png ./out/avg17.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg17.png ./img/train-png/${LETTER_AVG}-18.png ./out/avg18.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg18.png ./img/train-png/${LETTER_AVG}-19.png ./out/avg19.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg19.png ./img/train-png/${LETTER_AVG}-20.png ./out/avg20.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg20.png ./img/train-png/${LETTER_AVG}-21.png ./out/avg21.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg21.png ./img/train-png/${LETTER_AVG}-22.png ./out/avg22.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg22.png ./img/train-png/${LETTER_AVG}-23.png ./out/avg23.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg23.png ./img/train-png/${LETTER_AVG}-24.png ./out/avg24.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg24.png ./img/train-png/${LETTER_AVG}-25.png ./out/avg25.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg25.png ./img/train-png/${LETTER_AVG}-26.png ./out/avg26.png ${SVDOPTS_AVG}
	./svd-avg.py ./out/avg26.png ./img/train-png/${LETTER_AVG}-27.png ./out/avg27.png ${SVDOPTS_AVG}


.PHONY: trainingset trainingset-upper trainingset-lower trainingset-number
trainingset: trainingset-upper trainingset-lower trainingset-number

trainingset-test:
	@for letter in A; do \
		mkdir -p ./img/train-png ; \
		./gen-train.py $$letter ./img/train-png ; \
	done
	@echo $@ complete

trainingset-upper:
	@for letter in A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ; do \
		mkdir -p ./img/train-png ; \
		./gen-train.py $$letter ./img/train-png ; \
	done
	@echo $@ complete

trainingset-lower:
	@for letter in a b c d e f g h i j k l m n o p q r s t u v w x y z ; do \
		mkdir -p ./img/train-png ; \
		./gen-train.py $$letter ./img/train-png ; \
	done
	@echo $@ complete

trainingset-number:
	@for letter in 0 1 2 3 4 5 6 7 8 9 ; do \
		mkdir -p ./img/train-png ; \
		./gen-train.py $$letter ./img/train-png ; \
	done
	@echo $@ complete


.PHONY: train
train: train_u train_l train_n

pretr_set_u := $(foreach i,A B C D E F G H I J K L M N O P Q R S T U V W X Y Z,pre-$i)
train_set_u := $(foreach i,A B C D E F G H I J K L M N O P Q R S T U V W X Y Z,$(foreach j,1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32,job-$i-$j))
psttr_set_u := $(foreach i,A B C D E F G H I J K L M N O P Q R S T U V W X Y Z,pst-$i)
i = $(firstword $(subst -, ,$*))
j = $(lastword $(subst -, ,$*))

.PHONY: pretr_u train_u psttr_u
pretr_u: ${pretr_set_u}
train_u: pretr_u ${train_set_u} psttr_u; @echo $@ complete
psttr_u: ${psttr_set_u}

.PHONY: ${pretr_set_u}
${pretr_set_u}: pre-%:
	./svd-avg.py ./img/train-png/$i_u-0.png ./img/train-png/$i_u-0.png ./out/$*_u-0.png ${SVDOPTS_AVG}

.PHONY: ${train_set_u}
${train_set_u}: job-%:
	./svd-avg.py ./out/$i_u-$$(($j-1)).png ./img/train-png/$i_u-$j.png ./out/$i_u-$j.png ${SVDOPTS_AVG}

.PHONY: ${psttr_set_u}
${psttr_set_u}: pst-%:
	-mv ./out/$*_u-27.png ./out/$*_u.png
	-rm ./out/$*_?-*.png

pretr_set_l := $(foreach i,a b c d e f g h i j k l m n o p q r s t u v w x y z,pre-$i)
train_set_l := $(foreach i,a b c d e f g h i j k l m n o p q r s t u v w x y z,$(foreach j,1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32,job-$i-$j))
psttr_set_l := $(foreach i,a b c d e f g h i j k l m n o p q r s t u v w x y z,pst-$i)

.PHONY: pretr_l train_l psttr_l
pretr_l: ${pretr_set_l}
train_l: pretr_l ${train_set_l} psttr_l; @echo $@ complete
psttr_l: ${psttr_set_l}

.PHONY: ${pretr_set_l}
${pretr_set_l}: pre-%:
	./svd-avg.py ./img/train-png/$i_l-0.png ./img/train-png/$i_l-0.png ./out/$*_l-0.png ${SVDOPTS_AVG}

.PHONY: ${train_set_l}
${train_set_l}: job-%:
	./svd-avg.py ./out/$i_l-$$(($j-1)).png ./img/train-png/$i_l-$j.png ./out/$i_l-$j.png ${SVDOPTS_AVG}

.PHONY: ${psttr_set_l}
${psttr_set_l}: pst-%:
	-mv ./out/$*_l-27.png ./out/$*_l.png
	-rm ./out/$*_?-*.png

pretr_set_n := $(foreach i,0 1 2 3 4 5 6 7 8 9,pre-$i)
train_set_n := $(foreach i,0 1 2 3 4 5 6 7 8 9,$(foreach j,1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32,job-$i-$j))
psttr_set_n := $(foreach i,0 1 2 3 4 5 6 7 8 9,pst-$i)

.PHONY: pretr_n train_n psttr_n
pretr_n: ${pretr_set_n}
train_n: pretr_n ${train_set_n} psttr_n; @echo $@ complete
psttr_n: ${psttr_set_n}

.PHONY: ${pretr_set_n}
${pretr_set_n}: pre-%:
	./svd-avg.py ./img/train-png/$i_n-0.png ./img/train-png/$i_n-0.png ./out/$*_n-0.png ${SVDOPTS_AVG}

.PHONY: ${train_set_n}
${train_set_n}: job-%:
	./svd-avg.py ./out/$i_n-$$(($j-1)).png ./img/train-png/$i_n-$j.png ./out/$i_n-$j.png ${SVDOPTS_AVG}

.PHONY: ${psttr_set_n}
${psttr_set_n}: pst-%:
	-mv ./out/$*_n-27.png ./out/$*_n.png
	-rm ./out/$*_?-*.png


.PHONY: test
test:
	./ml-ocr.py -b ./out/ ./img/train-png/


.PHONY: deepclean clean cleantrain
deepclean: clean cleantrain
clean:
	@-rm ./out/*.png
	@echo $@ complete
cleantrain:
	@-rm -r ./img/train-png
	@echo $@ complete
