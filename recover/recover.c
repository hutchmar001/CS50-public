#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");
    char buffer[5000];
    while (fread(&buffer, sizeof(char), 5000, file) == 5000)
{
    for (int i = 0; i <= 5000; i++)
    {
            printf("%c\n", buffer[i]);
        }
}
}

