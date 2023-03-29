#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");
    char buffer[500];
    while (fread(&buffer, sizeof(char), 500, file) == file)
{


}
}
