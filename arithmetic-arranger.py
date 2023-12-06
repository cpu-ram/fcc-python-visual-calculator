import re

def arithmeticArranger(self, expressions, displayResults):
    resultString=map(lambda x: processExpression(x), expressions)

    def assembleVisualResult():
        linesArray=["","","",""]
    for i in range(4):
         linesArray[i] = reduce(lambda a, b: str(a) + "    " + str(b), expressions[i]) # fix this!



    return resultString

def processExpression(self, expressionString, calculateResult=False):
    visualResult=None

    operand_1=None
    operand_2=None
    operator=None

    numericalResult=None

    try:
        operand_1, operand_2, operator = interpretExpression(expressionString)
    except ValueError:
        raise ValueError
    
    if(calculateResult):
        numericalResult=calculateExpression(operand_1, operand_2, operator)
    result=formatFinalExpression(operand_1, operand_2, operator, numericalResult)

    def interpretExpression(self, expressionString):
        pattern = r'^(\d{1,4}) ([+-]) (\d{1,4}$)'
        match = re.search(pattern, expressionString)

        if not match:
           raise ValueError()
        
        operand_1 = match.group(1)
        operand_2 = match.group(3)
        operator = match.group(2)

        return [operand_1, operand_2, operator]
    
    def formatFinalExpression(self, operand_1, operand_2, operator, numericalResult=None):
        result=[str(operand_1),str(operand_2),""]
        width = max(len(result[0]), len(result[1]))+2
        
        result[0]=result[0].rjust(width, ' ')
        result[1]=result[1].rjust(width-1, ' ')
        result[1]=result[1].rjust(width-1, operator)
        result[2]=result[2].rjust(width, '-')

        if(numericalResult is not None):
             result.append(str(numericalResult))
             result[3]=(operator+numericalResult).rjust(width)
        
        return result
        

    return visualResult


def calculateExpression(self, operand_1, operand_2, operator):
        result=None
        
        try:
            ints=[int(operand_1), int(operand_2)]
        except ValueError:
             raise ValueError

        if(operator=="+"):
             result=operand_1+operand_2
        elif(operator=="-"):
             result==operand_1-operand_2
        else:
             raise Exception()
        return result
             
             




