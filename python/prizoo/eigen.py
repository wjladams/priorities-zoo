import numpy as np

def harker_fix(mat):
    """
    Performs Harkers fix on the numpy matrix mat.  It returns a copy with the fix.
    The function does not change the matrix mat.
    :param mat:
    :return:
    """
    nrows = mat.shape[0]
    ncols = mat.shape[1]
    rval = mat.copy()
    for row in range(nrows):
        val = 1
        for col in range(ncols):
            if col != row and mat[row,col]==0:
                val+=1
        rval[row,row]=val
    return(rval)

def largest_eigen(mat, error = 1e-10, use_harker = False):
    if use_harker:
        mat = harker_fix(mat)
    size = mat.shape[0]
    vec = np.ones([size])
    diff = 1
    while diff > error:
        nextv = np.matmul(mat, vec)
        nextv = nextv/sum(nextv)
        diff = max(abs(nextv - vec))
        vec = nextv
    return(vec)

def inconsistency(mat, error = 1e-10, use_harker = False):
    if use_harker:
        mat = harker_fix(mat)
    size = mat.shape[0]
    vec = np.ones([size])
    diff = 1
    while diff > error:
        nextv = np.matmul(mat, vec)
        nextv = nextv/sum(nextv)
        diff = max(abs(nextv - vec))
        vec = nextv
    nextv = np.matmul(mat, vec)
    eigenval = sum(nextv)
    ci = (eigenval-size)/(size-1)
    rval = ci/riindex(size)
    return(rval)

def riindex(n):
    if n==1:
        return(1)
    elif n==2:
        return(1)
    elif n==3:
        return(0.58)
    elif n==4:
        return(0.90)
    elif n==5:
        return(1.12)
    elif n==6:
        return(1.24)
    elif n==7:
        return(1.32)
    elif n==8:
        return(1.41)
    elif n==9:
        return(1.45)
    elif n==10:
        return(1.49)
    elif n==11:
        return(1.51)
    elif n==12:
        return(1.48)
    elif n==13:
        return(1.56)
    elif n==14:
        return(1.57)
    elif n==15:
        return(1.59)
    else:
        return(1.6)