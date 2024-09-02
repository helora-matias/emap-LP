#include <stdio.h> 
#include <stdlib.h>

int main(char argc, char* argv[]) {
    int n = atoi(argv[1]); 
    int total = 0;

    for(int i = 1; i <= n; i++) {
        total += i;
    }
    printf("%d\n", total);
}