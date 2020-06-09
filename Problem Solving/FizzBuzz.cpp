
#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);


/*
 * Complete the 'fizzBuzz' function below.
 *
 * The function accepts INTEGER n as parameter.
 */

void fizzBuzz(int n) {
    int i = 0; // initialize
    for (int i=1; i <=n; i++){
        if (i % 15 ==0)
            printf("FizzBuzz\n");
        else if (i % 3 == 0 && i % 5 !=0)
            printf("Fizz\n");
        else if (i % 5 == 0 && i % 3 !=0)
            printf("Buzz\n");
        else 
            printf("%d\n",i);
    }
}
int main()
