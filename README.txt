<stmt> --> <if_stmt> | <while_loop> | <assignment> | <block>
<block> --> '{' { <stmt>';' } '}'
<if_stmt> --> 'if''('<bool_expr>')' <stmt> [ 'else' <stmt>]
<while_loop> --> 'while''(' <bool_expr> ')' <stmt>
<assignment> --> 'id' '=' <expr>
<expr> --> <term> { (+|-) <term> }
<term> --> <factor> {(+|-) <factor> }
<factor> --> id | int_lit | '(' <expr> ')'
