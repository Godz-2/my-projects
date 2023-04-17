#include <stdio.h>

int main()
{
    int a[200][200], b[200][200], result[200][200];
    int rows, coulmn;
    printf("Enter The Rows Of Your Matrix: ");
    scanf("%d", &rows);

    printf("Enter The Coulmn Of Your Martrix: ");
    scanf("%d", &coulmn);

    printf("Enter The Elements Of your Matrix\n");

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < coulmn; j++)
        {
            scanf("%d", &a[i][j]);
        }
    }

    printf("\nFirst Matrix A\n");

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < coulmn; j++)
        {
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }

    printf("Enter The Elements Of Matrix\n");

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < coulmn; j++)
        {
            scanf("%d", &b[i][j]);
        }
    }

    printf("\nSecond Matrix B\n");

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < coulmn; j++)
        {
            printf("%d ", b[i][j]);
        }
        printf("\n");
    }

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < coulmn; j++)
        {
            result[i][j] = a[i][j] + b[i][j];
        }
    }

    printf("\nMatrix A+B\n");

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < coulmn; j++)
        {
            printf("%d ", result[i][j]);
        }
        printf("\n");
    }

    return 0;
}
