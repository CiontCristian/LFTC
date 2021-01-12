#include <stdlib.h>
#include <stdio.h>
#include "lex.yy.c"


extern int yylex();

void main(int argc, char** argv){           
    if (argc > 1)
    {
        FILE *file;
        file = fopen(argv[1], "r");
        if (!file)
        {
            fprintf(stderr, "Could not open %s\n", argv[1]);
            exit(1);
        }
        yyin = file;
    }

    yylex();
    if(lexicallyCorect == 0){
        printf("Program is lexically correct!");
    }
}