import sys
from faisallang.lexer import Lexer
from faisallang.parser import Parser
from faisallang.compiler import Compiler
from faisallang.vm import VM


def run_file(path):
    with open(path, "r", encoding="utf-8") as f:
        code = f.read()

    lexer = Lexer(code)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()

    compiler = Compiler()
    bytecode = compiler.compile(ast)

    vm = VM(bytecode)
    vm.run()


def repl():
    print("FaisalLang v10 REPL")

    while True:
        code = input(">>> ")

        if code.strip() == "خروج":
            break

        lexer = Lexer(code)
        tokens = lexer.tokenize()

        parser = Parser(tokens)
        ast = parser.parse()

        compiler = Compiler()
        bytecode = compiler.compile(ast)

        vm = VM(bytecode)
        vm.run()


def main():
    if len(sys.argv) > 1:
        run_file(sys.argv[1])
    else:
        repl()


if __name__ == "__main__":
    main()
