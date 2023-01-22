#include<poorser/poorser.hpp>
#include <io.h>
#include <fcntl.h>

int main() {
	_setmode(_fileno(stdout), _O_U8TEXT);
	
	client C;

	C.interact();

}