#include <Python.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, al, index = 0;
	PyObject *element;

	size = PyList_Size(p);
	al = ((PyListObject *)p)->al;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", al);
	while (index < size)
	{
		element = PyList_GET_ITEM(p, index);
		printf("Element %ld: %s\n", index, element->ob_type->tp_name);
		index++;
	}
}
