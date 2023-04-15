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
    unsigned char buffer[512];
    int i = 0;
    char jpegs[50];
    while (fread(buffer, 1, 512, file) == 512)
{
    if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
    {

        sprintf(&jpegs[0], "%03i.jpg", i);
        FILE *img = fopen(&jpegs[0], "w");
        fwrite(&buffer[0], 1, 512, img);
        i++;
        fclose(img);
    }
}
}

