import re
import sys

tokenData = [
    # None
    (r'[ \t]+',                                      None),
    (r'\/\/[^\n]*',                                  None),
    (r'\/\*[^*/]*\*\/',                              None),

    # Number and String
    (r'\"[^\"\n]*\"',           "STRING"),
    (r'\'[^\'\n]*\'',           "STRING"),
    (r'[\+\-]?[0-9]*\.[0-9]+',  "NUM"),
    (r'[\+\-]?[1-9][0-9]+',     "NUM"),
    (r'[\+\-]?[0-9]',           "NUM"),

    # Uniq char
    (r'\n',                     "NEWLINE"),
    (r'\(',                     "LRB"), 
    (r'\)',                     "RRB"),
    (r'\[',                     "LSB"), 
    (r'\]',                     "RSB"),
    (r'\{',                     "LCB"),
    (r'\}',                     "RCB"),
    (r'\;',                     "SEMICOLON"), 
    (r'\:',                     "COLON"),
    (r'\,',                     "COMMA"),
    (r'\w+[.]\w+',              "KARTITIK"),
    (r'\.',                     "TITIK"),

    # Operator
    (r'\*\*=',                  "POWEQ"),
    (r'\*\*',                   "POW"),
    (r'\*=',                    "MULEQ"),
    (r'/=',                     "DIVEQ"),
    (r'\+=',                    "SUMEQ"),
    (r'\++',                    "SUMEQ NUM"),
    (r'\--',                    "SUBEQ NUM"),
    (r'\-=',                    "SUBEQ"),
    (r'\%=',                    "MODEQ"),
    (r'\=>',                    "ARROW"),
    (r'\+',                     "ADD"),
    (r'\-',                     "SUB"),
    (r'\*',                     "MUL"),
    (r'/',                      "DIV"),
    (r'%',                      "MOD"),
    (r'<=',                     "LEQ"),
    (r'<',                      "L"),
    (r'>=',                     "GEQ"),
    (r'>',                      "G"),
    (r'!==',                     "NEQEQ"),
    (r'!(?!\=)(?!\=)',                     "NOT"),
    (r'\!=(?!\=)',                     "NEQ"),
    (r'\!\==',                     "NEQEQ"),
    (r'!',                      "NOT"),
    (r'\===',                    "ISEQEQ"),
    (r'\==(?!\=)',                    "ISEQ"),
    (r'\=\==',                    "ISEQEQ"),
    (r'(?!\!)\=(?!\=)',                     "EQ"),
    (r'\|\|',               "OR"),
    (r'!',                  "NOT"),
    (r'&&',                 "AND"),

    # Keyword
    (r'\bformat\b',             "FORMAT"),
    (r'&&',                 "AND"),
    (r'\&(?!\&)',                 "AND"),
    (r'\|\|',               "OR"),
    (r'\|(?!\|)',                 "AND"),
    (r'\b!\b',                  "NOT"),
    (r'\~',                 "NOTBIT"),
    (r'\^',                 "XORBIT"),
    (r'\bif\b',                 "IF"),
    (r'\belse\b',               "ELSE"),
    (r'\bfor\b',                "FOR"),
    (r'\bwhile\b',              "WHILE"),
    (r'\bdo\b',                 "DO"),
    (r'\bswitch\b',             "SWITCH"),
    (r'\bcase\b',               "CASE"),
    (r'\bdefault\b',            "DEFAULT"),
    (r'\bbreak\b',              "BREAK"),
    (r'\bcontinue\b',           "CONTINUE"),
    (r'\bfalse\b',              "FALSE"),
    (r'\btrue\b',               "TRUE"),
    (r'\bNone\b',               "NONE"),
    (r'\breturn\b',             "RETURN"),
    (r'\bvar\b',                "TYPE"),
    (r'\blet\b',                "TYPE"),
    (r'\bconst\b',              "TYPE"),
    (r'\btry\b',                "TRY"),
    (r'\bcatch\b',              "CATCH"),
    (r'\bthrow\b',              "THROW"),
    (r'\bfinally\b',            "FINALLY"),
    (r'\berr\b',                "ERR"),
    (r'\bdelete\b',             "DELETE"),
    (r'\bfunction\b',           "FUNCTION"),
    (r'\bconstructor\b',        "CONSTRUCTOR"),
    (r'[A-Za-z_][A-Za-z0-9_]*', "ID"),
]

def lexer(text, tokenData):
    pos = 0
    regexs = []
    tokens = []
    lengthText = len(text)

    for x in tokenData:
        pattern, code = x
        regex = re.compile(pattern)
        regexs.append((regex, code))

    while(pos < lengthText):
        if text[pos] == " ":
            pos += 1

        for regex in regexs:
            reg, code = regex
            isMatch = reg.match(text, pos)

            if isMatch:
                tokens.append(code)
                break
        
        if isMatch:
            pos = isMatch.end(0)
        else:
            print("Error")
            break

    return tokens

def create_token(tesFile):
    file = open(tesFile)
    char = file.read()
    file.close()

    print(char)

    tokens = lexer(char,tokenData)

    print(tokens)

    return " ".join(tokens)