#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");
    int i = 0;
    unsigned char buffer[10000];

    while (fread(buffer, 1, 1, file) == 1)
{
    if (buffer[0] == 255 && buffer[1] == 0xd8 && buffer[2] == 0xff)
    {
        fread(buffer, 1, 1, file);
    }
}
for (i = 0; i < 10; i++)
    {
        printf("%d\n%d\n", buffer[i], buffer[i+1]);
    }

}
