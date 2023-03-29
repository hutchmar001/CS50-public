#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");
    char buffer[5000];
    while (fread(&buffer, sizeof(char), 5000, file) == 5000)
{
    if (buffer[0] == "0xff")
        {
            printf("%c\n", &buffer[0]);
        }
}
}
