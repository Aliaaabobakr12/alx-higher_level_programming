#include <Python.h>
#include <stdio.h>
#include <floatobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p) {
    Py_ssize_t size, alloc, i;
    const char *type;

    if (!PyList_Check(p)) {
        printf("[*] Python list info\n  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size, alloc);

    for (i = 0; i < size; i++) {
        type = Py_TYPE(PyList_GetItem(p, i))->tp_name;
        printf("Element %ld: %s\n", i, type);

        if (strcmp(type, "bytes") == 0) {
            print_python_bytes(PyList_GetItem(p, i));
        } else if (strcmp(type, "float") == 0) {
            print_python_float(PyList_GetItem(p, i));
        }
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;

    if (!PyBytes_Check(p)) {
        printf("[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("[.] bytes object info\n  size: %ld\n  trying string: %s\n", size, str);

    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++) {
        printf("%02x", str[i] & 0xFF);
        if (i < size - 1) {
            printf(" ");
        }
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    double value;

    if (!PyFloat_Check(p)) {
        printf("[.] float object info\n  [ERROR] Invalid Float Object\n");
        return;
    }

    value = PyFloat_AsDouble(p);
    printf("[.] float object info\n  value: %f\n", value);
}
