#include <stdio.h>
void printPrimeFactors(int num) 
{
    printf("Prime factorization of %d: ", num);
    
    while (num % 2 == 0) {
        printf("%d", 2);
        num /= 2;
        if (num > 1)
        {
        printf(" * ");
        }
    }
    for (int i = 3; i * i <= num; i += 2) 
    {
        while (num % i == 0)
        {
            printf("%d", i);
            num /= i;
            if (num > 1) 
            {
            printf(" * ");
            }
        }
    }
    
    if (num > 1) 
    {
        printf("%d", num);
    }
    printf("\n");
}

int main() 
{
    int num;
    printf("Enter a number: ");
    if (scanf("%d", &num) != 1 || num <= 1) 
    {
        printf("Please enter an integer greater than 1.\n");
        return 1;
    }
    printPrimeFactors(num);
    return 0;
}