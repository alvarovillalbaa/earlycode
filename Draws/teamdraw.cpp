#include <iostream>
#include <unistd.h>
#include <stdio.h>
#include <string>
using namespace std;

void teamDraw()
{
    int i;
    int rand_i;
    int size;
    int sized;
    int n;
    int teams;
    int members;
    string namesArr[size];
    string randArr[size];
    string finalArr[teams];

    cout << "How many participants?\n";
    cin >> size;
    cout << "How many teams?\n";
    cin >> teams;

    members == size / teams;

    cout << "Write the names of the participants:\n";
    i = 0;
    while (i < size)
    {
        cin >> namesArr[i];
        i++;
    }

    sized = size - 1;
    rand_i = rand() % sized + 0;

    // Creating a finalArr as the combination of namesArr
    i = 0;
    while (i < teams)
    {
        finalArr[i] = namesArr[rand_i];
        while (i < members)
        {
            finalArr[i] += ", " + namesArr[rand_i];
        }
        i++;
    }

    // Looping the output
    i = 0;
    while (i < teams)
    {
        n = 1;
        while (n < teams)
        {
            cout << n << ". " << finalArr[rand_i];
            n++;
        }
        break;
    }
}

int main()
{
    teamDraw();
    return 0;
}