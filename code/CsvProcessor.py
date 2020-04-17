import csv
import sys
class CsvProcessor:
    def __init__(self, path):
        self.path = path
        self.ncols = 0
        self.values = []
        self.outputFile = 'data.csv'
        self.labelsFile = 'labels.csv'
        self.csvReader = None
        self.__loadCsv()
        self.__initializeOutputFiles()
        
    def __loadCsv(self):
        with open(self.path, mode='r') as csv_file:
            self.csvReader = list(csv.reader(csv_file, delimiter=','))
            self.ncols = len(self.csvReader[0])

    def __initializeOutputFiles(self):
        f = open(self.outputFile, 'w')
        line = ''.join('level_%s'%(str(i))+ ',' for i in range(self.ncols -1)) 
        line = line[:-1] + '\n'
        f.write(line)
        f.close()
        f = open(self.labelsFile, 'w')
        f.write('id,label\n')
        f.close()
        self.values = ['' for i in range(self.ncols - 1)]

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
        f.write('"' + row[i] + '"' + ',' + '"' + row[-1] + '"' + '\n')
        f.close()
    def __updateValues(self, row, i):
        if i < self.ncols -1 and row[i] != "" and row[i] != " " and row[i] != self.values[i]:
            self.values[i] = row[i]
            self.__writeLabel(row, i)
            if(i < self.ncols - 2):
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
