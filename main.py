from rotom_cmp.lexing import lexer
from rotom_cmp.parsing.parser import parser
from rotom_cmp.semantics.ast import Program

from rotom_cmp.codegen.js_transpiler import JavascriptTranspiler


if __name__ == "__main__":
    with open("./example/code/sum.rotom") as fd:
        data = fd.read()
        print(data)
        # lexer.input(data)

        root: Program = parser.parse(data)

        transpiler = JavascriptTranspiler(root)

        js = transpiler.transpile()

        print("====================== TRANSPILED ===================")
        print(js)
