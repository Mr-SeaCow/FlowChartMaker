import re
dataTypes = ['int', 'double', 'string', 'bool', 'float']

def main():
    fileRead = open('example.cpp', 'r')
    contentsLine = filterComments(fileRead.readlines())
    contentsWhole = fileRead.read()
    # HOW FUNCTIONS ARE STORED
    # {'FUNCTIONNAME': {'declaredLine': lineNumber, 'type': 'int', 'vars': {'varName': varType}}}

    # HOW VARIABLES ARE STORED
    # {'VARIABLENAME': {'declaredLine': lineNumber, 'type': 'int', value: ''}}
    preprocesser = []
    functions = {}
    variables = {}
    lineCounter = 0
    for line in contentsLine:
        lineCounter += 1
        if checkForPreprocessor(line):
            splitLineStripAppend(preprocesser, line, '#include ', 1)
        
        functionValues = checkForFunctions(line)
        if functionValues:
            functionObj = formatFunctionObj(functionValues.groups(), lineCounter)


       # print(line)
    
    print(preprocesser)

def formatFunctionObj(values, lineNumber):
    obj = {}
    varsObj = {}
    obj[values[1]] = {'declaredLine': lineNumber, 'type': values[0], 'vars': {}}
    if values[2]:

        arr = values[2].split(',')
        for x in arr:
            val = x.strip().split(' ')
            varsObj[val[0]] = val[1]
    
    obj[values[1]]['vars'] = varsObj
    
    return obj

def checkForPreprocessor(line):
    if line.find('#include') != -1:
        return True
    else:
        return False

def checkForFunctions(line):
    if line.find('=') > -1:
         return False
    for val in dataTypes:
        regex = r"(" + val + r") (.+?)[=?(](.+?|\0?)[=?)].+?|\0[=?{|]"
        match = re.search(regex, line)
        if match != None:
            return match
    return False

def filterComments(contents):
    newContents = []
    inAComment = False
    for line in contents:
        if inAComment == False:
            if line.find('/*') != -1:
                marker = line.find('//') if line.find('//') != -1 else 100000
                if line.find('/*') < marker:
                   splitLineStripAppend(newContents, line, '/*', 0)
                else:
                    splitLineStripAppend(newContents, line, '//', 0)
            elif line.find('//') != -1:
                splitLineStripAppend(newContents, line, '//', 0)
            else:
                newContents.append(line)
        else:
            if line.find('*/') != -1:
                splitLineStripAppend(newContents, line, '*/', 1)
                inAComment == True
            else:
                newContents.append(line)
    return newContents
                
def splitLineStripAppend(array, line, delimiter, number):
    marker = line.split(delimiter)[number]
    if marker != '':
        array.append(marker.strip())
        return
    array.append('\n')
    return

if __name__== "__main__":
    main()