#include <iostream>
#include <unistd.h>
#include <stdio.h>
#include <string>
using namespace std;

void simpleDraw()
{
    int i;
    int rand_i;
    int size;
    int sized;
    int n;
    string namesArr[size];

    cout << "How many participants?\n";
    cin >> size;

    cout << "Write the names of the participants:\n";
    i = 0;
    while (i < size)
    {
        cin >> namesArr[i];
        i++;
    }

    sized = size - 1;
    rand_i = rand() % sized + 0; // We create a random position instead of a random array

    // Looping the output
    i = 0;
    while (i < size)
    {
        n = 1;
        while (n < size)
        {
            cout << n << ". " << namesArr[rand_i]; // We need to set a seed for generating different random numbers in while
            n++;
        }
        break;
    }
}

int main()
{
    simpleDraw();
    return 0;
}