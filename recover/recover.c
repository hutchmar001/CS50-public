#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");
    int i = 0;
    unsigned char buffer[10000];

    while (fread(buffer, 1, 512, file) == 512)
{
    if (buffer[i] == 0xFF)
    {
        fread(buffer, 1, 512, file);
    }
}
for (i = 0; i < 10; i++)
    {
        printf("%c\n", buffer[i]);
    }

}
