from abc import ABCMeta


class Visitor(metaclass=ABCMeta):
    def visit_Program(self, node, *args):
        pass

    def visit_BinaryExpr(self, node, *args):
        pass

    def visit_FnDefinition(self, node, *args):
        pass

    def visit_Variable(self, node, *args):
        pass

    def visit_DeclarationStmt(self, node, *args):
        pass

    def visit_Literal(self, node, *args):
        pass

    def visit_GroupingExpr(self, node, *args):
        pass

    def visit_PrintStmt(self, node, *args):
        pass

    def visit_FnCallExpr(self, node, *args):
        pass

    def visit_TernaryExpr(self, node, *args):
        pass

    def visit_BlockExpr(self, node, *args):
        pass

    def visit_ConditionStmt(self, node, *args):
        pass

    def visit_WhileStmt(self, node, *args):
        pass

    def visit_AssignStmt(self, node, *args):
        pass

    def visit_DispatchVariableExpr(self, node, *args):
        pass

    def visit_DispatchMethodExpr(self, node, *args):
        pass

    def visit_IndexOfExpr(self, node, *args):
        pass

    def visit_UseStmt(self, node, *args):
        pass

    def visit_ForStmt(self, node, *args):
        pass

    def visit_ReturnStmt(self, node, *args):
        pass
