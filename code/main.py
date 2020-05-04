import yaml
import json
import argparse
from shutil import copyfile
from MappingGenerator import MappingGenerator
from CsvProcessor import CsvProcessor 

#awk -F ',' '{$1="\""$1;$NF=$NF"\"";print $0 } OFS="\",\""' clasificacion-economica-gasto-labels-extended.csv > test_extended.csv
def readConfig(path):
    if(path[-1] != "/"):
        path += "/"
    conf = json.loads(open(path+'config.json', 'r', encoding='utf-8').read())
    copyfile(path + conf["skosFileName"], './tmp/csv/input.csv')
    copyfile(path + conf["descriptionFileName"], './tmp/csv/description.csv')
    return conf
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--config_path", required=True, help="Input config file path.")
    args = parser.parse_args()
    conf = readConfig(args.config_path)
    csvProcessor = CsvProcessor()
    skosUri = conf["skosUri"]
    mappingGenerator = MappingGenerator(csvProcessor.ncols - 3, skosUri)
if __name__ == '__main__':
    main()
