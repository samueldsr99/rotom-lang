class TokenType:
    # Single character
    LEFT_PAREN = "LEFT_PAREN"
    RIGHT_PAREN = "RIGHT_PAREN"
    LEFT_BRACE = "LEFT_BRACE"
    RIGHT_BRACE = "RIGHT_BRACE"
    LEFT_BRACKET = "LEFT_BRACKET"
    RIGHT_BRACKET = "RIGHT_BRACKET"
    COMMA = "COMMA"
    DOT = "DOT"
    MINUS = "MINUS"
    PLUS = "PLUS"
    SEMICOLON = "SEMICOLON"
    SLASH = "SLASH"
    STAR = "STAR"
    COLON = "COLON"

    # One or two characters
    BANG = "BANG"
    BANG_EQUAL = "BANG_EQUAL"
    EQUAL = "EQUAL"
    EQUAL_EQUAL = "EQUAL_EQUAL"
    GREATER = "GREATER"
    GREATER_EQUAL = "GREATER_EQUAL"
    LESS = "LESS"
    LESS_EQUAL = "LESS_EQUAL"
    ARROW = "ARROW"

    # Literals
    IDENTIFIER = "IDENTIFIER"
    STRING = "STRING"
    NUMBER = "NUMBER"

    # Keywords
    AND = "AND"
    CLASS = "CLASS"
    ELSE = "ELSE"
    FALSE = "FALSE"
    FN = "FN"
    FOR = "FOR"
    IF = "IF"
    NIL = "NIL"
    PRINT = "PRINT"
    PRINTLN = "PRINTLN"
    RETURN = "RETURN"
    SUPER = "SUPER"
    THIS = "THIS"
    TRUE = "TRUE"
    LET = "LET"
    MUT = "MUT"
    WHILE = "WHILE"
    USE = "USE"
    IN = "IN"
    OR = "OR"
    AND = "AND"
    NOT = "NOT"
    TYPE = "TYPE"

    # EOF
    EOF = "EOF"


class Token:
    def __init__(self, type: TokenType, lex: str, literal: object, line: int) -> None:
        self.type = type
        self.lexeme = lex
        self.literal = literal
        self.line = line

    def __repr__(self) -> str:
        return f"{self.lexeme}"
