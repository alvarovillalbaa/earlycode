#include <iostream>
#include <unistd.h>
#include <stdio.h>
#include <string>
using namespace std;

void lotteryDraw()
{
    int maxNumber;
    int minNumber;
    int amount;
    int x;
    int randNumber;

    cout << "We are going to set a range!";
    cout << "What is the maximum number?";
    cin >> maxNumber;
    cout << "What is the minimum number?";
    cin >> minNumber;
    cout << "How many numbers do you need?";
    cin >> amount;

    randNumber = rand() % maxNumber + minNumber;

    x = 1;
    while (x <= amount)
    {
        while (number >= minNumber)
        {
            while (number <= maxNumber)
            {
                cout << randNumber;
            }
        }
        x++;
    }
}

int main()
{
    lotteryDraw();
    return 0;
}