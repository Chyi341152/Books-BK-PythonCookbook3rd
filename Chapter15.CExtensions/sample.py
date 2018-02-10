'''
C functions that have been compiled into a shared library or DLL
shared library compatible with python interpreter
    
    ctypes:
        -- is a foreign function library for Python. It provides C compatible data types, and allows calling functions in DLLs or shared library.
    Attach-ing the type signatures is critical if you want to make Python pass the right kinds of arguments and convert data correctly (if you don't do this, not only will the code not work, but you might cause the entire interpreter process to crash)

'''

import ctypes # A foreign function library for Python
import os
 
# Try to locate the .so file in the same directory as this file
_file = 'library.so' # shared library
_path = os.path.join(*(os.path.split(__file__)[:-1] + (_file,)))
_mod = ctypes.CDLL(_path) # Loading shared libraries
 
# int gcd(int, int)
gcd = _mod.gcd
gcd.argtypes = (ctypes.c_int, ctypes.c_int) # containing the input arguments to a function
gcd.restype = ctypes.c_int # the return type 
print(gcd, gcd.argtypes, gcd.restype)

# int in_mandel (double, double, int)
in_mandel = _mod.in_mandel
in_mandel.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_int)
in_mandel.restype = ctypes.c_int 
print(in_mandel, in_mandel.argtypes, in_mandel.restype)

# int divide(int, int, int *)
_divide = _mod.divide 
_divide.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
_divide.restype = ctypes.c_int
print(_divide, _divide.argtypes, _divide.restype)

def divide(x, y):
    # c_int object can eb mutated 
    rem = ctypes.c_int()
    quot = _divide(x, y, rem)
    return quot, rem.value # .value attribute can be used to either retrieve or change the value as desired 

# void avg(double *, int n)
# Define a special type for the 'double *' argument 
class DoubleArrayType:
    # 
    def from_param(self, param):
        typename = type(param).__name__
        if hasattr(self, 'from_' + typename):
            return getattr(self, 'from_' + typename)(param)
        elif isinstance(param, ctypes.Array):
            return param
        else:
            raise TypeError("Can't convert %s" % typename)
    
    # Cast from array.array objects
    def from_array(self, param):
        if param.typecode != 'd':
            raise TypeError('must be an array of doubles')
        ptr, _ = param.buffer_info()
        return ctypes.cast(ptr, ctypes.POPINTER(ctypes.c_double))
    
    # Cast from lists/tuples
    def from_list(self, param):
        val = ((ctypes.c_double)*len(param))(*param)
        return val 
    
    from_tuple = from_list 
    
    # Cast from a numpy array 
    def from_ndarray(self, param):
        return param.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    
DoubleArray = DoubleArrayType()
_avg = _mod.avg 
_avg.argtypes = (DoubleArray, ctypes.c_int)
_avg.restype = ctypes.c_double 

def avg(values):
    return _avg(values, len(values))

# struct Point { }
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double),
               ('y', ctypes.c_double)]

# double distance(Point *, Point *)
distance = _mod.distance
distance.argtypes = (ctypes.POINTER(Point), ctypes.POINTER(Point))
distance.restype = ctypes.c_double
