import csv
import sys

nLabelColumns = 4
labelColumnsNames = "denomEs,denomEn,defEs,defEn"
class CsvProcessor:
    def __init__(self, path):
        self.path = path
        self.ncols = 0
        self.values = []
        self.outputFile = './data/data.csv'
        self.labelsFile = './data/labels.csv'
        self.csvReader = None
        self.__loadCsv()
        self.__initializeOutputFiles()
        
    def __loadCsv(self):
        with open(self.path, mode='r', encoding='utf-8') as csv_file:
            self.csvReader = list(csv.reader(csv_file, delimiter=','))
            self.ncols = len(self.csvReader[0])

    def __initializeOutputFiles(self):
        f = open(self.outputFile, 'w')
        line = ''.join('level_%s'%(str(i))+ ',' for i in range(self.ncols - nLabelColumns)) 
        line = line[:-1] + '\n'
        f.write(line)
        f.close()
        f = open(self.labelsFile, 'w')
        f.write('id,%s\n'%(labelColumnsNames))
        f.close()
        self.values = ['' for i in range(self.ncols - nLabelColumns)]

    def __shouldWrite(self):
        return (' ' not in self.values and '' not in self.values)
    def __writeFile(self, row):
        f = open(self.outputFile, '+a')
        line = ''.join( '"' + value + '"' + ',' for value in self.values)
        line = line[:-1] + '\n'
        f.write(line)
        f.close()
    def __writeLabel(self, row, i):
        f = open(self.labelsFile, 'a')
        labels = ''.join('"' + label + '",' for label in row[-nLabelColumns:])
        labels = labels[:-1]
        if("mantenimiento y conservación." in row):
            print(labels)
            print(row)
            print(i)
            print(self.ncols - nLabelColumns)
        f.write('"' + row[i] + '"' + ',' + labels + '\n')
        f.close()
    def __updateValues(self, row, i):
        if i < self.ncols - nLabelColumns and row[i] != "" and row[i] != " " and row[i] != self.values[i]:
            self.values[i] = row[i]
            self.__writeLabel(row, i)
            if(i < self.ncols - nLabelColumns - 1):
                self.values[i + 1] = ''

    def normalizeCsv(self):
        print(self.csvReader[1])
        for k,row in enumerate(self.csvReader[1:]):
            for i in range(self.ncols):
                self.__updateValues(row, i)
            if(self.__shouldWrite()):
                self.__writeFile(row)
            # if(k > 5):
            #     break
