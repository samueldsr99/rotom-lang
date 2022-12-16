from ply.lex import LexToken, TOKEN
import ply.lex as lex
from ply.yacc import yacc

from .tokens import TokenType

reserved = {
    "and": TokenType.AND,
    "class": TokenType.CLASS,
    "else": TokenType.ELSE,
    "false": TokenType.FALSE,
    "for": TokenType.FOR,
    "fn": TokenType.FN,
    "if": TokenType.IF,
    "nil": TokenType.NIL,
    "or": TokenType.OR,
    "print": TokenType.PRINT,
    "println": TokenType.PRINTLN,
    "return": TokenType.RETURN,
    "super": TokenType.SUPER,
    "this": TokenType.THIS,
    "true": TokenType.TRUE,
    "let": TokenType.LET,
    "mut": TokenType.MUT,
    "while": TokenType.WHILE,
    "use": TokenType.USE,
}


tokens = [
    # Single character
    TokenType.LEFT_PAREN,
    TokenType.RIGHT_PAREN,
    TokenType.LEFT_BRACE,
    TokenType.RIGHT_BRACE,
    TokenType.LEFT_BRACKET,
    TokenType.RIGHT_BRACKET,
    TokenType.COMMA,
    TokenType.DOT,
    TokenType.MINUS,
    TokenType.PLUS,
    TokenType.SEMICOLON,
    TokenType.SLASH,
    TokenType.STAR,
    TokenType.ARROW,
    # One or two characters
    TokenType.BANG,
    TokenType.BANG_EQUAL,
    TokenType.EQUAL,
    TokenType.EQUAL_EQUAL,
    TokenType.GREATER,
    TokenType.GREATER_EQUAL,
    TokenType.LESS,
    TokenType.LESS_EQUAL,
    # Literals
    TokenType.IDENTIFIER,
    TokenType.STRING,
    TokenType.NUMBER,
    # Keywords
    TokenType.AND,
    TokenType.CLASS,
    TokenType.ELSE,
    TokenType.FALSE,
    TokenType.FN,
    TokenType.FOR,
    TokenType.IF,
    TokenType.NIL,
    TokenType.OR,
    TokenType.PRINT,
    TokenType.PRINTLN,
    TokenType.RETURN,
    TokenType.SUPER,
    TokenType.THIS,
    TokenType.TRUE,
    TokenType.LET,
    TokenType.MUT,
    TokenType.WHILE,
    TokenType.USE,
    # EOF
    TokenType.EOF,
]

t_LEFT_PAREN = r"\("
t_RIGHT_PAREN = r"\)"
t_LEFT_BRACE = r"\{"
t_RIGHT_BRACE = r"\}"
t_LEFT_BRACKET = r"\["
t_RIGHT_BRACKET = r"\]"
t_COMMA = r"\,"
t_DOT = r"\."
t_MINUS = r"\-"
t_PLUS = r"\+"
t_SEMICOLON = r"\;"
t_SLASH = r"\/"
t_STAR = r"\*"
t_ARROW = r"\-\>"

t_BANG = r"\!"
t_BANG_EQUAL = r"\!\="
t_EQUAL = r"\="
t_EQUAL_EQUAL = r"\=\="
t_GREATER = r"\>"
t_GREATER_EQUAL = r"\>\="
t_LESS = r"\<"
t_LESS_EQUAL = r"\<\="


def t_NUMBER(t: LexToken) -> LexToken:
    r"\d+"
    t.value = int(t.value)
    return t


# String literal
def t_STRING(t: LexToken) -> LexToken:
    r"\"([^\\\n]|(\\(.|\n)))*?\" "
    t.lexer.lineno += t.value.count("\n")
    return t


def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reserved.get(t.value, TokenType.IDENTIFIER)  # Check for reserved words
    return t


t_ignore = " \t\f\r"
t_ignore_comment = r"\/\/[^\n]*"


def t_newline(t: LexToken) -> LexToken:
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t: LexToken) -> LexToken:
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
