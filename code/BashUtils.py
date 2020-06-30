import os
rootPath = '/code/'
def translateMapping():
    os.system("yarrrml-parser -i %stmp/mapping.yaml -o %stmp/mapping.ttl"%(rootPath, rootPath))