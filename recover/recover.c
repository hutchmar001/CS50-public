#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");
    int i = 0;
    unsigned char buffer[10000];

    while (fread(buffer, sizeof(char), 512, file) == 512)
{
    if (buffer[i] == 0xFF)
    {
        fread(buffer, sizeof(char), 512, file);
    }
}
for (i = 0; i < 10000; i++)
    if (buffer[i] == 0xFF)
    {
        printf("%c\n", buffer[i]);
    }

}
