import os
import argparse

from rotom_cmp.semantics.ast import Program
from rotom_cmp.parsing.parser import parser
from rotom_cmp.codegen.js_transpiler import JavascriptTranspiler
from rotom_cmp.utils.rich_logger import RichLogger

from transpile import transpile


def build_arg_parser():
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
        "--verbosity", type=int, default=1, help="Handle verbosity levels (0 or 1)"
    )

    return arg_parser


if __name__ == "__main__":
    arg_parser = build_arg_parser()
    args = arg_parser.parse_args()

    file = args.file.name
    verbosity = args.verbosity

    output_dir = args.output_dir or os.path.splitext(file)[0]
    transpiled_filepath = output_dir + ".js"

    logger = RichLogger()

    if verbosity:
        logger.log_info("1/2 Transpiling...", bold=True)

    js_code, errors = transpile(file)
    if errors:
        logger.log_error(f"Errors found: {len(errors)}", bold=True)
        for error in errors:
            logger.log_error("    - " + error)
    else:
        if verbosity:
            logger.log_success("1/2 Transpilation succeded", bold=True)
            logger.log_info("2/2 Writing js file...", bold=True)

        with open(transpiled_filepath, "w") as fd:
            fd.write(js_code)
            if verbosity:
                logger.log_success("2/2 🥳 Finished!!!\n", bold=True)

        os.system(f"node {transpiled_filepath}")
