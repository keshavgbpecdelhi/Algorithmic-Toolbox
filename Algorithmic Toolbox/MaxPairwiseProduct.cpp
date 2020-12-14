#include <iostream>
#include <vector>
using std::vector;
using std::cin;
using std::cout;
using std::max;
long long int MaxPairwiseProduct(const vector<long long int>& numbers) {
long long int index1 = 0, index2 = 0, product=0;
for (int i = 0; i < numbers.size(); i++)
{
	if (numbers[i] > index1)
	{
		index2 = index1;
		index1 = numbers[i];
	}
	else if (numbers[i] > index2)
	{
		index2 = numbers[i];
	}
}
product = index1*index2;
return product;
}


int main() {
long long int n;
cin >> n;
vector<long long int> numbers(n);
for (int i = 0; i < n; ++i) {
cin >> numbers[i];
}
long long int product = MaxPairwiseProduct(numbers);
cout << product << "\n";
return 0;
}
