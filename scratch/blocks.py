class Block(object):
    def __init__(self,block_code:str,block:dict):
        self.opcode=block['opcode']
        self.block_code=block_code
        self.next=block['next']
        self.parent=block['parent']
        self.topLevel=block['topLevel']
        self.Type=self.opcode.split('_')[0]
        self.block_name=self.opcode.split('_')[1]

        if self.topLevel:
            self.position=[block['x'],block['y']]
        else:
            self.position=[None,None]