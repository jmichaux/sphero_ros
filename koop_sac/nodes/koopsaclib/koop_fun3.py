import numpy as np
def phi(x):
        return np.array([x[0],x[1],x[2],x[3],x[4],x[5],x[2]**3,x[2]**2*x[3],x[2]**2*x[4],x[2]**2*x[5],x[2]**2,x[2]*x[3]**2,x[2]*x[3]*x[4],x[2]*x[3]*x[5],x[2]*x[3],x[2]*x[4]**2,x[2]*x[4]*x[5],x[2]*x[4],x[2]*x[5]**2,x[2]*x[5],x[3]**3,x[3]**2*x[4],x[3]**2*x[5],x[3]**2,x[3]*x[4]**2,x[3]*x[4]*x[5],x[3]*x[4],x[3]*x[5]**2,x[3]*x[5],x[4]**3,x[4]**2*x[5],x[4]**2,x[4]*x[5]**2,x[4]*x[5],x[5]**3,x[5]**2,1])

def dphidx(x):
    return np.array([[ 1, 0,       0,       0],
    [ 0, 1,       0,       0],
    [ 0, 0,       1,       0],
    [ 0, 0,       0,       1],
    [ 0, 0,       0,       0],
    [ 0, 0,       0,       0],
    [ 0, 0,  3*x[2]**2,       0],
    [ 0, 0, 2*x[2]*x[3],    x[2]**2],
    [ 0, 0, 2*x[2]*x[4],       0],
    [ 0, 0, 2*x[2]*x[5],       0],
    [ 0, 0,    2*x[2],       0],
    [ 0, 0,    x[3]**2, 2*x[2]*x[3]],
    [ 0, 0,   x[3]*x[4],   x[2]*x[4]],
    [ 0, 0,   x[3]*x[5],   x[2]*x[5]],
    [ 0, 0,      x[3],      x[2]],
    [ 0, 0,    x[4]**2,       0],
    [ 0, 0,   x[4]*x[5],       0],
    [ 0, 0,      x[4],       0],
    [ 0, 0,    x[5]**2,       0],
    [ 0, 0,      x[5],       0],
    [ 0, 0,       0,  3*x[3]**2],
    [ 0, 0,       0, 2*x[3]*x[4]],
    [ 0, 0,       0, 2*x[3]*x[5]],
    [ 0, 0,       0,    2*x[3]],
    [ 0, 0,       0,    x[4]**2],
    [ 0, 0,       0,   x[4]*x[5]],
    [ 0, 0,       0,      x[4]],
    [ 0, 0,       0,    x[5]**2],
    [ 0, 0,       0,      x[5]],
    [ 0, 0,       0,       0],
    [ 0, 0,       0,       0],
    [ 0, 0,       0,       0],
    [ 0, 0,       0,       0],
    [ 0, 0,       0,       0],
    [ 0, 0,       0,       0],
    [ 0, 0,       0,       0],
    [ 0, 0,       0,       0]])

def dphidu(x):
    return np.array([[       0,       0],
            [       0,       0],
            [       0,       0],
            [       0,       0],
            [       1,       0],
            [       0,       1],
            [       0,       0],
            [       0,       0],
            [    x[2]**2,       0],
            [       0,    x[2]**2],
            [       0,       0],
            [       0,       0],
            [   x[2]*x[3],       0],
            [       0,   x[2]*x[3]],
            [       0,       0],
            [ 2*x[2]*x[4],       0],
            [   x[2]*x[5],   x[2]*x[4]],
            [      x[2],       0],
            [       0, 2*x[2]*x[5]],
            [       0,      x[2]],
            [       0,       0],
            [    x[3]**2,       0],
            [       0,    x[3]**2],
            [       0,       0],
            [ 2*x[3]*x[4],       0],
            [   x[3]*x[5],   x[3]*x[4]],
            [      x[3],       0],
            [       0, 2*x[3]*x[5]],
            [       0,      x[3]],
            [  3*x[4]**2,       0],
            [ 2*x[4]*x[5],    x[4]**2],
            [    2*x[4],       0],
            [    x[5]**2, 2*x[4]*x[5]],
            [      x[5],      x[4]],
            [       0,  3*x[5]**2],
            [       0,    2*x[5]],
            [       0,       0]])
