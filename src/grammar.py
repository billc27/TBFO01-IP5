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

def convert_CFG_to_CNF(CFG):

    # Step 1: Add a new_pro production S' -> S if the start symbol S occurs on the right side
    list_head = list(CFG.keys())
    list_body = list(CFG.values())
    start_symbol = list_head[0]
    add_new_pro_rule = False

    for rules in list_body:
        for rule in rules:
            if start_symbol in rule:
                add_new_pro_rule = True
                break
        if add_new_pro_rule:
            break
    if add_new_pro_rule:
        new_pro_rule = {"START" : [[start_symbol]]}
        new_pro_rule.update(CFG)
        CFG = new_pro_rule

    # Step 2: Remove unit productions
    have_unit = True
    while have_unit:
        unit_productions = {}
        have_unit = False
        for head, body in CFG.items():
            for pro_rule in body:
                if len(pro_rule) == 1 and isNonTerminal(pro_rule[0]):
                    have_unit = True
                    if head not in unit_productions.keys():
                        unit_productions[head] = [[pro_rule[0]]]
                    else:
                        unit_productions[head].append([pro_rule[0]])

        # Unit productions are filled
        for head_unit, body_unit in unit_productions.items():
            for rule_unit in body_unit:
                for head, body in CFG.items():
                    if len(rule_unit) == 1 and head == rule_unit[0]:
                        new_pro_rule = {head_unit : body}
                        if head_unit not in CFG.keys():
                            CFG[head_unit] = body
                        else:
                            for rule in body:
                                if rule not in CFG[head_unit]:
                                    CFG[head_unit].append(rule)
    
        for head_unit, body_unit in unit_productions.items():
            for rule_unit in body_unit:
                if len(rule_unit) == 1:
                    CFG[head_unit].remove(rule_unit)

    # Step 3: Replace more than 2 non-terminals to 2 non-terminals only (e.g. A -> B0..Bk to A -> B0Z)
    new_pro = {}
    marked_for_deletion = {}
    i = 0
    for head, body in CFG.items():
        for rule in body:
            head_symbol = head
            temp_rule = [r for r in rule]
            if len(temp_rule) > 2:
                while len(temp_rule) > 2:
                    new_pro_symbol = f"X{i}"
                    if head_symbol not in new_pro.keys():
                        new_pro[head_symbol] = [[temp_rule[0], new_pro_symbol]]
                    else:
                        new_pro[head_symbol].append([temp_rule[0], new_pro_symbol])
                    head_symbol = new_pro_symbol
                    temp_rule.remove(temp_rule[0])
                    i += 1
                else:
                    if head_symbol not in new_pro.keys():
                        new_pro[head_symbol] = [temp_rule]
                    else:
                        new_pro[head_symbol].append(temp_rule)
                    
                    if head not in marked_for_deletion.keys():
                        marked_for_deletion[head] = [rule]
                    else:
                        marked_for_deletion[head].append(rule)

    for new_pro_head, new_pro_body in new_pro.items():
        if new_pro_head not in CFG.keys():
            CFG[new_pro_head] = new_pro_body
        else:
            CFG[new_pro_head].extend(new_pro_body)

    for del_head, del_body in marked_for_deletion.items():
        for del_rule in del_body:
            CFG[del_head].remove(del_rule)

    # STEP 4: Replace a terminal that is adjacent to a non terminal (e.g. A -> aB to A -> XB, X -> a)
    j = 0
    k = 0
    marked_for_deletion = {}
    new_pro = {}
    
    for head, body in CFG.items():
        for rule in body:
            if len(pro_rule) == 2 and isTerminal(rule[0]) and isTerminal(rule[1]):
                new_pro_symbol_Y = f"Y{j}"
                new_pro_symbol_Z = f"Z{k}"

                if head not in new_pro.keys():
                    new_pro[head] = [[new_pro_symbol_Y, new_pro_symbol_Z]]
                else:
                    new_pro[head].append([new_pro_symbol_Y, new_pro_symbol_Z])
                    
                new_pro[new_pro_symbol_Y] = [[rule[0]]]
                new_pro[new_pro_symbol_Z] = [[rule[1]]]

                if head not in marked_for_deletion.keys():
                    marked_for_deletion[head] = [rule]
                else:
                    marked_for_deletion[head].append(rule)
                j += 1
                k += 1

            elif len(rule) == 2 and isTerminal(rule[0]):
                new_pro_symbol_Y = f"Y{j}"

                if head not in new_pro.keys():
                    new_pro[head] = [[new_pro_symbol_Y, rule[1]]]
                else:
                    new_pro[head].append([new_pro_symbol_Y, rule[1]])

                new_pro[new_pro_symbol_Y] = [[rule[0]]]

                if head not in marked_for_deletion.keys():
                    marked_for_deletion[head] = [rule]
                else:
                    marked_for_deletion[head].append(rule)

                j += 1

            elif len(rule) == 2 and isTerminal(rule[1]):
                new_pro_symbol_Z = f"Z{k}"

                if head not in new_pro.keys():
                    new_pro[head] = [[rule[0], new_pro_symbol_Z]]
                else:
                    new_pro[head].append([rule[0], new_pro_symbol_Z])

                new_pro[new_pro_symbol_Z] = [[rule[1]]]

                if head not in marked_for_deletion.keys():
                    marked_for_deletion[head] = [rule]
                else:
                    marked_for_deletion[head].append(rule)

                k += 1

            else:
                pass

    for new_pro_head, new_pro_body in new_pro.items():
        if new_pro_head not in CFG.keys():
            CFG[new_pro_head] = new_pro_body
        else:
            CFG[new_pro_head].extend(new_pro_body)

    for del_head, del_body in marked_for_deletion.items():
        for del_rule in del_body:
            CFG[del_head].remove(del_rule)

    return CFG