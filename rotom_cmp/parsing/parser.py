import ply.yacc as yacc

from typing import List

from rotom_cmp.lexing import lexer
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
    TypeDefinitionStmt,
)


tokens = lexer.tokens


precedence = (
    ("right", "EQUAL"),
    ("right", "NOT"),
    (
        "nonassoc",
        "LESS",
        "LESS_EQUAL",
        "GREATER",
        "GREATER_EQUAL",
        "EQUAL_EQUAL",
        "BANG_EQUAL",
        "AND",
        "OR",
    ),
    ("left", "PLUS", "MINUS", "STAR", "SLASH"),
)


def p_prog(p):
    """
    prog : use_list type_def fn_def_list
    """
    p[0] = Program(uses=p[1], fn_definitions=p[3])


def p_use_list(p):
    """
    use_list : use use_list
             | use
             | empty
    """
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        if p[1] is not None:
            p[0] = [p[1]]
        else:
            p[0] = []


def p_use(p):
    """
    use : USE STRING ARROW IDENTIFIER SEMICOLON
        | USE STRING ARROW LEFT_PAREN param_list RIGHT_PAREN SEMICOLON
    """
    if len(p) == 6:
        p[0] = UseStmt(module=p[2], name=p[4])
    else:
        p[0] = UseStmt(module=p[2], subnames=p[5])


def p_fn_def_list(p):
    """
    fn_def_list : fn_def fn_def_list
                | fn_def
    """
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]


def p_fn_def(p):
    """
    fn_def : FN IDENTIFIER LEFT_PAREN param_list RIGHT_PAREN LEFT_BRACE stmt_list RIGHT_BRACE
           | FN IDENTIFIER LEFT_PAREN param_list RIGHT_PAREN ARROW expr
    """
    if len(p) == 9:
        p[0] = FnDefinition(name=p[2], params=p[4], stmts=p[7])
    else:
        p[0] = FnDefinition(name=p[2], params=p[4], stmts=[p[7]], is_inline=True)


def p_param_list(p):
    """
    param_list : IDENTIFIER COMMA param_list
               | IDENTIFIER
               | empty
    """
    if len(p) == 4:
        p[0] = [p[1]] + p[3]
    elif len(p) == 2:
        if p[1] is None:
            p[0] = []
        else:
            p[0] = [p[1]]


def p_stmt_list(p):
    """
    stmt_list : stmt stmt_list
              | stmt
    """
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]


def p_stmt(p):
    """
    stmt : expr SEMICOLON
         | declaration
         | assign
         | print
         | condition
         | while
         | for
         | return
    """
    if len(p) == 3:
        p[0] = ExprStmt(expr=p[1])
    else:
        p[0] = p[1]


def p_type_def(p):
    """
    type_def : TYPE IDENTIFIER LEFT_BRACE prop_list RIGHT_BRACE
    """
    p[0] = TypeDefinitionStmt(name=p[2], properties=p[4], methods=[])


def p_property_list(p):
    """
    prop_list : IDENTIFIER COMMA prop_list
              | IDENTIFIER COMMA
              | IDENTIFIER
    """
    if len(p) == 4:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = [p[1]]


def p_return(p):
    """
    return : RETURN expr SEMICOLON
    """
    p[0] = ReturnStmt(expr=p[2])


def p_for(p):
    """
    for : FOR IDENTIFIER IN expr LEFT_BRACE stmt_list RIGHT_BRACE
        | FOR IDENTIFIER COMMA IDENTIFIER IN expr LEFT_BRACE stmt_list RIGHT_BRACE
    """
    if len(p) == 8:
        p[0] = ForStmt(name=p[2], iterable=p[4], stmts=p[6])
    else:
        p[0] = ForStmt(name=p[4], iterable=p[6], stmts=p[8], iterator_name=p[2])


def p_while(p):
    """
    while : WHILE expr LEFT_BRACE stmt_list RIGHT_BRACE
    """
    p[0] = WhileStmt(condition=p[2], stmts=p[4])


def p_condition(p):
    """
    condition : IF expr LEFT_BRACE stmt_list RIGHT_BRACE
              | IF expr LEFT_BRACE stmt_list RIGHT_BRACE ELSE LEFT_BRACE stmt_list RIGHT_BRACE
    """
    if len(p) == 6:
        p[0] = ConditionStmt(condition=p[2], true_branch=p[4])
    else:
        p[0] = ConditionStmt(condition=p[2], true_branch=p[4], false_branch=p[8])


def p_print(p):
    """
    print : PRINT expr SEMICOLON
          | PRINTLN expr SEMICOLON
    """
    end_line = p[1] == "print"
    p[0] = PrintStmt(p[2], end_line=end_line)


def p_expr_unary(p):
    """
    expr : NOT expr
    """
    p[0] = UnaryExpr(value=p[2])


def p_expr_binary(p):
    """
    expr : expr PLUS expr
         | expr MINUS expr
         | expr STAR expr
         | expr SLASH expr
         | expr LESS expr
         | expr LESS_EQUAL expr
         | expr GREATER expr
         | expr GREATER_EQUAL expr
         | expr EQUAL_EQUAL expr
         | expr BANG_EQUAL expr
         | expr OR expr
         | expr AND expr
    """
    p[0] = BinaryExpr(p[1], p[2], p[3])


def p_expr_grouping(p):
    """
    expr : LEFT_PAREN expr RIGHT_PAREN
    """
    p[0] = GroupingExpr(p[2])


def p_expr_literal(p):
    """
    expr : NUMBER
         | NIL
         | STRING
         | LEFT_BRACKET expr_list_comma RIGHT_BRACKET
    """
    if len(p) == 4:
        p[0] = Literal(p[2], type="list")
    else:
        if isinstance(p[1], int) or isinstance(p[1], float):
            type_ = "number"
        elif p[1] is None:
            type_ = "nil"
        elif isinstance(p[1], str):
            type_ = "string"
        p[0] = Literal(p[1], type=type_)


def p_expr_dispatch(p):
    """
    expr : expr DOT IDENTIFIER
         | expr DOT IDENTIFIER LEFT_PAREN expr_list_comma RIGHT_PAREN
    """
    if len(p) == 4:
        p[0] = DispatchVariableExpr(expr=p[1], name=p[3])
    else:
        p[0] = DispatchMethodExpr(expr=p[1], name=p[3], params=p[5])


def p_expr_indexof(p):
    """
    expr : expr LEFT_BRACKET expr RIGHT_BRACKET
    """
    p[0] = IndexOfExpr(expr=p[1], pos=p[3])


def p_expr_fn_call(p):
    """
    expr : expr LEFT_PAREN expr_list_comma RIGHT_PAREN
    """
    p[0] = FnCallExpr(name_expr=p[1], params=p[3])


def p_expr_list_comma(p):
    """
    expr_list_comma : expr COMMA expr_list_comma
                 | expr
                 | empty
    """
    if len(p) == 4:
        p[0] = [p[1]] + p[3]
    elif len(p) == 2:
        if p[1] is None:
            p[0] = []
        else:
            p[0] = [p[1]]


def p_expr_variable(p):
    """
    expr : IDENTIFIER
    """
    p[0] = Variable(name=p[1])


def p_expr_ternary(p):
    """
    expr : expr IF expr ELSE expr
    """
    p[0] = TernaryExpr(condition=p[3], true_branch=p[1], false_branch=p[5])


def p_expr_block(p):
    """
    expr : LEFT_BRACE stmt_list RIGHT_BRACE
    """
    p[0] = BlockExpr(p[2])


def p_indexof_list(p):
    """
    indexof_list : LEFT_BRACKET expr RIGHT_BRACKET
                 | LEFT_BRACKET expr RIGHT_BRACKET indexof_list
    """
    if len(p) == 4:
        p[0] = [p[2]]
    else:
        p[0] = [p[2]] + p[4]


def p_declaration(p):
    """
    declaration : LET IDENTIFIER EQUAL expr SEMICOLON
                | LET MUT IDENTIFIER EQUAL expr SEMICOLON
                | LET IDENTIFIER SEMICOLON
                | LET MUT IDENTIFIER SEMICOLON
    """
    if len(p) == 6:
        p[0] = DeclarationStmt(p[2], p[4])
    elif len(p) == 7:
        p[0] = DeclarationStmt(p[3], p[5], is_mutable=True)
    elif len(p) == 4:
        p[0] = DeclarationStmt(p[2], "nil")
    elif len(p) == 5:
        p[0] = DeclarationStmt(p[3], "nil", is_mutable=True)


def p_assign(p):
    """
    assign : expr EQUAL expr SEMICOLON
           | expr indexof_list EQUAL expr SEMICOLON
    """
    if len(p) == 5:
        p[0] = AssignStmt(name=p[1], expr=p[3])
    else:
        p[0] = AssignStmt(name=p[1], expr=p[4], is_indexed=True, indexes=p[2])


def p_empty(p):
    """
    empty :
    """
    pass


def p_error(p):
    errors.append(f'(line={p.lineno}): Syntax error on input: "{p.value}"')


errors: List[str] = []
parser = yacc.yacc(debug=True)
