def basic_calc(a, b, op):
    if a.isnumeric() & b.isnumeric():
        a = float(a)
        b = float(b)
        if op == "add":
            res = a + b
        elif op == "substract":
            res = a - b
        elif op == "divide":
            res = a / b
        elif op == "multiply":
            res = a * b
        else:
            res = "Operations supported: add, substract, divide, multiply"

    else:
        res = "Please enter a valid n for a & b"
    return res
