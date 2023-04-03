#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");

    unsigned char *buffer;
    buffer = (unsigned char *)malloc(sizeof(unsigned char)*1000000);

    while (fread(buffer, 1, 512, file) == 512)
{
        fread(buffer, 1, 512, file);
}
for (int i = 0; i < 1000; i++)
{
    if (buffer[i] == 0xFF)
    {
        printf("%d\n%d\n%d\n", buffer[i], buffer[i+1], buffer[i+2]);
    }
}
}
