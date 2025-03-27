#include <stdio.h>
#include <string.h>

int main() {
    int N, X;
    
    // Accept the number of domestic animals
    printf("Enter the number of domestic animals: ");
    scanf("%d", &N);
    
    char domestic[N][50];
    
    // Accept names of domestic animals
    for (int i = 0; i < N; i++) {
        printf("Enter the name of domestic animal %d: ", i + 1);
        scanf("%s", domestic[i]);
    }
    
    // Accept the number of wild animals
    printf("Enter the number of wild animals: ");
    scanf("%d", &X);
    
    char wild[X][50];
    
    // Accept names of wild animals
    for (int i = 0; i < X; i++) {
        printf("Enter the name of wild animal %d: ", i + 1);
        scanf("%s", wild[i]);
    }
    
    // Print all animals
    printf("Combined list of animals:\n");
    for (int i = 0; i < N; i++) {
        printf("%s,", domestic[i]);
    }
    for (int i = 0; i < X; i++) {
        printf("%s,", wild[i]);
    }
    
    return 0;
}