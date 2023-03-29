#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");
    char buffer[33];
    while (fread(&buffer, sizeof(char), 33, file) == file)
{


}
}
