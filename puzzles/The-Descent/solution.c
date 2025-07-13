#include <stdio.h>


int main()
{
    while (1) {
        int max = 0;
        int max_i = 0;
        for (int i = 0; i < 8; i++) {

            int mountain_h;
            scanf("%d", &mountain_h);
            if (i == 0 || mountain_h > max) {
                max = mountain_h; 
                max_i = i;
            }
        }

        printf("%d\n", max_i);
    }
}
