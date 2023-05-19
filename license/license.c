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
    char *plates, *buffer;
    // Create buffer to read into
    buffer = (char *)malloc(50 * sizeof(char)); //changed

    // Create array to store plate numbers
    plates = (char *)malloc(50 * sizeof(char)); //changed

    FILE *infile = fopen(argv[1], "r");

    int idx = 0;

    while (fread(buffer, 1, 7, infile) == 7)
    {
        // Replace '\n' with '\0'
        buffer[6] = '\0';

        // Save plate number in array
        strcpy(&plates[idx], buffer); //changed
        idx++;
    }

    for (int i = 0; i < 32; i++)
    {
        printf("%s\n", plates[i]);
    }
}
