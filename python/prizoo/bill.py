import numpy as np


def geom_avg(vals):
    """
    Compute the geometric average of a list of values.
    
    The values need not be a list, but simply anything with a len() and []
    """
    rval=1.0
    count = 0
    for val in vals:
        val = vals[count]
        if val != 0:
            rval *= val
            count+=1
    if count != 0:
        rval = pow(rval, 1.0/count)
    return(rval)

def geom_avg_mat(mat, coeffs = None):
    '''
    Computes the geometric average of the columns of a matrix.  Returns
    an np.array of dimension [nRowsOfMat], i.e. a vector.  
    
    :param mat: Must be an numpy.array of shape [nRows, nCols]
    :param coeffs:  If not None, it is a list like object with nColsOfMat elements.
    We multiply column 0 of mat by coeffs[0], column 1 of mat by coeffs[1], etc
    and then do the geometric average of the columns.  Essentially this weights the
    columns.
    '''
    """
    """
    size = mat.shape[0]
    rval = np.ones([size])
    for row in range(size):
        if np.any(coeffs):
            theRow = mat[row,:] * np.array(coeffs)
        else:
            theRow = mat[row,:]
        rval[row] = geom_avg(theRow)
    return(rval)

def bpriorities(mat, error = 1e-10):
    """
    Calculates priorities using Bill's method
    """
    size = mat.shape[0]
    vec = np.ones([size])
    diff = 1
    count=0
    while diff >= error and count < 100:
        nextv = geom_avg_mat(mat, vec)
        #nextv = nextv/max(nextv)
        diff = max(abs(nextv - vec))
        vec = nextv
        count+=1
    return(vec/sum(vec))

def gm_priorities(mat):
    '''
    Calculates the priorities using the geometric mean method
    :param mat: An numpy.array of dimension [size,size]
    '''
    rval = geom_avg_mat(mat)
    rval = rval / sum(rval)
    return(rval)