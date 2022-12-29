#include <stdio.h>
#include <stdin.h>

int main(void)
{
    printf("hello, world\n");
    string str= get_string("What's your name? ");
    printf("hello, %s\n", str);
}
