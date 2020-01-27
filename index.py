import re
dataTypes = ['int', 'double', 'string', 'bool', 'float']

def main():
    pass


class DeconstructFile():
    def __init__(self, filePath):
        with open(filePath) as body:
            self.file = body
            self.contentsList = body.readlines()
            self.contents = body.read()

    def parse(self):
        print(len(self.contentsList))
        isInComment = False
        for i in range(1, len(self.contentsList), 1):
            currentLine = self.contentsList[i]
            currentLine = self.removeComment(currentLine)
            print(currentLine)
            if isInComment == False:
                
                pass
            else:
                pass
            #print(currentLine)
        print(self.contentsList)

    def removeComment(self, line):
        newLine = ''
        if self.isComment(line):
            newLine = line.split(self.firstComment(line))[0]
            return newLine
        else:
            return line

    def firstComment(self, line):
        single = line.find('//')
        multi = line.find('/*')
        single = single if single != -1 else multi + 1
        multi = multi if multi != -1 else single + 1
        
        if single < multi:
            return '//'
        else:
            return '/*'
        
    def isComment(self, line):
        if line.find('//') > -1 or line.find('/*') > -1:
            return True
        return NotImplemented

    def isInBrackets(self):
        return NotImplemented

    def isInQuotes(self):
        return NotImplemented

    def isVariable(self):
        return NotImplemented

    def isFunction(self):
        return NotImplemented
    
    def isPreProcessor(self, line):
        location = line.find('#include')
        if (location > -1):
            pass


            
if __name__== "__main__":
    main()
    cl = DeconstructFile('example.cpp')
    cl.parse()