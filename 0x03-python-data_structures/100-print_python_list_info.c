#include <Python.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, idx = 0;
	PyObject *element;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);
	while (idx < size)
	{
		element = PyList_GET_ITEM(p, idx);
		printf("Element %ld: %s\n", idx, element->ob_type->tp_name);
		idx++;
	}
}
