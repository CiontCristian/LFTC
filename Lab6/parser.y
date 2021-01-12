%{
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1
%}

%token IDENTIFIER
%token CONSTANT
%token ASSIGN
%token EQUALS
%token DIFFERENT
%token LESS_THAN
%token LESS_OR_EQUAL_THAN
%token GREATER_THAN
%token GREATER_OR_EQUAL_THAN
%token PLUS
%token MINUS
%token MULTIPLY
%token DIVISION
%token MODULO
%token AND
%token OR
%token NOT
%token LEFT_SQUARE_BRACKET
%token RIGHT_SQUARE_BRACKET
%token LEFT_CURLY_BRACKET
%token RIGHT_CURLY_BRACKET
%token LEFT_ROUND_BRACKET
%token RIGHT_ROUND_BRACKET
%token SEMI_COLON
%token COMA
%token NUMBER
%token BOOL
%token TRUE
%token FALSE
%token IF
%token ELSE
%token WHILE
%token YIELD
%token ENOUGH
%token READLN
%token WRITELN
%token FUNCTION
%token MAIN

%start program

%%

    program: FUNCTION MAIN LEFT_ROUND_BRACKET RIGHT_ROUND_BRACKET cmpdstmt;
    cmpdstmt: LEFT_CURLY_BRACKET stmtlist RIGHT_CURLY_BRACKET;
    stmtlist: stmt stmtlist | stmt;
    stmt: decl SEMI_COLON | simplestmt SEMI_COLON | structstmt;
    decl: type IDENTIFIER;
    type: simple_data_type | array_type;
    simple_data_type: NUMBER | BOOL;
    array_type: simple_data_type LEFT_SQUARE_BRACKET term RIGHT_SQUARE_BRACKET;
    simplestmt: assignstmt | outstmt | instmt | returnstmt;
    returnstmt: YIELD term;
    assignstmt: IDENTIFIER ASSIGN expression;
    expression: arithmetic_expression | relational_expression | term;
    arithmetic_expression: term operator arithmetic_expression | term operator term;
    operator: PLUS | MINUS | DIVISION | MULTIPLY | MODULO;
    relational_expression: term relation relational_expression | term relation term;
    relation: EQUALS | DIFFERENT | LESS_THAN | LESS_OR_EQUAL_THAN | GREATER_THAN | GREATER_OR_EQUAL_THAN | AND | OR | NOT;
    term: IDENTIFIER | CONSTANT | IDENTIFIER LEFT_SQUARE_BRACKET term RIGHT_SQUARE_BRACKET | TRUE | FALSE;
    outstmt: WRITELN LEFT_ROUND_BRACKET term RIGHT_ROUND_BRACKET;
    instmt: READLN LEFT_ROUND_BRACKET term RIGHT_ROUND_BRACKET;
    structstmt: ifstmt | whilestmt;
    ifstmt: IF LEFT_ROUND_BRACKET relational_expression RIGHT_ROUND_BRACKET cmpdstmt | IF LEFT_ROUND_BRACKET relational_expression RIGHT_ROUND_BRACKET cmpdstmt ELSE cmpdstmt;
    whilestmt: WHILE LEFT_ROUND_BRACKET relational_expression RIGHT_ROUND_BRACKET cmpdstmt;

%%

yyerror(char *s)
{
  printf("%s\n", s);
}

extern FILE *yyin;

void main(int argc, char **argv)
{
    if (argc > 1)
    {   
        yyin = fopen(argv[1], "r");
    }
    if ( (argc > 2) && ( !strcmp(argv[2], "-d") ) ) 
        yydebug = 1;

    if ( !yyparse() ) 
        fprintf(stderr,"Program is syntactically correct!\n");

}
