import argparse

from rotom_cmp.semantics.ast import Program
from rotom_cmp.parsing.parser import parser, errors
from rotom_cmp.codegen.js_transpiler import JavascriptTranspiler


def transpile(filename: str):
    with open(filename, mode="r", encoding="utf-8") as fd:
        code = fd.read()

        root: Program = parser.parse(code)
        if len(errors) > 0:
            return None, errors

        transpiler = JavascriptTranspiler(root)
        js_code = transpiler.transpile()
        return js_code, None


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "filename",
        type=argparse.FileType(mode="r", encoding="utf-8"),
        help="Source .rotom file",
    )

    args = arg_parser.parse_args()

    filename = args.filename.name

    js_code = transpile(filename)

    print("====================Transpiled====================")
    print(js_code)
