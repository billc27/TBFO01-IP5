from argparse import ArgumentParser
import tokenGenerator
import grammar
from CYK import CYK_validation

if __name__ == "__main__":
    argument_parser = ArgumentParser()
    argument_parser.add_argument("nama_file", type=str, help="Nama File...")

    args = argument_parser.parse_args()

    if CYK_validation(grammar.convert_CFG_to_CNF(grammar.read_grammar("CFG.txt")), tokenGenerator.tokenGenerator(args.nama_file)):
        print("ACCEPTED")
    else:
        print("SYNTAX ERROR")