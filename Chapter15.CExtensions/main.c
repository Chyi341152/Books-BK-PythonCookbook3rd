//
// Created by goku on 18-2-7.
// clang -o main main.c library.c -lm 
//

#include "library.h"
#include <stdio.h>

int main(void) {
    int x = 10;
    int y = 20;
    int result;
    result = gcd(x, y);
    printf("%d\n", result);
}
