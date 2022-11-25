arith_op = ["+","-","*","/"]
input_exp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y"
            "z", "_", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbol = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "{", "}", "[", "]", "|", "\\", ":", ";", "\"", "'", "?", "="]
capital = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
            "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
            "Y", "Z"]
transition_exp = {}

# Variabel Valid di Awal
for i in input_exp:
    transition_exp[("q0", i)] = "q1"

# Operator Matematika di Awal
for i in arith_op:
    transition_exp[("q0", i)] = "qd"

# Huruf Kapital di Awal
for i in capital:
    transition_exp[("q0", i)] = "qd"

# Simbol di Awal
for i in symbol:
    transition_exp[("q0", i)] = "qd"

# Variabel Valid
for i in input_exp:
    transition_exp[("q1", i)] = "q1"

# Operator Matematika
for i in arith_op:
    transition_exp[("q1", i)] = "q2"

# Huruf Kapital
for i in capital:
    transition_exp[("q1", i)] = "q1"

# Simbol
for i in symbol:
    transition_exp[("q1", i)] = "qd"

# Variabel Valid
for i in input_exp:
    transition_exp[("q2", i)] = "q3"

# Operator Matematika
for i in arith_op:
    transition_exp[("q2", i)] = "qd"

# Huruf Kapital
for i in capital:
    transition_exp[("q2", i)] = "qd"

# Simbol
for i in symbol:
    transition_exp[("q2", i)] = "qd"

# Variabel Valid
for i in input_exp:
    transition_exp[("q3", i)] = "q3"

# Operator Matematika
for i in arith_op:
    transition_exp[("q3", i)] = "q2"

# Huruf Kapital
for i in capital:
    transition_exp[("q3", i)] = "qd"

# Simbol
for i in symbol:
    transition_exp[("q3", i)] = "qd"

# Penanganan Dead State
# Variabel Valid
for i in input_exp:
    transition_exp[("qd", i)] = "qd"

# Operator Matematika
for i in arith_op:
    transition_exp[("qd", i)] = "qd"

# Huruf Kapital
for i in capital:
    transition_exp[("qd", i)] = "qd"

# Simbol
for i in symbol:
    transition_exp[("qd", i)] = "qd"

# Test Expression
def isValidExpression(expression):
    valid_expression = False
    current_state_exp = "q0"
    for i in expression:
        current_state_exp = transition_exp[(current_state_exp, i)]
        if (current_state_exp == "q3"):
            valid_expression = True
        else:
            valid_expression = False
    return valid_expression