#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("File cannot be opened for reading.");
        return 1;
    }
    unsigned char buffer[10000];
    while (fread(buffer, 512, 1, file) == 1)
{
    fread(buffer, 512, 1, file);
    int i = 0;
    if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
    {
        char jpegs[50];
        sprintf(&jpegs[i], "%03i.jpg", i);
        printf("%s\n", &jpegs[i]);
    }
}
}
