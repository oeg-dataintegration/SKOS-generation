import csv
import sys

nLabelColumns = 4
labelColumnsNames = "denomEs,denomEn,defEs,defEn,"

class CsvProcessor:
    def __init__(self, path="/code/tmp/csv/input.csv"):
        self.path = path
        self.ncols = 0
        self.values = []
        self.outputFile = '/code/tmp/csv/data.csv'
        self.labelsFile = '/code/tmp/csv/labels.csv'
        self.csvReader = None
        self.__loadCsv()
        self.__initializeOutputFiles()
        self.normalizeCsv()
        
    def __loadCsv(self):
        with open(self.path, mode='r', encoding='utf-8') as csv_file:
            self.csvReader = list(csv.reader(csv_file, delimiter=','))
            self.ncols = len(self.csvReader[0])

    def __initializeOutputFiles(self):
        f = open(self.outputFile,'w', encoding='utf-8')
        line = ''.join('level_%s'%(str(i))+ ',' for i in range(self.ncols - nLabelColumns)) 
        line += '\n'
        f.write(line)
        f.close()
        f = open(self.labelsFile,'w',encoding='utf-8')
        f.write('id,%s\n'%(labelColumnsNames))
        f.close()
        self.values = ['' for i in range(self.ncols - nLabelColumns)]

    def __shouldWrite(self, last):
        return (' ' not in self.values[:last] and '' not in self.values[:last])

    def __writeFile(self):
        f = open(self.outputFile,'+a',encoding='utf-8')
        line = ''.join( '"' + value + '"' + ',' for value in self.values)
        line = self.__normalizeText(line)
        line += '\n'
        f.write(line)
        f.close()

    def __writeLabel(self, row, i):
        f = open(self.labelsFile,'a',encoding='utf-8')
        labels = ''.join('"' + label + '",' for label in row[-nLabelColumns:])
        f.write('"' + self.__normalizeText(row[i]) + '"' + ',' + labels + '\n')
        f.close()
    def __updateValues(self, row, i):
        if i < self.ncols - nLabelColumns and row[i] != "" and row[i] != " " and row[i] != self.values[i]:
            if(i < self.ncols - nLabelColumns - 1):
                if('' in self.values and self.__shouldWrite(i)):
                    self.__writeFile()
                for j in range(i, self.ncols - nLabelColumns):
                    self.values[j] = ''            
            self.values[i] = row[i]
            self.__writeLabel(row, i)

    def normalizeCsv(self):
        for row in self.csvReader[1:]:
            for i in range(self.ncols):
                if(row[i] != "" and row[i] != " "):
                    self.__updateValues(row, i)
                    break
            if(self.__shouldWrite(len(self.values))):
                self.__writeFile()

    def __normalizeText(self, text):
        return str(text).lower().strip().replace("-"," ").replace(" ", "-").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ü","u").replace("ñ","n").replace(".", "")


#a = CsvProcessor()