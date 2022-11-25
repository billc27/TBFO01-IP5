import re

tokenData = [
    (r'[ \t]+',                                      None),
    (r'\/\/[^\n]*',                                  None),
    (r'\/\*[^*/]*\*\/',                              None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),

    # Number and String
    (r'\"[^\"\n]*\"',           "STRING"),
    (r'\'[^\'\n]*\'',           "STRING"),
    (r'[\+\-]?[0-9]*\.[0-9]+',  "NUM"),
    (r'[\+\-]?[1-9][0-9]+',     "NUM"),
    (r'[\+\-]?[0-9]',           "NUM"),

    # Delimiter
    (r'\n',                     "NEWLINE"),
    (r'\(',                     "LRB"), 
    (r'\)',                     "RRB"),
    (r'\[',                     "LSB"), 
    (r'\]',                     "RSB"),
    (r'\{',                     "LCB"),
    (r'\}',                     "RCB"),
    (r'\;',                     "SEMICOLON"), 
    (r'\:',                     "COLON"),

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
    (r'!=',                     "NEQ"),
    (r'\==',                    "ISEQ"),
    (r'\=(?!\=)',               "EQ"),

    # Keyword
    (r'\bformat\b',             "FORMAT"),
    (r'\b&&\b',                 "AND"),
    (r'\b\|\|\b',               "OR"),
    (r'\b!\b',                  "NOT"),
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
    (r'\bin\b',                 "IN"),
    (r'\bclass\b',              "CLASS"),
    (r'\breturn\b',             "RETURN"),
    (r'\bimport\b',             "IMPORT"),
    (r'\braise\b',              "RAISE"),
    (r'\bwith\b',               "WITH"),
    (r'\bas\b',                 "AS"),
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
    (r'\bthis\b',               "THIS"),
    (r'\,',                     "COMMA"),
    (r'[A-Za-z_][A-Za-z0-9_]*', "ID"),
    (r'\w+[.]\w+',              "KARTITIK"),
    (r'\.',                     "TITIK"),
    (r'\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',       "MULTILINE"),
    (r'\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',       "MULTILINE"),
]

def lexer(stringInput, token_exp):
    pos = 0
    cur = 1 # character position relative to row
    line = 1 # current row position
    tokens = []
    while pos < len(stringInput):
        if stringInput[pos] == '\n':
            cur = 1
            line += 1
        match = None

        for t in token_exp:
            pattern, tag = t
            regex = re.compile(pattern)
            match = regex.match(stringInput, pos)
            if match:
                if tag:
                    token = tag
                    tokens.append(token)
                break

        pos = match.end(0)
        cur += 1
    return tokens

def create_token(sentence):
    file = open(sentence)
    char = file.read()
    file.close()

    print(char)

    tokens = " ".join(lexer(char,tokenData))

    return tokens