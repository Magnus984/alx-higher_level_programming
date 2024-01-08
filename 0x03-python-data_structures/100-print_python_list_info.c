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
	long int length = PyList_Size(p);
	PyListObject *list_obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", length);
	printf("[*] Allocated = %li\n", list_obj->allocated);
	for (i = 0; i < length; i++)
		printf("Element %i: %s\n", i, Py_TYPE(list_obj->ob_item[i])->tp_name);
}

