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
    char buffer[7];

    // Create array to store plate numbers
    char *plates = malloc(60);
    FILE *infile = fopen(argv[1], "r");

    int idx = 0;

    while (fread(&buffer, 1, 7, infile) == 7)
    {
        // Replace '\n' with '\0'
        buffer[6] = '\0';
        printf("%s\n", &buffer[idx]); //changed
        // Save plate number in array
        strncpy(&plates[idx], &buffer[idx], 1); //changed
        idx++;
    }


    fclose(infile);
}
