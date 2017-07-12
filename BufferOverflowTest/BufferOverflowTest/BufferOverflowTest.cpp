// BufferOverflowTest.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
	char *temp;

	temp = (char *) malloc(500);

	for (int i = 0; i < 1000; i++)
	{
		temp[i] = 32;
	}

	return 0;
}