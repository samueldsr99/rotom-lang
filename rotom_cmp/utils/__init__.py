import re


# Strings with no "${something}" pattern
NON_FSTRING = "(?!.*?\${.*?}).*?"


def is_fstring(string):
    match = re.match(NON_FSTRING, string)
    return False if match else True
