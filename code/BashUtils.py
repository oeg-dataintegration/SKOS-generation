import os

def translateMapping():
    os.system("yarrrml-parser -i ./tmp/mapping.yaml -o ./tmp/mapping.ttl")