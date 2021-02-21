from scratch import Scratch
from scratch.translater import translate
sc=Scratch('Exam.sb3')
analy=translate(sc.analyze()['blockStat'],'cn-lang.json')
print(analy)