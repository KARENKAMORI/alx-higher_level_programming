#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - PyBytesObject function
 *
 * @p: PyObject input
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t s = 0, i = 0;
	char *strn = NULL;

	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	if (PyBytes_AsStringAndSize(p, &strn, &s) != -1)
	{
		printf("  size: %zd\n", s);
		printf("  trying string: %s\n", strn);
		printf("  first %zd bytes:", s < 10 ? s + 1 : 10);
		while (i < s + 1 && i < 10)
		{
			printf(" %02hhx", strn[i]);
			i++;
		}
		printf("\n");
	}
}

/**
 * print_python_list - PyListObject function
 *
 * @p: PyObject input
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *item;
	int i = 0;

	if (PyList_CheckExact(p))
	{
		size = PyList_Size(p);

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		while (i < size)
		{
			item = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			i++;
		}
	}
}
