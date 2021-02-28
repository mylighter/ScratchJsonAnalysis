ERR_STR={
    'format':'The .sb3 file\'s format is wrong'
}
class WrongFileError(Exception):
    pass
class SB3Error(Exception):
    def __init__(self,errorType:str):
        self.msg=ERR_STR[errorType]

    def __str__(self):
        return self.msg