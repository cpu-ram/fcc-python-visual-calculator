import re
from functools import reduce


def arithmeticArranger(expressions, calculateResults=False):
    
    def processExpression(expressionString, calculateResult=False):
        def _interpretExpression(expressionString):
            pattern = r'^(\d{1,4}) ([+-]) (\d{1,4}$)'
            match = re.search(pattern, expressionString)

            if not match:
                expressionWithWrongOperationPattern = r'.+([*\/]).+'
                expressionWithNonDigitOperandsPattern = r'.*([^\d\+\- ]).*'
                expressionWIthMoreThanFourConsecutiveDigits = r'.*(\d{5,}).*'

                if(re.search(expressionWithWrongOperationPattern, expressionString)):
                    raise ValueError("Error: Operator must be '+' or '-'.")
                if(re.search(expressionWithNonDigitOperandsPattern, expressionString)):
                    raise ValueError("Error: Numbers must only contain digits.")
                if(re.search(expressionWIthMoreThanFourConsecutiveDigits, expressionString)):
                    raise ValueError("Error: Numbers cannot be more than four digits.")
                
                raise ValueError("Error: Unknown error.")
            
            operand_1 = match.group(1)
            operand_2 = match.group(3)
            operator = match.group(2)

            return [int(operand_1), int(operand_2), operator]


        def _formatFinalExpression(operand_1, operand_2, operator, numericalResult=None):
            result=[str(operand_1),str(operand_2),""]
            width = max(len(result[0]), len(result[1]))+2
            
            result[0]=result[0].rjust(width, ' ')
            result[1]=result[1].rjust(width-1, ' ')
            result[1]=result[1].rjust(width, operator)
            result[2]=result[2].rjust(width, '-')

            if(numericalResult is not None):
                result.append("")
                result[3]=(str(numericalResult)).rjust(width, ' ')
            
            return result

        visualResult=None

        operand_1=None
        operand_2=None
        operator=None

        numericalResult=None

        try:
            operand_1, operand_2, operator = _interpretExpression(expressionString)
        except ValueError as e:
            raise e
        
        if(calculateResult):
            numericalResult=calculateExpression(operand_1, operand_2, operator)
        visualResult=_formatFinalExpression(operand_1, operand_2, operator, numericalResult)

        return visualResult


    def calculateExpression(operand_1, operand_2, operator):
            result=None
            
            try:
                ints=[int(operand_1), int(operand_2)]
            except ValueError:
                raise ValueError

            if(operator=="+"):
                result=ints[0]+ints[1]
            elif(operator=="-"):
                result=ints[0]-ints[1]
            else:
                raise Exception()
            return result
                
    

    if(len(expressions)>5):
         return "Error: too many problems."


    resultStr=""
    try:
        superArr=list(map(lambda x: processExpression(x,calculateResults), expressions))
    except ValueError as e:
        return e
        
    for j in range(len(superArr[0])):
         for i in range(1, len(superArr)):
              superArr[0][j]+="    " + superArr[i][j]
    while(len(superArr)>1):
         superArr.pop()
    
    resultStr = reduce(lambda x,y: x+"\n"+y, superArr[0])

    return resultStr


resultStr=arithmeticArranger(["32 + 69898", "3801 - 2", "45 + 43", "123 + 49"], False)
print(resultStr)
print("")




