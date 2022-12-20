from typing import List

from rotom_cmp.semantics.ast import (
    Program,
    FnDefinition,
    BinaryExpr,
    Literal,
    DeclarationStmt,
    Variable,
    GroupingExpr,
    PrintStmt,
    FnCallExpr,
    TernaryExpr,
    BlockExpr,
    ConditionStmt,
    WhileStmt,
    AssignStmt,
    DispatchMethodExpr,
    DispatchVariableExpr,
    IndexOfExpr,
    UseStmt,
    ForStmt,
    ReturnStmt,
    ExprStmt,
    UnaryExpr,
)

from rotom_cmp.utils.visitor import Visitor


def list_to_str(list: list, breaks: int = 1):
    return ("\n" * breaks).join(list)


def make_expr_str_return(expr_str: str, tabs: int = 0):
    return "  " * tabs + f"return {expr_str};"


class JavascriptTranspiler(Visitor):
    """
    Converts a Rotom Program instance into js code
    """

    def __init__(self, root: Program) -> None:
        self.root = root

    def transpile(self) -> str:
        code = self.root.visit(self)

        # Execute main fn
        return list_to_str([code, "main();"], breaks=2)

    def visit_Program(self, node: Program):
        uses: List[str] = list_to_str([use.visit(self) for use in node.uses])
        fn_definitions: List[str] = list_to_str(
            [fn_def.visit(self) for fn_def in node.fn_definitions], breaks=2
        )

        code: List[str] = []
        if len(uses) > 0:
            code.append(uses)
        if len(fn_definitions) > 0:
            code.append(fn_definitions)

        return list_to_str(code, breaks=2)

    def visit_UseStmt(self, node: UseStmt, tabs: int = 0):
        if node.name is not None:
            return f"const {node.name} = require({node.module});"
        else:
            subnames = ", ".join(node.subnames)
            return f"const {{{ subnames }}} = require({node.module});"

    def visit_FnDefinition(self, node: FnDefinition, tabs: int = 0):
        params = ", ".join(node.params)

        stmts: List[str] = []
        for stmt in node.stmts:
            stmts.append(stmt.visit(self, tabs + 1))

        if node.is_inline:
            stmts[-1] = make_expr_str_return(stmts[-1], tabs + 1)

        body = list_to_str(stmts)

        code = list_to_str(
            [
                "  " * tabs + f"function {node.name}({params}) {{",
                body,
                "  " * tabs + "}",
            ]
        )

        return code

    def visit_Variable(self, node: Variable, tabs: int = 0):
        return node.name

    def visit_UnaryExpr(self, node: UnaryExpr, tabs: int = 0):
        return f"!({node.value.visit(self, tabs)})"

    def visit_BinaryExpr(self, node: BinaryExpr, tabs: int = 0):
        left = node.left.visit(self, tabs)
        right = node.right.visit(self, tabs)

        operators_map = {"==": "===", "and": "&&", "or": "||"}

        try:
            op = operators_map[node.operator]
        except KeyError:
            op = node.operator

        return f"{left} {op} {right}"

    def visit_Literal(self, node: Literal, tabs: int = 0):
        if node.type == "list" and isinstance(node.value, List):
            exprs: List[str] = []
            for val in node.value:
                if hasattr(val, "visit"):
                    exprs.append(val.visit(self, tabs))
                else:
                    exprs.append(val)

            return f"[{', '.join(exprs)}]"
        elif node.value == "nil":
            return "null"
        else:
            return f"{node.value}"

    def visit_DeclarationStmt(self, node: DeclarationStmt, tabs: int = 0):
        decl_keyword = "let" if node.is_mutable else "const"
        return (
            "  " * tabs
            + f"{decl_keyword} {node.name}"
            + (";" if node.value == "nil" else f" = {node.value.visit(self, tabs)};")
        )

    def visit_GroupingExpr(self, node: GroupingExpr, tabs: int = 0):
        value = node.value.visit(self)
        return "  " * tabs + f"({value})"

    def visit_PrintStmt(self, node: PrintStmt, tabs: int = 0):
        value = node.value.visit(self)
        if node.end_line:
            return "  " * tabs + f"console.log({value});"
        else:
            return "  " * tabs + f"process.stdout.write({value});"

    def visit_FnCallExpr(self, node: FnCallExpr, tabs: int = 0):
        fn_name = node.name_expr.visit(self, tabs)
        params = ", ".join([param.visit(self) for param in node.params])

        return f"{fn_name}({params})"

    def visit_TernaryExpr(self, node: TernaryExpr, tabs: int = 0):
        condition = node.condition.visit(self)
        true_branch = node.true_branch.visit(self)
        false_branch = node.false_branch.visit(self)

        return f"{condition} ? {true_branch} : {false_branch}"

    def visit_BlockExpr(self, node: BlockExpr, tabs: int = 0):
        stmts: List[str] = []
        for stmt in node.stmts:
            stmts.append(stmt.visit(self, tabs + 1))

        body = list_to_str(stmts)

        return list_to_str(["(() => {", body, "  " * tabs + "})()"])

    def visit_ConditionStmt(self, node: ConditionStmt, tabs: int = 0):
        condition = node.condition.visit(self, tabs)

        true_stmts: List[str] = []
        for stmt in node.true_branch:
            stmt_code = stmt.visit(self, tabs + 1)
            true_stmts.append(stmt_code)
        true_body = list_to_str(true_stmts)

        has_false_stmt = len(node.false_branch) > 0

        if has_false_stmt:
            false_stmts: List[str] = []
            for stmt in node.false_branch:
                stmt_code = stmt.visit(self, tabs + 1)
                false_stmts.append(stmt_code)
            false_body = list_to_str(false_stmts)

            return list_to_str(
                [
                    "  " * tabs + f"if ({condition}) {{",
                    true_body,
                    "  " * tabs + "} else {",
                    false_body,
                    "  " * tabs + "}",
                ]
            )
        else:
            return list_to_str(
                ["  " * tabs + f"if ({condition}) {{", true_body, "  " * tabs + "}"]
            )

    def visit_WhileStmt(self, node: WhileStmt, tabs: int = 0):
        condition = node.condition.visit(self, tabs)
        stmts = [stmt.visit(self, tabs + 1) for stmt in node.stmts]
        body = list_to_str(stmts)

        return list_to_str(
            ["  " * tabs + f"while ({condition}) {{", body, "  " * tabs + "}"]
        )

    def visit_AssignStmt(self, node: AssignStmt, tabs: int = 0):
        name = node.name.visit(self, tabs)
        expr = node.expr.visit(self, tabs)
        if node.is_indexed:
            indexes = (
                "[" + "][".join([idx.visit(self, tabs) for idx in node.indexes]) + "]"
            )
            return "  " * tabs + f"{name}{indexes} = {expr};"
        else:
            return "  " * tabs + f"{name} = {expr};"

    def visit_DispatchVariableExpr(self, node: DispatchVariableExpr, tabs: int = 0):
        expr = node.expr.visit(self, tabs)

        return f"{expr}.{node.name}"

    def visit_DispatchMethodExpr(self, node: DispatchMethodExpr, tabs: int = 0):
        expr = node.expr.visit(self, tabs)
        params = ", ".join([param.visit(self, tabs) for param in node.params])

        return f"{expr}.{node.name}({params})"

    def visit_IndexOfExpr(self, node: IndexOfExpr, tabs: int = 0):
        expr = node.expr.visit(self, tabs)
        pos = node.pos.visit(self, tabs)

        return f"{expr}[{pos}]"

    def visit_ForStmt(self, node: ForStmt, tabs: int = 0):
        body = list_to_str([stmt.visit(self, tabs + 1) for stmt in node.stmts])
        iterable = node.iterable.visit(self, tabs)

        if node.iterator_name is not None:
            return list_to_str(
                [
                    "  " * tabs
                    + f"for (const [{node.iterator_name}, {node.name}] of {iterable}.map((e, i) => [i, e])) {{",
                    body,
                    "  " * tabs + "}",
                ]
            )
        else:
            return list_to_str(
                [
                    "  " * tabs + f"for (const {node.name} of {iterable}) {{",
                    body,
                    "  " * tabs + "}",
                ]
            )

    def visit_ReturnStmt(self, node: ReturnStmt, tabs: int = 0):
        return "  " * tabs + f"return {node.expr.visit(self, tabs)};"

    def visit_ExprStmt(self, node: ExprStmt, tabs: int = 0):
        return "  " * tabs + f"{node.expr.visit(self, tabs)};"
