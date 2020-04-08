import yaml
import json

class MappingGenerator:
    mappingStructure=json.loads(open('./levels.json').read())
    def __init__(self, nCols_, specificTaxonomy_):
        self.nCols = nCols_
        self.specificTaxonomy = specificTaxonomy_
        self.jsonMapping = {"mappings":{}, "prefixes":{}}
        self.yamlMapping = ''
    def __generateJsonMapping(self):
        keys = list(MappingGenerator.mappingStructure["levels"].keys())
        self.jsonMapping["prefixes"] = MappingGenerator.mappingStructure["prefixes"]
        self.jsonMapping["prefixes"].update({"specificTaxonomy":self.specificTaxonomy})
        j = 2
        for i in  range(self.nCols):
            if(i < 4):
                if(i == self.nCols - 1):

                    for k,tm in enumerate(MappingGenerator.mappingStructure["levels"][keys[i]]):
                        if(k < len(MappingGenerator.mappingStructure["levels"][keys[i]]) - 1):
                            self.jsonMapping["mappings"].update(tm)
                        else:
                            key = list(tm.keys())[0]
                            result = {
                                    key:{
                                        "sources": tm[key]["sources"],
                                        "s": tm[key]["s"],
                                        "po": [ tm[key]["po"][po] for po in range(len(tm[key]["po"]) - 1)]
                                        }
                                    }
                            self.jsonMapping["mappings"].update(result)
                else:                
                    for tm in MappingGenerator.mappingStructure["levels"][keys[i]]:
                        self.jsonMapping["mappings"].update(tm)
            else:
                prevLevel = i - 1
                prevSubConcept = j - 1
                nextLevel = i + 1
                nextSubConcept = j + 1
                tms = MappingGenerator.mappingStructure["levels"][keys[4]]
                if(i == self.nCols -1):
                    key = list(tms[-1].keys())[0]
                    tms[-1][key]["po"] = tms[-1][key]["po"][:-1]
                for tm in tms:
                    strTM = str(tm)
                    strTM = strTM.replace("_CURRENTSBC", '_' + str(j))
                    strTM = strTM.replace("_CURRENTLVL", '_' + str(i))
                    strTM = strTM.replace("_PREVLVL", '_' + str(prevLevel))
                    strTM = strTM.replace("_PREVSBC", '_' + str(prevSubConcept))
                    strTM = strTM.replace("_NXTLVL", '_' + str(nextLevel))
                    strTM = strTM.replace("_NXTSBC", '_' + str(nextSubConcept))
                    self.jsonMapping["mappings"].update(json.loads(strTM.replace("'", '"')))
                j = j +1
        #print(json.dumps(self.jsonMapping, indent=2))
        

    def __generateYamlMapping(self):
        dumpedMapping = str(yaml.dump(self.jsonMapping, default_flow_style=None))
        #dumpedMapping = dumpedMapping.replace("'\"", '"')
        #dumpedMapping = dumpedMapping.replace("\"'",'"')
        #dumpedMapping = dumpedMapping.replace('\'', '')
        self.yamlMapping = dumpedMapping

    def generateMapping(self, fileName='mapping.yaml'):
        self.__generateJsonMapping()
        self.__sanitizeYaml()
        f = open(fileName, '+w')
        f.write(self.yamlMapping)

    def __sanitizeYaml(self):
        for tm in self.jsonMapping["mappings"]:
            for i,po in enumerate(self.jsonMapping["mappings"][tm]["po"]):
                if(type(po) is list):
                    if(' ' in po[1] or '[' in po[1] or ']' in po[1] or ':' in po[1]):
                        self.jsonMapping["mappings"][tm]["po"][i][1] = '"' + po[1] + '"'
        self.yamlMapping = str(yaml.dump({"prefixes":self.jsonMapping["prefixes"]}, default_flow_style=False))
        self.yamlMapping +=  str(yaml.dump({"mappings":self.jsonMapping["mappings"]}, default_flow_style=None)).replace('"', '')
