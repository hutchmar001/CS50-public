#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");
    unsigned char buffer[10000];
    int *ptr1 = new int;
   int *ptr2 = new int[10];

    while (fread(buffer, sizeof(char), 512, file) == 512)
{
        fread(buffer, sizeof(char), 512, file);
}
for (int i = 0; i < 10000; i++)
{
    if (buffer[i] == 0xFF && buffer[i+1] == 0xD8 && buffer[i+2] == 0xFF)
    {
    printf("%d\n%d\n%d\n", buffer[i], buffer[i+1], buffer[i+2]);
    }
}
}
