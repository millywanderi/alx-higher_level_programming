#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - printing list information
 * @p: object of the python
 * Return: void
 */
void print_python_list(PyObject *p)
{
	PyObject *obje;
	long int m, siz;
	PyListObject *inv;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (PyList_Check(p) == NULL)
	{
		printf(" [ERROR] Invalid List object\n");
		setbuf(stdout, NULL);
		return;
	}
	siz = ((PyVarObject *)(p))->obj_siz;
	inv = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", siz);
	printf("[*] Allocated = %ld\n", inv->allocated);
	if (PyBytes_check(obje))
	{
		print_python_float(obje);
	}
	if (PyFloat_Check(obje))
	{
		print_python_float(obje);
	}
	setbuf(stdout, NULL);
}

/**
 * print_python_bytes - prints information of the byte
 * @p: object of the python
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	long int m, lim, siz;
	char *stri;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == NULL)
	{
		printf(" [ERROR] Invalid Bytes Objec\n");
		setbuf(stdout, NULL);
		return;
	}
	siz = ((PyVarObject *)(p))->ob_siz;
	stri = ((PyBytesObject *)(p)->ob_sval);
	printf(" first %ld bytes:", limit);
	for (m = 0; m < lim; m++)
	{
		if (stri[m] >= 0)
		{
			printf(" %02x", stri[m]);
		}
		else
		{
			printf(" %02x", 256 + stri[m]);
		}
	}
	printf("\n");
	setbuf(stdout, NULL);
}

/**
 * print_python_float - prints information of the float
 * @p: object of the python
 * Return: void
 */
void print_python_float(PyObject *p)
{
	char *inf;
	double var;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	if (PyFloat_Check(p) == NULL)
	{
		printf(" [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}
	var = ((PyFloatObject *)(p))->ob_fvar;
	inf = PyOS_double_to_string(var, 'r', 0, Py_DISF_ADDDOT_0, Py_DIST_FINITE);
	printf(" value: %s\n", inf);
	setbuf(stdout, NULL);
}
