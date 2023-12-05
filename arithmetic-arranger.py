def arithmetic_aranger(self, expressions, displayResults):
    resultString=map(lambda x: True, expressions)
    return resultString

def process_expression(self, expressionString, calculateResult=False):
    operand_1=None
    operand_2=None
    operator=None

    numericalResult=None
    
    result=None

    try:
        result=validate_expression(expressionString)
    except Exception:
        raise Exception
    
    operand_1, operand_2, operator = interpret_expression
    if(calculateResult):
        numericalResult=calculate_expression(operand_1, operand_2, operator)
    result=format_final_expression(operand_1, operand_2, operator)

    def validate_expression(self, expressionString):
        return True

    def interpret_expression(self, expressionString):
        return True
    
    def format_final_expression(self, operand_1, operand_2, operator, numericalResult=None):
         return ""
    
    return result

def calculate_expression(self, operand_1, operand_2, operator):
        return True




