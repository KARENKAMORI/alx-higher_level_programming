#include <Python.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t p_size, alloc, index = 0;
	PyObject *i;

	p_size = PyList_Size(p);
	alloc = ((PyListObject *)p)->alloc;
	printf("[*] Size of the Python List = %ld\n", p_size);
	printf("[*] Allocated = %ld\n", alloc);
	while (index < p_size)
	{
		i = PyList_GET_ITEM(p, index);
		printf("Element %ld: %s\n", index, i->ob_type->tp_name);
		index++;
	}
}
