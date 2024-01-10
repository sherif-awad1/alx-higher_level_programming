#include <stdio.h>
#include <Python.h>

/**
 * print_pyb - Prints bytes information
 * @p: Python Object
 */
void print_pyb(PyObject *p)
{
char *str;
long int s, i, hit;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

s = ((PyVarObject *)(p))->ob_size;
str = ((PyBytesObject *)p)->ob_sval;

printf("  size: %ld\n", s);
printf("  trying string: %s\n", str);

if (s >= 10)
hit = 10;
else
hit = s + 1;

printf("  first %ld bytes:", hit);

for (i = 0; i < hit; i++)
if (str[i] >= 0)
printf(" %02x", str[i]);
else
printf(" %02x", 256 + str[i]);

printf("\n");
}

/**
 * print_python_list - Prints list information
 * @p: Python Object
 */
void print_python_list(PyObject *p)
{
long int s, i;
PyListObject *sll;
PyObject *obj;

s = ((PyVarObject *)(p))->ob_size;
sll = (PyListObject *)p;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", s);
printf("[*] Allocated = %ld\n", sll->allocated);

for (i = 0; i < s; i++)
{
obj = ((PyListObject *)p)->ob_item[i];
printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
if (PyBytes_Check(obj))
print_pyb(obj);
}
}
