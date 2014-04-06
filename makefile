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
	@for word in the be to of and in that have it for not on with he as you do at; do \
		mkdir -p ./img/train-png ; \
		./gen-train.py $$word ./img/train-png ; \
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


.PHONY: train train_u train_l train_n
train: train_u train_l train_n

i = $(firstword $(subst -, ,$*))

train_set_test := $(foreach i,A,tst-$i)
train_test: ${train_set_test};
.PHONY: ${train_set_test}
${train_set_test}: tst-%:
	./mean.py ./out/$i_u.png ./img/train-png/$i_u-*.png

train_set_u := $(foreach i,A B C D E F G H I J K L M N O P Q R S T U V W X Y Z,tsu-$i)
train_u: ${train_set_u};
.PHONY: ${train_set_u}
${train_set_u}: tsu-%:
	./mean.py ./out/$i_u.png ./img/train-png/$i_u-*.png

train_set_l := $(foreach i,a b c d e f g h i j k l m n o p q r s t u v w x y z,tsl-$i)
train_l: ${train_set_l};
.PHONY: ${train_set_l}
${train_set_l}: tsl-%:
	./mean.py ./out/$i_l.png ./img/train-png/$i_l-*.png

train_set_n := $(foreach i,0 1 2 3 4 5 6 7 8 9,tsn-$i)
train_n: ${train_set_n};
.PHONY: ${train_set_n}
${train_set_n}: tsn-%:
	./mean.py ./out/$i_n.png ./img/train-png/$i_n-*.png


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
