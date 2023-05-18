#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    // Check for command line args
    if (argc != 2)
    {
        printf("Usage: ./read infile\n");
        return 1;
    }

    // Create buffer to read into
    char *buffer = (char *)malloc(100 * sizeof(char));

    // Create array to store plate numbers
    char *plates = (char *)malloc(100 * sizeof(char));

    FILE *infile = fopen(argv[1], "r");

    int idx = 0;

    while (fread(buffer, 1, 7, infile) == 7)
    {
        // Save plate number in array
        fwrite(&plates[idx], 1, sizeof(plates), infile);
        idx++;
    }

    for (int i = 0; i < 8; i++)
    {
        printf("%c\n", plates[i]);
    }
}
