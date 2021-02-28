import json

def translate(block_Stat:dict,lang_file:str):
    lang_dict=json.loads(open('scratch\\lang\\%s'%lang_file,encoding='utf-8').read())
    returnDict={}
    for key in block_Stat.keys():
        try:
            returnDict[lang_dict[key]]=block_Stat[key]
        except KeyError:
            returnDict[key]=block_Stat[key]
    return returnDict