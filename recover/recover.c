#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");
    const char buffer[5000];
    while (fread(buffer, sizeof(char), 5000, file) == 5000)
{
        fread(buffer, sizeof(char), 5000, file);
}
for (int i = 0; i < 5; i++)
{
    if (strcmp(buffer[i], "d9") == 0)
    {
    printf("%s\n", buffer[i]);
    }
}
}
