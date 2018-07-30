import time
import timeit
import numpy as np

def create_numpy_arrays():
    """Creating NumPy arrays."""
    #List to 1D array
    print(np.array([2,3,4]))

    #List to 2D array
    print(np.array([(2,3,4),(5,6,7)]))

    #Empty array
    print(np.empty(5))
    print(np.empty((5,4,3)))

    # Array of 1s
    print(np.ones((5,4)))

    # Specifying the datatype
    print(np.ones((5,4), dtype=np.int_))

    # Array of 0s
    print(np.zeros((5,4)))

def gen_random_number():
    """Generating random numbers."""
    # Generate an array full of random numbers, uniformly smapled from [0.0,1.0)
    print(np.random.random((5,4))) # pass in a size tuple
    print(np.random.rand(5,4)) # function arguments (not a tuple)

    # Sample numbers from a Gaussian (normal) distribution
    print(np.random.normal(size=(2,3))) # "standard normal" (mean = 0, s.d. = 1)
    print(np.random.normal(50, 10, size=(2,3))) # change mean to 50 and s.d. to 10

    # Random integers
    print("a single integer")
    print(np.random.randint(10)) # a single integer in [0,10)
    print("a single integer")
    print(np.random.randint(0, 10)) # same as above, specifying [low, high) explicit
    print("1d array")
    print(np.random.randint(0, 10, size=5)) # 5 random integers as a 1D array
    print("2d array")
    print(np.random.randint(0, 10, size=(2,3))) # 2x3 array of random integers

def array_attributes():
    """Array attributes."""

    a = np.random.random((5,4)) # 5x4 array of random numbers
    print(a)
    print(a.shape)
    print(a.shape[0]) #number of rows
    print(a.shape[1]) #number of columns
    print(len(a.shape)) #number of dimensions

    print(a.size) #number of elements in the array (= product of the shape)
    print(a.dtype) #data type of the values in the array

def operation_on_array():
    """Operations on array."""
    np.random.seed(693) # seed the random number generator
    a = np.random.randint(0, 10, size=(5,4)) # 5x4 random integers in [0,10)
    print("Array:\n", a)

    # Sum of all elements
    print("Sum of all elements:", a.sum())

    # Iterate over rows, to compute sum of each column
    print("Sum of each column:\n", a.sum(axis=0))

    # Iterate over columns, to compute sum of each row
    print("Sum of each row:\n", a.sum(axis=1))

    # Statistics: min, max, mean (across rows, cols, and overall)
    print("Minimum of each column:\n", a.min(axis=0))
    print("Maximum of each row:\n", a.max(axis=1))
    print("Mean of all elements:", a.mean()) #leave out axis arg.

    # Find the maximum and its index in array
    # Might be useful: https://docs.scipy.org/doc/numpy/reference/routines.sort.html
    a = np.array([9, 6, 2, 3, 12, 14, 7, 10], dtype=np.int32)  # 32-bit integer array
    print("Array:", a)
    print("Maximum value:", a.max())
    print("Index of max.:", a.argmax()) # Return the index of the maximum value in given 1D array.

#==============================================
# Time measure
def time_measure():
    """Using time function."""
    t1 = timeit.default_timer()
    print("ML4T")
    t2 = timeit.default_timer()
    print("The time taken by print statement is ", t2 - t1, " seconds")

def how_long(func, *args):
    """Execute function with given arguments, and measure execution time."""
    t0 = time.time()
    result = func(*args) # all arguments are passed in as-is
    t1 = time.time()
    return result, t1-t0

def manual_mean(arr):
    """Compute mean (average) of all elements in the given 2D array."""
    sum = 0
    for i in range(0, arr.shape[0]):
        for j in range(0,arr.shape[1]):
            sum = sum + arr[i,j]
    return sum/arr.size

def numpy_mean(arr):
    """Compute mean (average) using NumPy."""
    return arr.mean()

def time_test():
    """Function called by time_test."""
    nd1 = np.random.random((1000,10000)) # use a sufficiently large arrays

    # Time the two functions, retrieving results and execution time
    res_manual, t_manual = how_long(manual_mean, nd1)
    res_numpy, t_numpy = how_long(numpy_mean, nd1)
    print("Manual: {:-6f} ({:.3f} secs.) vs. NumPy: {:.6f} ({:.3f} secs.)".format(res_manual, t_manual, res_numpy, t_numpy))

    # Make sure both give us the same answer (upto some precision)
    assert abs(res_manual - res_numpy) <= 10e-6, "Results aren't equal!"

    # Compute speedup
    speedup = t_manual / t_numpy
    print("Numpy mean is ", speedup, " times faster than manual for ones.")

#==============================================

def access_elements():
    """Accessing array elements."""
    a = np.random.rand(5,4)
    print("Array:\n",a)

    # Accessing element at position (3,2)
    element = a[3,2]
    print(element)

    # Slicing
    # Element in defined range
    print(a[0, 1:3])

    #Top-left corner
    print(a[0:2, 0:2])

    # Note: Slice n:m:t specifies a range that starts at n, and stops before m, in steps of size t
    print(a[:,0:3:2]) #will select columns 0,2 for every row

    # Assigning a value to a particular location
    a[0,0] = 1
    print("\nModified (replace one element):\n",a)

    # Assigning a single value to an entire row
    a[0,:] = 2
    print("\nModified (replace a row with a single value):\n", a)

    # Assigning a list to a column in an array
    a[:,3] = [1,2,3,4,5]
    print("\nModified (replace a column with a list):\n",a)

    # accessing using list of indices
    a = np.random.rand(5)
    indices = np.array([1,1,2,3])
    print(a)
    print(a[indices])

    # Getting all the element that are less than the mean
    a = np.array([(20,25,10,23,26,32,10,5,0),(0,2,50,20,0,1,28,5,0)])
    print(a)

    # calculating the mean
    mean = a.mean()
    print(mean)

    # masking
    print(a[a<mean])

    # Changing the values less than the mean to the mean
    a[a<mean] = mean
    print(a)

def arithmetic_operations():
    """Arithmetic operations."""
    a = np.array([(1,2,3,4,5),(10,20,30,40,50)])
    print("Original array a:\n", a)

    # Multiply a by 2
    print("\nMultiply a by 2:\n", 2*a)

    # Divide a by 2
    print("\nDivide a by 2:\n", a/2.0)

    # Add two arrays
    b = np.array([(100,200,300,400,500),(1,2,3,4,5)])
    print("\nOriginal array a:\n",a)
    print("\nOriginal array b:\n",b)
    print("\nAdd a + b:\n", a+b) #same with subtraction

    # Multiply a by b
    print("\nMultiply a * b:\n", a*b)

    # Divide a by b
    print("\nDivide a / b:\n", a/b)

if __name__ == "__main__":
    # create_numpy_arrays()
    # gen_random_number()
    # array_attributes()
    # operation_on_array()
    # time_measure()
    # time_test()
    # access_elements()
    arithmetic_operations()
