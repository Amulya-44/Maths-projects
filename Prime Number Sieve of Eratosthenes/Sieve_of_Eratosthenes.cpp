#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

void displayPrime(int num)
{
    if (num < 2)
    {
        cout << "No prime numbers." << endl;
        return;
    }

    vector<bool> is_prime(num + 1, true);

    is_prime[0] = false;
    is_prime[1] = false;

    int limit = sqrt(num);

    for (int p = 2; p <= limit; p++)
    {
        if (is_prime[p])
        {
            for (int i = p * p; i <= num; i += p)
            {
                is_prime[i] = false;
            }
        }
    }

    cout << "Prime numbers are: ";

    for (int i = 2; i <= num; i++)
    {
        if (is_prime[i])
        {
            cout << i << " ";
        }
    }

    cout << endl;
}

int main()
{
    int num;

    cout << "Enter a number up to which primes are to be determined: ";
    cin >> num;

    displayPrime(num);

    return 0;
}
