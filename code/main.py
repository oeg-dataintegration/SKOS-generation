import yaml
import json
def readYarrrml(mappingPath):
    data = yaml.load(open(mappingPath).read())
    with open('mapping.json', 'w') as f:
        f.write(json.dumps(data,indent=2))



def main():
    readYarrrml('../mappings/mapping.yaml')

if __name__ == '__main__':
    main()