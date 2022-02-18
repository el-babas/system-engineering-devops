#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>

/* ########## Prototypes ########## */
int infinite_while(void);

/* ########## Functions ########## */

/**
 * main - C program that creates 5 zombie processes.
 *
 * Return: Always 0 on success
 */
int main(void)
{
	int i = 0, pzombies = 5;

	for (i = 0; i < pzombies; i++)
	{
		if (fork() == 0)
		{
			dprintf(1, "Zombie process created, PID: %d\n", getpid());
			return (0);
		}
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - C Functions create infinite while (sleep 1)
 *
 * Return: Always 0 on success
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
