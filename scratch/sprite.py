from .blocks import Block
class Sprite(object):
    def __init__(self,sprite:dict):
        self.sprite=sprite
        self.name=sprite['name']

        self.variables={}
        for var in sprite['variables'].values():
            self.variables[var[0]]=var[1]

        self.lists={}
        for List in sprite['variables'].values():
            self.lists[List[0]]=List[1]

        self.blocks={}
        for code,block in sprite['blocks'].items():
            if len(code)==20:
                self.blocks[code]=Block(code,block)

    def __repr__(self):
        return f'<scratch_Sprite Object:{self.name} at {hex(id(self))}>'

class Stage(Sprite):
    '''
    直接继承角色类
    '''
    def __repr__(self):
        return f'<scratch_Stage Object:Stage at {hex(id(self))}>'