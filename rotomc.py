import os
from pathlib import Path
import argparse

from rotom_cmp.semantics.ast import Program
from rotom_cmp.parsing.parser import parser
from rotom_cmp.codegen.js_transpiler import JavascriptTranspiler

from transpile import transpile


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "file",
        type=argparse.FileType(mode="r", encoding="utf-8"),
        help="Source .rotom file",
    )
    arg_parser.add_argument(
        "--output_dir",
        type=str,
        help="Output directory of the transpiled file",
    )
    arg_parser.add_argument(
        "--verbose", type=bool, help="Verbosity of compilation process", default=False
    )

    args = arg_parser.parse_args()

    file = args.file.name
    verbose = args.verbose

    output_dir = args.output_dir or os.path.splitext(file)[0]
    transpiled_filepath = output_dir + ".js"

    js_code = transpile(file)

    with open(transpiled_filepath, "w") as fd:
        fd.write(js_code)

        if verbose:
            print("====================Transpiled====================")

    os.system(f"node {transpiled_filepath}")
