
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARROW BANG BANG_EQUAL CLASS COMMA DOT ELSE EOF EQUAL EQUAL_EQUAL FALSE FN FOR GREATER GREATER_EQUAL IDENTIFIER IF LEFT_BRACE LEFT_BRACKET LEFT_PAREN LESS LESS_EQUAL LET MINUS MUT NIL NUMBER OR PLUS PRINT PRINTLN RETURN RIGHT_BRACE RIGHT_BRACKET RIGHT_PAREN SEMICOLON SLASH STAR STRING SUPER THIS TRUE WHILE\n    prog : fn_def_list\n    \n    fn_def_list : fn_def fn_def_list\n                | fn_def\n    \n    fn_def : FN IDENTIFIER LEFT_PAREN param_list RIGHT_PAREN LEFT_BRACE stmt_list RIGHT_BRACE\n           | FN IDENTIFIER LEFT_PAREN param_list RIGHT_PAREN ARROW expr\n    \n    param_list : IDENTIFIER COMMA param_list\n               | IDENTIFIER\n               | empty\n    \n    stmt_list : stmt stmt_list\n              | stmt\n    \n    stmt : expr\n         | declaration\n         | assign\n         | print\n         | condition\n         | while\n    \n    while : WHILE expr LEFT_BRACE stmt_list RIGHT_BRACE\n    \n    condition : IF expr LEFT_BRACE stmt_list RIGHT_BRACE\n              | IF expr LEFT_BRACE stmt_list RIGHT_BRACE ELSE LEFT_BRACE stmt_list RIGHT_BRACE\n    \n    print : PRINT expr SEMICOLON\n          | PRINTLN expr SEMICOLON\n    \n    expr : expr PLUS expr\n         | expr MINUS expr\n         | expr STAR expr\n         | expr SLASH expr\n         | expr LESS expr\n         | expr LESS_EQUAL expr\n         | expr GREATER expr\n         | expr GREATER_EQUAL expr\n         | expr EQUAL_EQUAL expr\n         | expr BANG_EQUAL expr\n    \n    expr : LEFT_PAREN expr RIGHT_PAREN\n    \n    expr : NUMBER\n         | NIL\n         | STRING\n         | LEFT_BRACKET expr_list_comma RIGHT_BRACKET\n    \n    expr : expr DOT IDENTIFIER\n         | expr DOT IDENTIFIER LEFT_PAREN expr_list_comma RIGHT_PAREN\n    \n    expr : IDENTIFIER LEFT_PAREN expr_list_comma RIGHT_PAREN\n    \n    expr_list_comma : expr COMMA expr_list_comma\n                 | expr\n                 | empty\n    \n    expr : IDENTIFIER\n    \n    expr : expr IF expr ELSE expr\n    \n    expr : LEFT_BRACE stmt_list RIGHT_BRACE\n    \n    declaration : LET IDENTIFIER EQUAL expr SEMICOLON\n                | LET MUT IDENTIFIER EQUAL expr SEMICOLON\n    \n    assign : IDENTIFIER EQUAL expr SEMICOLON\n    \n    empty :\n    '
    
_lr_action_items = {'FN':([0,3,27,28,29,36,37,42,67,68,69,70,71,72,73,74,75,76,77,78,79,81,89,99,104,],[4,4,-33,-34,-35,-43,-5,-4,-32,-45,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-37,-36,-39,-44,-38,]),'$end':([1,2,3,5,27,28,29,36,37,42,67,68,69,70,71,72,73,74,75,76,77,78,79,81,89,99,104,],[0,-1,-3,-2,-33,-34,-35,-43,-5,-4,-32,-45,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-37,-36,-39,-44,-38,]),'IDENTIFIER':([4,7,11,14,15,16,17,18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,39,44,45,46,47,48,49,50,51,52,53,54,55,61,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,86,87,88,89,90,91,92,96,99,100,101,103,104,106,107,109,],[6,8,8,16,36,-43,36,16,16,-11,-12,-13,-14,-15,-16,-33,-34,-35,36,36,60,36,36,36,-43,36,36,36,36,36,36,36,36,36,36,36,36,79,36,85,-32,-45,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-37,-36,36,16,36,-20,-21,16,-39,-48,36,36,36,-44,-18,-46,-17,-38,-47,16,-19,]),'LEFT_PAREN':([6,14,15,16,17,18,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,39,44,45,46,47,48,49,50,51,52,53,55,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,86,87,88,89,90,91,92,96,99,100,101,103,104,106,107,109,],[7,17,17,38,17,17,17,-11,-12,-13,-14,-15,-16,-33,-34,-35,17,17,17,17,17,38,17,17,17,17,17,17,17,17,17,17,17,17,17,-32,-45,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,91,-36,17,17,17,-20,-21,17,-39,-48,17,17,17,-44,-18,-46,-17,-38,-47,17,-19,]),'RIGHT_PAREN':([7,8,9,10,11,13,27,28,29,36,38,40,57,58,65,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,89,91,93,98,99,104,],[-49,-7,12,-8,-49,-6,-33,-34,-35,-43,-49,67,-41,-42,89,-32,-45,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-37,-36,-49,-39,-49,-40,104,-44,-38,]),'COMMA':([8,27,28,29,36,57,67,68,69,70,71,72,73,74,75,76,77,78,79,81,89,99,104,],[11,-33,-34,-35,-43,82,-32,-45,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-37,-36,-39,-44,-38,]),'LEFT_BRACE':([12,14,15,16,17,18,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,39,44,45,46,47,48,49,50,51,52,53,55,59,64,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,86,87,88,89,90,91,92,96,99,100,101,103,104,105,106,107,109,],[14,18,18,-43,18,18,18,-11,-12,-13,-14,-15,-16,-33,-34,-35,18,18,18,18,18,-43,18,18,18,18,18,18,18,18,18,18,18,18,18,83,88,-32,-45,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-37,-36,18,18,18,-20,-21,18,-39,-48,18,18,18,-44,-18,-46,-17,-38,107,-47,18,-19,]),'ARROW':([12,],[15,]),'NUMBER':([14,15,16,17,18,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,39,44,45,46,47,48,49,50,51,52,53,55,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,86,87,88,89,90,91,92,96,99,100,101,103,104,106,107,109,],[27,27,-43,27,27,27,-11,-12,-13,-14,-15,-16,-33,-34,-35,27,27,27,27,27,-43,27,27,27,27,27,27,27,27,27,27,27,27,27,-32,-45,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-37,-36,27,27,27,-20,-21,27,-39,-48,27,27,27,-44,-18,-46,-17,-38,-47,27,-19,]),'NIL':([14,15,16,17,18,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,39,44,45,46,47,48,49,50,51,52,53,55,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,86,87,88,89,90,91,92,96,99,100,101,103,104,106,107,109,],[28,28,-43,28,28,28,-11,-12,-13,-14,-15,-16,-33,-34,-35,28,28,28,28,28,-43,28,28,28,28,28,28,28,28,28,28,28,28,28,-32,-45,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-37,-36,28,28,28,-20,-21,28,-39,-48,28,28,28,-44,-18,-46,-17,-38,-47,28,-19,]),'STRING':([14,15,16,17,18,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,39,44,45,46,47,48,49,50,51,52,53,55,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,86,87,88,89,90,91,92,96,99,100,101,103,104,106,107,109,],[29,29,-43,29,29,29,-11,-12,-13,-14,-15,-16,-33,-34,-35,29,29,29,29,29,-43,29,29,29,29,29,29,29,29,29,29,29,29,29,-32,-45,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-37,-36,29,29,29,-20,-21,29,-39,-48,29,29,29,-44,-18,-46,-17,-38,-47,29,-19,]),'LEFT_BRACKET':([14,15,16,17,18,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,39,44,45,46,47,48,49,50,51,52,53,55,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,86,87,88,89,90,91,92,96,99,100,101,103,104,106,107,109,],[30,30,-43,30,30,30,-11,-12,-13,-14,-15,-16,-33,-34,-35,30,30,30,30,30,-43,30,30,30,30,30,30,30,30,30,30,30,30,30,-32,-45,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-37,-36,30,30,30,-20,-21,30,-39,-48,30,30,30,-44,-18,-46,-17,-38,-47,30,-19,]),'LET':([14,16,18,20,21,22,23,24,25,26,27,28,29,36,67,68,69,70,71,72,73,74,75,76,77,78,79,81,83,86,87,88,89,90,99,100,101,103,104,106,107,109,],[32,-43,32,32,-11,-12,-13,-14,-15,-16,-33,-34,-35,-43,-32,-45,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-37,-36,32,-20,-21,32,-39,-48,-44,-18,-46,-17,-38,-47,32,-19,]),'PRINT':([14,16,18,20,21,22,23,24,25,26,27,28,29,36,67,68,69,70,71,72,73,74,75,76,77,78,79,81,83,86,87,88,89,90,99,100,101,103,104,106,107,109,],[33,-43,33,33,-11,-12,-13,-14,-15,-16,-33,-34,-35,-43,-32,-45,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-37,-36,33,-20,-21,33,-39,-48,-44,-18,-46,-17,-38,-47,33,-19,]),'PRINTLN':([14,16,18,20,21,22,23,24,25,26,27,28,29,36,67,68,69,70,71,72,73,74,75,76,77,78,79,81,83,86,87,88,89,90,99,100,101,103,104,106,107,109,],[34,-43,34,34,-11,-12,-13,-14,-15,-16,-33,-34,-35,-43,-32,-45,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-37,-36,34,-20,-21,34,-39,-48,-44,-18,-46,-17,-38,-47,34,-19,]),'IF':([14,16,18,20,21,22,23,24,25,26,27,28,29,36,37,40,57,59,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,83,86,87,88,89,90,95,99,100,101,102,103,104,106,107,109,],[31,-43,31,31,55,-12,-13,-14,-15,-16,-33,-34,-35,-43,55,55,55,55,55,55,55,55,-32,-45,55,55,55,55,55,55,55,55,55,55,-37,55,-36,31,-20,-21,31,-39,-48,55,55,-18,-46,55,-17,-38,-47,31,-19,]),'WHILE':([14,16,18,20,21,22,23,24,25,26,27,28,29,36,67,68,69,70,71,72,73,74,75,76,77,78,79,81,83,86,87,88,89,90,99,100,101,103,104,106,107,109,],[35,-43,35,35,-11,-12,-13,-14,-15,-16,-33,-34,-35,-43,-32,-45,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-37,-36,35,-20,-21,35,-39,-48,-44,-18,-46,-17,-38,-47,35,-19,]),'PLUS':([16,21,27,28,29,36,37,40,57,59,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,95,99,102,104,],[-43,44,-33,-34,-35,-43,44,44,44,44,44,44,44,44,-32,-45,44,44,44,44,44,44,44,44,44,44,-37,44,-36,-39,44,44,44,-38,]),'MINUS':([16,21,27,28,29,36,37,40,57,59,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,95,99,102,104,],[-43,45,-33,-34,-35,-43,45,45,45,45,45,45,45,45,-32,-45,45,45,45,45,45,45,45,45,45,45,-37,45,-36,-39,45,45,45,-38,]),'STAR':([16,21,27,28,29,36,37,40,57,59,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,95,99,102,104,],[-43,46,-33,-34,-35,-43,46,46,46,46,46,46,46,46,-32,-45,46,46,46,46,46,46,46,46,46,46,-37,46,-36,-39,46,46,46,-38,]),'SLASH':([16,21,27,28,29,36,37,40,57,59,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,95,99,102,104,],[-43,47,-33,-34,-35,-43,47,47,47,47,47,47,47,47,-32,-45,47,47,47,47,47,47,47,47,47,47,-37,47,-36,-39,47,47,47,-38,]),'LESS':([16,21,27,28,29,36,37,40,57,59,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,95,99,102,104,],[-43,48,-33,-34,-35,-43,48,48,48,48,48,48,48,48,-32,-45,48,48,48,48,48,48,48,48,48,48,-37,48,-36,-39,48,48,48,-38,]),'LESS_EQUAL':([16,21,27,28,29,36,37,40,57,59,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,95,99,102,104,],[-43,49,-33,-34,-35,-43,49,49,49,49,49,49,49,49,-32,-45,49,49,49,49,49,49,49,49,49,49,-37,49,-36,-39,49,49,49,-38,]),'GREATER':([16,21,27,28,29,36,37,40,57,59,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,95,99,102,104,],[-43,50,-33,-34,-35,-43,50,50,50,50,50,50,50,50,-32,-45,50,50,50,50,50,50,50,50,50,50,-37,50,-36,-39,50,50,50,-38,]),'GREATER_EQUAL':([16,21,27,28,29,36,37,40,57,59,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,95,99,102,104,],[-43,51,-33,-34,-35,-43,51,51,51,51,51,51,51,51,-32,-45,51,51,51,51,51,51,51,51,51,51,-37,51,-36,-39,51,51,51,-38,]),'EQUAL_EQUAL':([16,21,27,28,29,36,37,40,57,59,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,95,99,102,104,],[-43,52,-33,-34,-35,-43,52,52,52,52,52,52,52,52,-32,-45,52,52,52,52,52,52,52,52,52,52,-37,52,-36,-39,52,52,52,-38,]),'BANG_EQUAL':([16,21,27,28,29,36,37,40,57,59,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,95,99,102,104,],[-43,53,-33,-34,-35,-43,53,53,53,53,53,53,53,53,-32,-45,53,53,53,53,53,53,53,53,53,53,-37,53,-36,-39,53,53,53,-38,]),'DOT':([16,21,27,28,29,36,37,40,57,59,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,95,99,102,104,],[-43,54,-33,-34,-35,-43,54,54,54,54,54,54,54,54,-32,-45,54,54,54,54,54,54,54,54,54,54,-37,54,-36,-39,54,54,54,-38,]),'RIGHT_BRACE':([16,19,20,21,22,23,24,25,26,27,28,29,36,41,43,67,68,69,70,71,72,73,74,75,76,77,78,79,81,86,87,89,90,94,97,99,100,101,103,104,106,108,109,],[-43,42,-10,-11,-12,-13,-14,-15,-16,-33,-34,-35,-43,68,-9,-32,-45,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-37,-36,-20,-21,-39,-48,100,103,-44,-18,-46,-17,-38,-47,109,-19,]),'EQUAL':([16,60,85,],[39,84,96,]),'RIGHT_BRACKET':([27,28,29,30,36,56,57,58,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,89,93,99,104,],[-33,-34,-35,-49,-43,81,-41,-42,-32,-45,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-37,-36,-49,-39,-40,-44,-38,]),'SEMICOLON':([27,28,29,36,62,63,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,89,95,99,102,104,],[-33,-34,-35,-43,86,87,90,-32,-45,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-37,-36,-39,101,-44,106,-38,]),'ELSE':([27,28,29,36,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,99,100,104,],[-33,-34,-35,-43,-32,-45,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-37,92,-36,-39,-44,105,-38,]),'MUT':([32,],[61,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'fn_def_list':([0,3,],[2,5,]),'fn_def':([0,3,],[3,3,]),'param_list':([7,11,],[9,13,]),'empty':([7,11,30,38,82,91,],[10,10,58,58,58,58,]),'stmt_list':([14,18,20,83,88,107,],[19,41,43,94,97,108,]),'stmt':([14,18,20,83,88,107,],[20,20,20,20,20,20,]),'expr':([14,15,17,18,20,30,31,33,34,35,38,39,44,45,46,47,48,49,50,51,52,53,55,82,83,84,88,91,92,96,107,],[21,37,40,21,21,57,59,62,63,64,57,66,69,70,71,72,73,74,75,76,77,78,80,57,21,95,21,57,99,102,21,]),'declaration':([14,18,20,83,88,107,],[22,22,22,22,22,22,]),'assign':([14,18,20,83,88,107,],[23,23,23,23,23,23,]),'print':([14,18,20,83,88,107,],[24,24,24,24,24,24,]),'condition':([14,18,20,83,88,107,],[25,25,25,25,25,25,]),'while':([14,18,20,83,88,107,],[26,26,26,26,26,26,]),'expr_list_comma':([30,38,82,91,],[56,65,93,98,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> fn_def_list','prog',1,'p_prog','parser.py',29),
  ('fn_def_list -> fn_def fn_def_list','fn_def_list',2,'p_fn_def_list','parser.py',36),
  ('fn_def_list -> fn_def','fn_def_list',1,'p_fn_def_list','parser.py',37),
  ('fn_def -> FN IDENTIFIER LEFT_PAREN param_list RIGHT_PAREN LEFT_BRACE stmt_list RIGHT_BRACE','fn_def',8,'p_fn_def','parser.py',47),
  ('fn_def -> FN IDENTIFIER LEFT_PAREN param_list RIGHT_PAREN ARROW expr','fn_def',7,'p_fn_def','parser.py',48),
  ('param_list -> IDENTIFIER COMMA param_list','param_list',3,'p_param_list','parser.py',58),
  ('param_list -> IDENTIFIER','param_list',1,'p_param_list','parser.py',59),
  ('param_list -> empty','param_list',1,'p_param_list','parser.py',60),
  ('stmt_list -> stmt stmt_list','stmt_list',2,'p_stmt_list','parser.py',73),
  ('stmt_list -> stmt','stmt_list',1,'p_stmt_list','parser.py',74),
  ('stmt -> expr','stmt',1,'p_stmt','parser.py',84),
  ('stmt -> declaration','stmt',1,'p_stmt','parser.py',85),
  ('stmt -> assign','stmt',1,'p_stmt','parser.py',86),
  ('stmt -> print','stmt',1,'p_stmt','parser.py',87),
  ('stmt -> condition','stmt',1,'p_stmt','parser.py',88),
  ('stmt -> while','stmt',1,'p_stmt','parser.py',89),
  ('while -> WHILE expr LEFT_BRACE stmt_list RIGHT_BRACE','while',5,'p_while','parser.py',96),
  ('condition -> IF expr LEFT_BRACE stmt_list RIGHT_BRACE','condition',5,'p_condition','parser.py',103),
  ('condition -> IF expr LEFT_BRACE stmt_list RIGHT_BRACE ELSE LEFT_BRACE stmt_list RIGHT_BRACE','condition',9,'p_condition','parser.py',104),
  ('print -> PRINT expr SEMICOLON','print',3,'p_print','parser.py',114),
  ('print -> PRINTLN expr SEMICOLON','print',3,'p_print','parser.py',115),
  ('expr -> expr PLUS expr','expr',3,'p_expr_binary','parser.py',123),
  ('expr -> expr MINUS expr','expr',3,'p_expr_binary','parser.py',124),
  ('expr -> expr STAR expr','expr',3,'p_expr_binary','parser.py',125),
  ('expr -> expr SLASH expr','expr',3,'p_expr_binary','parser.py',126),
  ('expr -> expr LESS expr','expr',3,'p_expr_binary','parser.py',127),
  ('expr -> expr LESS_EQUAL expr','expr',3,'p_expr_binary','parser.py',128),
  ('expr -> expr GREATER expr','expr',3,'p_expr_binary','parser.py',129),
  ('expr -> expr GREATER_EQUAL expr','expr',3,'p_expr_binary','parser.py',130),
  ('expr -> expr EQUAL_EQUAL expr','expr',3,'p_expr_binary','parser.py',131),
  ('expr -> expr BANG_EQUAL expr','expr',3,'p_expr_binary','parser.py',132),
  ('expr -> LEFT_PAREN expr RIGHT_PAREN','expr',3,'p_expr_grouping','parser.py',139),
  ('expr -> NUMBER','expr',1,'p_expr_literal','parser.py',146),
  ('expr -> NIL','expr',1,'p_expr_literal','parser.py',147),
  ('expr -> STRING','expr',1,'p_expr_literal','parser.py',148),
  ('expr -> LEFT_BRACKET expr_list_comma RIGHT_BRACKET','expr',3,'p_expr_literal','parser.py',149),
  ('expr -> expr DOT IDENTIFIER','expr',3,'p_expr_dispatch','parser.py',165),
  ('expr -> expr DOT IDENTIFIER LEFT_PAREN expr_list_comma RIGHT_PAREN','expr',6,'p_expr_dispatch','parser.py',166),
  ('expr -> IDENTIFIER LEFT_PAREN expr_list_comma RIGHT_PAREN','expr',4,'p_expr_fn_call','parser.py',176),
  ('expr_list_comma -> expr COMMA expr_list_comma','expr_list_comma',3,'p_expr_list_comma','parser.py',183),
  ('expr_list_comma -> expr','expr_list_comma',1,'p_expr_list_comma','parser.py',184),
  ('expr_list_comma -> empty','expr_list_comma',1,'p_expr_list_comma','parser.py',185),
  ('expr -> IDENTIFIER','expr',1,'p_expr_variable','parser.py',198),
  ('expr -> expr IF expr ELSE expr','expr',5,'p_expr_ternary','parser.py',205),
  ('expr -> LEFT_BRACE stmt_list RIGHT_BRACE','expr',3,'p_expr_block','parser.py',212),
  ('declaration -> LET IDENTIFIER EQUAL expr SEMICOLON','declaration',5,'p_declaration','parser.py',219),
  ('declaration -> LET MUT IDENTIFIER EQUAL expr SEMICOLON','declaration',6,'p_declaration','parser.py',220),
  ('assign -> IDENTIFIER EQUAL expr SEMICOLON','assign',4,'p_assign','parser.py',230),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',237),
]
