#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");
    unsigned char buffer[10000];
    while (fread(buffer, sizeof(char), 10000, file) == 5000)
{
        fread(buffer, sizeof(char), 10000, file);
}
for (int i = 0; i < 10000; i++)
{
    if (buffer[i] == 216)
    {
    printf("%d\n%d\n%d\n", buffer[i], buffer[i+1], buffer[i+2]);
    }
}
}
