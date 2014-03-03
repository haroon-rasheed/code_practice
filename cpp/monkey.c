#include <stdio.h>

int fun1()
{
		printf("welcome \n");
}


int fun2()
{
		printf("welcome2 \n");
}

int main()
{
		fun1();
		fun2();
		printf("%p \n", fun1);
		printf("%p \n", fun2);
		
}
