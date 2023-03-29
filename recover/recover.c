#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");
    char buffer[512];
    while (fread(&buffer, sizeof(char), 512, file) == 512)
{


}
}
