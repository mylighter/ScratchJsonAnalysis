from scratch import Scratch
from scratch.translater import translate
sc=Scratch('Truth 21w4a.sb3')
print(translate(sc.analyze()['blockStat'],'cn-lang.json'))