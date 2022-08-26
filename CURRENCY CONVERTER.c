#include <stdio.h>
int main()
{
    char input;
    float rupeestowon = 16.76;
    float rupeestodollar = 0.013;
    float rupeestoyen = 1.71;
    float yentodollar = 0.0073;
    float poundtodollar = 1.18;
    float poundtoyen = 162.02;
    float a, b;

    while (1)
    {
        printf("Press q to Quit\n 1. Press 1 for Rupees to Dollar\n 2. Press 2 for Rupees to Yen\n   3. Press 3 for Yen To Dollar\n 4. Press 4 for Pound to Dollar\n 5. Press 5 for Pound to Yen\n 6. Press 6 for Rupees to South Korean Won\n");
        scanf(" %c",&input);
        
        switch (input)
        {
        case 'q':
            //scanf(" %c", &input);
            // hello;
            printf("Quitting The Program\n");
            goto end;
            break;

        case '1':
           printf("Enter The Value In Rupees ");
           scanf("%f",&a);
            b = a * rupeestodollar;
            printf("The Given Value in Dollars is %0.2f \n", b);
            break;

        case '2':
           printf("Enter The Value in Rupees ");
           scanf("%f",&a);
            b = a * rupeestoyen;
            printf("The Given Value In Yen is %0.2f \n", b);
            break;

        case '3':
            printf("Enter The Value in Yen ");
            scanf("%f",&a);
            b = a * yentodollar;
            printf("The Given Value In Dollars is %0.2f \n ", b);
            break;

        case '4':
            printf("Enter The Value in Pound ");
            scanf("%f",&a);
            b = a * poundtodollar;
            printf("The Given Value In Dollar is %0.2f \n", b);
            break;

        case '5':
            printf("Enter The Value in Pound ");
            scanf("%f",&a);
            b = a * poundtoyen;
            printf("The Given Value In Yen is %0.2f \n", b);
            break;
        case '6':
            printf("Enter The Value in Rupees");
            scanf("%f",&a);
            b = a * rupeestowon;
            printf("The Given Value in South Korean Won is %0.2f \n",b);

        default:
            //printf("On Default Going");
            break;
        }
    }
    end:

     printf("Thank You Visit Again\n");
     return 0;
}
