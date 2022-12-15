from abc import ABCMeta
from typing import List

from rotom_cmp.utils.visitor import Visitor


class Node(metaclass=ABCMeta):
    def visit(self, visitor: Visitor):
        pass


class Stmt(Node):
    pass


class Expr(Node):
    pass


class FnDefinition(Node):
    def __init__(self, name: str, params: List[str], stmts: List[Stmt]) -> None:
        self.name = name
        self.params = params
        self.stmts = stmts

    def visit(self, visitor: Visitor, *args):
        return visitor.visit_FnDefinition(self, *args)

    def __repr__(self) -> str:
        params = ",".join(self.params)
        return f"{self.name}({params})"


class Program(Node):
    def __init__(self, fn_definitions: List[FnDefinition]) -> None:
        self.fn_definitions = fn_definitions

    def visit(self, visitor: Visitor, *args):
        return visitor.visit_Program(self, *args)

    def __repr__(self) -> str:
        return f"Program:\n{self.fn_definitions}"


class DeclarationStmt(Stmt):
    def __init__(self, name: str, value: Expr, is_mutable: bool = False) -> None:
        self.name = name
        self.value = value
        self.is_mutable = is_mutable

    def visit(self, visitor: Visitor, *args):
        return visitor.visit_DeclarationStmt(self, *args)


class BinaryExpr(Expr):
    def __init__(self, left: Expr, operator: str, right: Expr) -> None:
        self.left = left
        self.operator = operator
        self.right = right

    def visit(self, visitor: Visitor, *args):
        return visitor.visit_BinaryExpr(self, *args)


class GroupingExpr(Expr):
    def __init__(self, value: Expr) -> None:
        self.value = value

    def visit(self, visitor: Visitor, *args):
        return visitor.visit_GroupingExpr(self, *args)


class Literal(Expr):
    def __init__(self, value: object, type: str) -> None:
        self.value = value
        self.type = type

    def visit(self, visitor: Visitor, *args):
        return visitor.visit_Literal(self, *args)

    def __repr__(self) -> str:
        return f"{self.value}"


class Variable(Node):
    def __init__(self, name: str) -> None:
        self.name = name

    def visit(self, visitor: Visitor, *args):
        return visitor.visit_Variable(self, *args)

    def __repr__(self) -> str:
        return f"Variable({self.name})"


class PrintStmt(Stmt):
    def __init__(self, value: Expr, end_line: bool = False) -> None:
        self.value = value
        self.end_line = end_line

    def visit(self, visitor: Visitor, *args):
        return visitor.visit_PrintStmt(self, *args)


class FnCallExpr(Expr):
    def __init__(self, name: str, params: List[Expr]) -> None:
        self.name = name
        self.params = params

    def visit(self, visitor: Visitor, *args):
        return visitor.visit_FnCallExpr(self, *args)


class TernaryExpr(Expr):
    def __init__(self, condition: Expr, true_branch: Expr, false_branch: Expr) -> None:
        self.condition = condition
        self.true_branch = true_branch
        self.false_branch = false_branch

    def visit(self, visitor: Visitor, *args):
        return visitor.visit_TernaryExpr(self, *args)


class BlockExpr(Expr):
    def __init__(self, stmts: List[Expr]) -> None:
        self.stmts = stmts

    def visit(self, visitor: Visitor, *args):
        return visitor.visit_BlockExpr(self, *args)


class ConditionStmt(Stmt):
    def __init__(
        self, condition: Expr, true_branch: List[Expr], false_branch: List[Expr] = []
    ) -> None:
        self.condition = condition
        self.true_branch = true_branch
        self.false_branch = false_branch

    def visit(self, visitor: Visitor, *args):
        return visitor.visit_ConditionStmt(self, *args)


class WhileStmt(Stmt):
    def __init__(self, condition: Expr, stmts: List[Stmt]) -> None:
        self.condition = condition
        self.stmts = stmts

    def visit(self, visitor: Visitor, *args):
        return visitor.visit_WhileStmt(self, *args)


class AssignStmt(Stmt):
    def __init__(self, name: str, expr: Expr) -> None:
        self.name = name
        self.expr = expr

    def visit(self, visitor: Visitor, *args):
        return visitor.visit_AssignStmt(self, *args)
