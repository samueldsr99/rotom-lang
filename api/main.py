from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from rotom_cmp.semantics.ast import Program
from rotom_cmp.parsing.parser import parser, errors
from rotom_cmp.codegen.js_transpiler import JavascriptTranspiler


class JSTranspilationRequest(BaseModel):
    rotom_code: str


app = FastAPI()


def make_transpilation(code: str):
    root: Program = parser.parse(code)

    if len(errors) > 0:
        return None, errors

    transpiler = JavascriptTranspiler(root)
    js_code = transpiler.transpile()

    return js_code, None


@app.get("/js/transpile")
async def transpile_js(item: JSTranspilationRequest):
    transpiled, errors = make_transpilation(item.rotom_code)

    if errors is not None:
        return JSONResponse({"errors": errors}, status_code=400)

    return {"result": transpiled}
