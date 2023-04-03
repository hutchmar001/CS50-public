#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");
    char buffer[10000];
    while (fread(buffer, sizeof(char), 10000, file) == 5000)
{
        fread(buffer, sizeof(char), 10000, file);
}
for (int i = 0; i < 50; i++)
{

    printf("%p\n%p\n%p\n", &buffer[i], &buffer[i+1], &buffer[i+2]);

}
}
