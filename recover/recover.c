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
    unsigned char buffer[1000];
    int i = 0;
    FILE *img = NULL;

    while (fread(buffer, 1, 512, file) == 512)
{
    if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
    {
        if (i == 0)
        {
            char jpegs[1000];
            sprintf(&jpegs[i], "%03i.jpg", i);
            img = fopen(&jpegs[i], "w");
            fwrite(&buffer[0], 1, 512, img);
            i++;
        }
        else
        {
            fclose(img);
            char jpegs[1000];
            sprintf(&jpegs[i], "%03i.jpg", i);
            img = fopen(&jpegs[i], "w");
        }
    }
    else
    {
        continue;
    }
}
fclose(file);
}

