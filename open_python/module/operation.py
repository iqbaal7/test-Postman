def sum(left_param, right_param):
    return left_param + right_param

def substraction(left_param, right_param):
    return left_param - right_param

def multiplication(left_param, right_param):
    return left_param * right_param

def division(left_param, right_param):
    try:
        return left_param / right_param
    except ZeroDivisionError:
        print("Erreur : Division par zéro !")