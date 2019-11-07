#include "stdio.h"
int _MAX(int _A,int _B)
{
	if (_A>_B)
		return _A;
	else
		return _B;
}
main()
{
	int _MAX(int _A,int _B);
	int _X,_Y,_Z;
	printf ("请输入两个数,用逗号分开:\n");
	scanf ("%d,%d",&_X,&_Y);
	_Z=_MAX(_X,_Y);
	printf ("maxnumb=%d\n",_Z);
}
