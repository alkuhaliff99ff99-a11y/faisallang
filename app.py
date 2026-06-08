from compiler.lexer import Lexer
from compiler.parser import Parser
from compiler.interpreter import Interpreter


def run_faisal_lang(code):

    lexer = Lexer(code)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()

    interpreter = Interpreter(ast)
    interpreter.run()
