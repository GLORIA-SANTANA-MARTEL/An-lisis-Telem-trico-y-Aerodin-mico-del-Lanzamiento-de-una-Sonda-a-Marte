TEST GAUSS

def Test_Gauss():
     A =  array([[1, 1, 1],
                [1, -1, -1], 
                [1, -1, 1]])
     b =  array( [1, 2, 3 ] ) 
     x = Gauss( A, b )
     xsol = array([ 1.5, -1., 0.5])
     print("my Error =", xsol - x )
     print("scipy Error =", xsol - solve(A, b) ) 

     A =  array( [ [1, 2, 3] , [1, -2, -3] , [1, -2, 3] ] )
     b =  array( [1, 2, 3 ] ) 
     x = Gauss( A, b )
     xsol = array([ 1.5, -0.5,  1/6.])
     print("my Error =", xsol - x ) 
     print("scipy Error =", xsol - solve(A, b) ) 

     

