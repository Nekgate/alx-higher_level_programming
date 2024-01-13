#include <stdio.h>
void addnumber(int a, int b);

int main(void)
{
    addnumber(23, 45);
    return (0);
}
void addnumber(int a, int b)
{
    printf("%d\n", a + b);
}