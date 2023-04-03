#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");
    int i = 0;
    unsigned char buffer[10000];

    while (fread(buffer, 512, 1, file) == 1)
{
    fread(buffer, 1, 1, file);
    if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff)
    {
        fread(buffer, 1, 1, file);
    }
}
for (i = 0; i < 10000; i++)
    if (buffer[i] == 0xff)
    {
        printf("%d\n%d\n", buffer[i], buffer[i+1]);
    }

}
