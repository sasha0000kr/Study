#include <stdio.h>
#include <math.h>

int main() {
    double hypotenuse, leg_1, leg_2, inradius;

    // Ввод данных
    printf("Enter the value of the hypotenuse: ");
    scanf("%lf", &hypotenuse);
    printf("Enter the value of the leg: ");
    scanf("%lf", &leg_1);

    // Вычисление второго катета
    leg_2 = sqrt(hypotenuse * hypotenuse - leg_1 * leg_1);
    // Вычисление радиуса вписанной окружности
    inradius = (leg_1 + leg_2 - hypotenuse) / 2;

    // Вывод результатов
    printf("Second leg: %.2lf\n", leg_2);
    printf("Radius of the inscribed circle: %.2lf\n", inradius);

    return 0;
}
