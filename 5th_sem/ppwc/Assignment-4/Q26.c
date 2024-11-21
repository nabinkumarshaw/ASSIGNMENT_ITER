#include <stdio.h>

void transpose_matrix(int *matrix, int *transposed, int rows, int cols) {
    // Pointer to traverse the original matrix and transpose it
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            // Using pointer arithmetic to access elements and transpose
            *(transposed + j * rows + i) = *(matrix + i * cols + j);
        }
    }
}

void display_matrix(int *matrix, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            // Printing matrix elements using pointer arithmetic
            printf("%d ", *(matrix + i * cols + j));
        }
        printf("\n");
    }
}

int main() {
    int rows, cols;

    // Input the dimensions of the matrix
    printf("Enter the number of rows and columns: ");
    scanf("%d %d", &rows, &cols);

    int matrix[rows][cols];  // Original matrix
    int transposed[cols][rows];  // Transposed matrix

    // Input elements of the matrix
    printf("Enter the elements of the matrix:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }

    // Transpose the matrix
    transpose_matrix((int *)matrix, (int *)transposed, rows, cols);

    // Display the original matrix
    printf("\nOriginal Matrix:\n");
    display_matrix((int *)matrix, rows, cols);

    // Display the transposed matrix
    printf("\nTransposed Matrix:\n");
    display_matrix((int *)transposed, cols, rows);

    return 0;
}
