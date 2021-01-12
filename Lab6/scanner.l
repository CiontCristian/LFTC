%{ 	 

#include <stdio.h>
#include "parser.tab.h"

int line = 4;
int lexicallyCorect = 0;
%} 
%option noyywrap

CONSTANT		0|[+-]?[1-9][0-9]*
IDENTIFIER 		[a-zA-Z][a-zA-Z0-9]{0,8}

%% 

"function" {printf(" -reserved word: %s\n", yytext); return FUNCTION;}
"main" {printf(" -reserved word: %s\n", yytext); return MAIN;}
"Number" {printf(" -reserved word: %s\n", yytext); return NUMBER;}
"Bool" {printf(" -reserved word: %s\n", yytext); return BOOL;}
"if" {printf(" -reserved word: %s\n", yytext); return IF;}
"else" {printf(" -reserved word: %s\n", yytext);return ELSE;}
"while" {printf(" -reserved word: %s\n", yytext);return WHILE;}
"yield" {printf(" -reserved word: %s\n", yytext);return YIELD;}
"enough" {printf(" -reserved word: %s\n", yytext);return ENOUGH;}
"readln" {printf(" -reserved word: %s\n", yytext);return READLN;}
"writeln" {printf(" -reserved word: %s\n", yytext);return WRITELN;}
"true" {printf(" -reserved word: %s\n", yytext);return TRUE;}
"false" {printf(" -reserved word: %s\n", yytext);return FALSE;}

"div" {printf(" -operator: %s\n", yytext);return DIVISION;}
"mod" {printf(" -operator: %s\n", yytext);return MODULO;}
"and" {printf(" -operator: %s\n", yytext);return AND;}
"or" {printf(" -operator: %s\n", yytext);return OR;}
"not" {printf(" -operator: %s\n", yytext);return NOT;}


[+-]0	{
    printf("Invalid token at line %d , 0 can't have a sign\n", line);
    lexicallyCorect = 1;
     return -1;}
{IDENTIFIER} {printf( " -identifier: %s\n", yytext);return IDENTIFIER;}
{CONSTANT} {printf( " -constant: %s\n", yytext);return CONSTANT;}

":=" {printf(" -operator: %s\n", yytext);return ASSIGN;}
"==" {printf(" -operator: %s\n", yytext);return EQUALS;}
"<>" {printf(" -operator: %s\n", yytext);return DIFFERENT;}
"<" {printf(" -operator: %s\n", yytext);return LESS_THAN;}
"<=" {printf(" -operator: %s\n", yytext);return LESS_OR_EQUAL_THAN;}
">" {printf(" -operator: %s\n", yytext);return GREATER_THAN;}
">=" {printf(" -operator: %s\n", yytext);return GREATER_OR_EQUAL_THAN;}
"+" {printf(" -operator: %s\n", yytext);return PLUS;}
"-" {printf(" -operator: %s\n", yytext);return MINUS;}
"*" {printf(" -operator: %s\n", yytext);return MULTIPLY;}

"[" {printf(" -separator: %s\n", yytext);return LEFT_SQUARE_BRACKET;}
"]" {printf(" -separator: %s\n", yytext);return RIGHT_SQUARE_BRACKET;}
"{" {printf(" -separator: %s\n", yytext);return LEFT_CURLY_BRACKET;}
"}" {printf(" -separator: %s\n", yytext);return RIGHT_CURLY_BRACKET;}
"(" {printf(" -separator: %s\n", yytext);return LEFT_ROUND_BRACKET;}
")" {printf(" -separator: %s\n", yytext);return RIGHT_ROUND_BRACKET;}
";" {printf(" -separator: %s\n", yytext);return SEMI_COLON;}
"," {printf(" -separator: %s\n", yytext);return COMA;}

[ \t]+	{}

[\n]+	{++line;}

[a-zA-Z][a-zA-Z0-9]{9,}	{
    printf("Invalid token at line %d, token exceeds length limit\n", line);
    lexicallyCorect = 1;
     return -1;}

[0-9][a-zA-Z0-9]{0,8}	{
    printf("Invalid token at line %d, identifier can't start with letter\n", line);
    lexicallyCorect = 1;
     return -1;}
		 
.	{
     printf("Invalid token at line %d\n", line);
     lexicallyCorect = 1;
     return -1;
    }
%%  