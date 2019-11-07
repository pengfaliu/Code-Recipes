#include "stdio.h"
#include "math.h"
unsigned long  Cumulation(unsigned long  _MAX_N)
{
	unsigned long  i;
	for (i=_MAX_N-1;i>=1;i--)

		_MAX_N=_MAX_N+i;
		return _MAX_N;
}

main ()
{
 unsigned long  _N,_S;
 unsigned long  Cumulation(unsigned long  _MAX_N);
 printf ("please input a Number for accumulation:\n");
 scanf ("%lu",&_N);
 _S=Cumulation(_N);
 printf ("The sum is %lu:\t\n",_S);
 return 0;
}
 

