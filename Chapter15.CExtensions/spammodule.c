/* spammodule.c */

// Since Python may define some pre-processor definitions which affict the standard headers on some systems. you must include Python.h before any standard headers are inclued 
#include <Python.h> // pulls in the Python API

static PyObject *
spam_system(PyObject *self, PyObject *args)
{
	const char *command;
	int sts;

	if (!PyArg_ParseTuple(args, "s", &command))
		return NULL;
	sts = system(command);
	return PyLong_FromLong(sts);
}
