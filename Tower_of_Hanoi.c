#include <stdio.h>
#include <time.h>

void TOH(int n, char source, char aux, char destination) {
    if (n == 1) {
        printf("Move disk 1 from %c to %c\n", source, destination); // Added newline
    } else {
        TOH(n - 1, source, aux, destination);
        printf("Move disk %d from %c to %c\n", n, source, destination);
        TOH(n - 1, aux, destination, source);
    }
}

int main() {
    int num;

    printf("Enter number of disks to be simulated: ");
    scanf("%d", &num);

    float start_time = clock();

    TOH(num, 'A', 'B', 'C');

    float end_time = clock();

    float elapsed_time = ((double) (end_time - start_time)) / CLOCKS_PER_SEC;
    printf("Time taken to run program for %i disks is %.21f seconds./n", num ,  elapsed_time);

    return 0;
}
