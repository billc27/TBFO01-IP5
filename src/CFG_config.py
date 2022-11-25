DEBUG = False

def read_grammar(nama_file):
    file = open(nama_file, "r")
    cfg = {}

    baris = file.readline()
    while baris != "":
        if (baris.startswith('##')):    # ignore comments
            pass
        else:
            # head, body = baris.replace("\n", "").split(" -> ")
            head, *tail = baris.replace("\n", "").split(" -> ")

            if(len(tail) != 0):
                body = tail[0]
                if head not in cfg.keys():
                    cfg[head] = [body.split(" ")]
                else:
                    cfg[head].append(body.split(" "))

        baris = file.readline()

    file.close()

    if DEBUG is True:
        print(cfg)
    
    return cfg

def isTerminal(string):
    list_of_terminal = [
        "STRING",
        "NUM",
        "NEWLINE",
        "LRB",
        "RRB",
        "LSB",
        "LCB",
        "RCB",
        "SEMICOLON",
        "COLON",
        "POWEQ",
        "POW",
        "MULEQ",
        "DIVEQ",
        "SUMEQ",
        "SUMAS NUM",
        "SUBEQ",
        "MODEQ",
        "ARROW",
        "ADD",
        "SUB",
        "MUL",
        "DIV",
        "MOD",
        "LEQ",
        "L",
        "GEQ",
        "G",
        "NEQ",
        "NEQEQ",
        "ISEQ",
        "ISEQEQ",
        "EQ",
        "FORMAT",
        "ANDBIT",
        "ORBIT",
        "NOTBIT",
        "XORBIT",
        "AND",
        "OR",
        "NOT",
        "IF",
        "ELSE",
        "FOR",
        "WHILE",
        "DO",
        "BREAK",
        "SWITCH",
        "CASE",
        "DEFAULT",
        "CONTINUE",
        "FALSE",
        "TRUE",
        "NONE",
        "IN",
        "CLASS",
        "RETURN",
        "IMPORT",
        "RAISE",
        "WITH",
        "AS",
        "TYPE",
        "TRY",
        "CATCH",
        "THROW",
        "FINALLY",
        "FUNCTION",
        "ID",
        "KARTITIK",
        "MULTILINE",
        "ERR",
        "TITIK",
        "DELETE",
        "COMMA",
        "THIS",
        "CONSTRUCTOR",
        "EOF"
    ]
    return string in list_of_terminal

def isNonTerminal(string):
    return not isTerminal(string)

# read_grammar("CFG.txt")