#include <stdio.h>

void sum_n_avg(double a, double b, double c, double *sum, double *avg) {
    *sum = a + b + c;         // Calculate the sum
    *avg = *sum / 3;          // Calculate the average
}

int main() {
    double one, two, three, sum_of_3, avg_of_3;

    printf("Enter three numbers> ");
    scanf("%lf%lf%lf", &one, &two, &three);

    sum_n_avg(one, two, three, &sum_of_3, &avg_of_3);

    printf("Sum: %.2lf\n", sum_of_3);
    printf("Average: %.2lf\n", avg_of_3);

    return 0;
}
