#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - prints basic information about python list
 * @p: python object
 * Return: no return value
 */
void print_python_list_info(PyObject *p)
{
	int i;
	char *type_name;
	PyObject *element;
	long int length = PyList_Size(p);
	PyListObject *list_obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", length);
	printf("[*] Allocated = %li\n", list_obj->allocated);
	for (i = 0; i < length; i++)
	{
		element = list_obj->ob_item[i];
		type_name = Py_TYPE(element)->tp_name;
		printf("Element %i: %s\n", i, type_name);
	}
}

