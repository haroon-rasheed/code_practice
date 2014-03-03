#include <iostream>
using namespace std;

class Test
{
	public:
			void print()
			{
					cout << "Welcome" << endl;
			}


};

void get_class(Test t)
{
		printf("TT => %p \n", t);
};

int main()
{
		Test* t1 = new Test();
		t1->print();
		//  get_class(reinterpret_cast<Test>(t1)>);
		Test t2;
		get_class(t2);
}
