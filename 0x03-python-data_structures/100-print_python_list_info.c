#include <python.h>

void print_python_list_info(PyObject *p)
{
	const char *type_name;
	PyObject *element;
	long int length = PyList_Size(p);
	PyListObject *list_obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", length);
	printf("[*] Allocated Memory = %li\n", list_obj->allocated);
	for (i = 0; i < length; i++)
	{
		element = list_obj->ob_item[i];
		type_name = Py_TYPE(element)->tp_name;
		printf("Element %d: %s\n", i, type_name);
	}
}

