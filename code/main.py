import yaml
import json
import sys
import argparse
from shutil import copyfile
from MappingGenerator import MappingGenerator
from CsvProcessor import CsvProcessor 

#awk -F ',' '{$1="\""$1;$NF=$NF"\"";print $0 } OFS="\",\""' clasificacion-economica-gasto-labels-extended.csv > test_extended.csv
def readConfig(path):
    try:
        conf = json.loads(open(path+'config.json', 'r', encoding='utf-8').read())
        requiredFields = ["skosFileName", "descriptionFileName", "skosUri", "skosPrefix"]
        if(sorted(requiredFields) != sorted(conf.keys())):
            raise Exception("Review the configuration file, it's wrong.")
        if(not validateDescriptionFile(path + conf["descriptionFileName"])):
            raise Exception("The description file is not valid.")
        copyfile(path + conf["skosFileName"], './tmp/csv/input.csv')
        copyfile(path + conf["descriptionFileName"], './tmp/csv/description.csv')
        return conf
    except Exception as e:
        print(e)
        sys.exit()
    
    
def validateDescriptionFile(path):
    f = open(path, 'r', encoding='utf-8')
    fields = f.readline().strip().replace("\n", "").split(",")
    requiredFields = "creator,date,title,name,".split(",")
    return sorted(fields) == sorted(requiredFields)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--config_path", required=True, help="Input config file path.")
    args = parser.parse_args()
    conf = readConfig(args.config_path)
    csvProcessor = CsvProcessor()
    skosUri = conf["skosUri"]
    skosPrefix = conf["skosPrefix"]
    mappingGenerator = MappingGenerator(csvProcessor.ncols - 3, skosUri, skosPrefix)
if __name__ == '__main__':
    main()
