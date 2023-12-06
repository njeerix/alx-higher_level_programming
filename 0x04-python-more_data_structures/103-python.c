#include <Python.h>
void print_python_list(PyObject *p) {
	Py_ssize_t size, alloc, i;
	PyObject *item;
	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Python list info\n");
	print("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	for (i = 0; i < size; i++) {
		item = Pylist_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
void print_python_bytes(PyObject *p) {
	Py_ssize size, i;
	char *str;
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p)) {
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; i++) {
		printf("02x ", (unsigned char)str[i]);
	}
	printf("\n");
}
int main(void) {
	PyObject *s, *b, *l;
	Py_Initialize();
	s = PyBytes_FromString("Hello");
	b = PyBytes_FromStringAndSize("\xff\xf8\x00\x00\x00\x00\x00\x00", 8);
	l = PyList_New(2);
	PyList_SetItem(l, 0, s);
	PyList_SetItem(l, 1, b);
	print_python_bytes(s);
	print_python_bytes(b);
	print_python_list(l);
	Py_DECREF(s);
	Py_DECREF(b);
	Py_DECREF(l);
	Py_Finalize();
	return 0;
}
