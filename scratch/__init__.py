import json
import zipfile
import os
from .sprite import Sprite,Stage
from .errors import *
from time import time

class Scratch(object):
    def __init__(self,json_path:str):
        self.t=time()
        if not os.path.isfile(json_path):
            raise FileNotFoundError('The file is not found')

        try:
            self.pro_json=zipfile.ZipFile(json_path).read('project.json').decode()
        except zipfile.BadZipFile:
            raise WrongFileError('The file cannot be read')
        except KeyError:
            raise SB3Error('format')


        try:
            self.program=json.loads(self.pro_json)
            self.sprites=[]
            for item in self.program['targets']:
                if item['isStage']:
                    self.stage=Stage(item)
                else:
                    self.sprites.append(Sprite(item))
        except Exception:
            raise SB3Error('The .sb3 file\'s format is wrong')

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
            "other":0,
        }
        self.passages=0
        try:
            for sprite in self.sprites:
                for block in sprite.blocks.values():
                    if block.topLevel:
                        self.passages+=1
                    if block.Type in self.analy.keys():
                        self.analy[block.Type]+=1
                    else:
                        self.analy['other']+=1
            self.analy['total']=sum(self.analy.values())

        except KeyError:
            raise
        self.t+=time()-t
        return {
            'blockStat':self.analy,
            'time':float('%.8f'%self.t),
            'passages':self.passages
        }
    def findSprite(self,name):
        returnValue=0
        for sprite in self.sprites:
            if sprite.name==name:
                returnValue=sprite
        if returnValue==0:
            returnValue='No sprites'
        return returnValue