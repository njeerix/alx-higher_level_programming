#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
void print_python_list(PyObject *p);

void print_python_list(PyObject *p)
{
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    for (Py_ssize_t i = 0; i < PyList_Size(p); ++i)
    {
	PyObject *element = PyList_GetItem(p, i);
	printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
	if (PyBytes_Check(element))
	    print_python_bytes(element);
	else if (PyList_Check(element))
            print_python_list(element);
	else if (PyFloat_Check(element))
	    print_python_float(element);
    }
}

void print_python_bytes(PyObject *p)
{
   if (!PyBytes_Check(p))
   {
       fprintf(stderr, "[.] bytes object info\n");
       fprintf(stderr, " [ERROR] Invalid Bytes Object\n");
       return;
   }

   printf("[.] bytes object info\n");
   printf(" size: %ld\n", PyBytes_GET_SIZE(p));
   printf(" trying string: ");
   
   const char *bytes_string = PyBytes_AsString(p);

   if (!bytes_string)
   {
       fprintf(stderr, " [ERROR] Unable to retrieve bytes string\n");
	   return;
   }

   for (Py_ssize_t i = 0; i < PyBytes_GET_SIZE(p) && i < 10; ++i)
       printf("%02x ", (unsigned char)bytes_string[i]);

   printf("\n");
}

void print_python_float(PyObject *p)
{
    printf("[.] float object info\n");
    printf(" value: %f\n", PyFloat_AsDouble(p));
}

int main(void)
{
	return 0;
}
