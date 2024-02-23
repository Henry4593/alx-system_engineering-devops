
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - Enters an infinite loop.
 *
 * Description:
 * - Uses a `while(1)` loop to continuously execute.
 * - Calls `sleep(1)` to introduce a one-second delay between iterations.
 *
 * This function essentially halts program execution by never exiting the loop.
 *
 * Return: 0 (but never reached due to infinite loop).
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * create_zombie_process - Creates a zombie process.
 *
 * Description:
 * - Uses `fork()` to create a child process.
 * - Child process prints its PID and exits immediately.
 * - Parent process exits without waiting for the child.
 *
 * This creates a zombie process because the child exits, but the parent
 * doesn't wait for it, leaving the child's entry in the process table.
 *
 * Return: None.
 */

void create_zombie_process(void)
{
	int created_process = fork();

	if (created_process == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}
}

/**
 * main - Creates five zombie processes and enters infinite loop.
 *
 * Description:
 * - Calls `create_zombie_process()` five times to create zombie processes.
 * - Calls `infinite_while()` to enter an infinite loop.
 *
 * This code demonstrates how to create zombie processes, but running it
 * can negatively impact system performance due to uncleaned zombie processes.
 *
 * Return: None (but program never exits due to infinite loop).
 */

int main(void)
{
	create_zombie_process();
	create_zombie_process();
	create_zombie_process();
	create_zombie_process();
	create_zombie_process();
	return (infinite_while());
}
