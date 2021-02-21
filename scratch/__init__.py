import json
import zipfile
import os
from .sprite import Sprite,Stage
from .errors import WrongFileError,SB3Error
from time import time

class Scratch(object):
    def __init__(self,json_path:str):
        self.t=time()
        if not os.path.isfile(json_path):
            raise FileNotFoundError

        try:
            self.pro_json=zipfile.ZipFile(json_path).read('project.json').decode()
        except zipfile.BadZipFile:
            raise WrongFileError('Cannot read the .sb3 file')

        try:
            self.program=json.loads(self.pro_json)
            self.sprites=[]
            for item in self.program['targets']:
                if item['isStage']:
                    self.stage=Stage(item)
                else:
                    self.sprites.append(Sprite(item))
        except Exception:
            raise SB3Error('The .sb3 file\'s format is wrong ')

        self.t=time()-self.t

    def analyze(self):
        t=time()
        self.analy={
            "motion":0,
            "looks":0,
            "sound":0,
            "event":0,
            "sensing":0,
            "control":0,
            "operator":0,
            "data":0,
            "procedures":0,
            "argument":0,
            "other":0
        }
        for sprite in self.sprites:
            for block in sprite.blocks.values():
                if block.Type in self.analy.keys():
                    self.analy[block.Type]+=1
                else:
                    self.analy['other']+=1
        self.analy['total']=sum(self.analy.values())
        self.t+=time()-t
        return {
            'blockStat':self.analy,
            'time':float('%.8f'%self.t)
        }