#---------------------------------Newton-Raphson method package--------------------------------------------------------
#Author: Suman Saurabh
#email: sumanan047@gmail.com
#-----------------------------------------------------------------------------------------------------------------
# Working with the package
# 1.Define the function f first
# 2.Run the function newton
#--------------------------------parameters and the defaults in the package---------------------------------------
f = lambda t: t**3+4*(t**2)-10  # defining the required function

# the solver function is defined here
def newton(f,seed,itern=10,rounding=3,diff_tol=0.1,sol_tol=1E-10):
    """
The function newton has several parameters all of them has been talked about a bit below:
                1. f: It is the function/equation to be solevd, the user of the package must define this 
                function before calling the solver package "newton".
                2. seed: It is the initial estimation of the value of root for the equation. It can be set at any
                value, but user should be aware of the complexities that can arise because of the 
                problems of discontinuous nature of function. Hence, this value should be set with an intelligent 
                guess or some amount of ground work
                3. itern: Sets the number of iteration the loop in the function newton should run if the 
                convergence has not been reached upto defined solution tolerance, default value of 1E-10.
                4.rounding: It is the rounding of number of signficant digits the solution and numbers generated 
                in function are reduced to for printing, default value is 3 decimal places.
                5. diff_tol: It is the forward difference value used in estimation of derivaive of the function
                in the neighborhood of the seed value, default value is 0.1. It can be easily made smaller to 
                achieve convergence quicker.
                6. sol_tol: This parameter checks if the seed value in each iteration is changing more than 
                this threshold value or not. If the chnage in seed values is smaller than this value, the loop 
                in the package exits and the prompt that convergence has been achieved is printed. Hence, 
                changing this values is essential to achieve more precise convergence. 
                  
    """
    soln=[] # empty list to save the seed values for comparison to check if they are chnaging in each iteration
    print(30*"*","Newton's method convergence visualization",30*"*")
    print("f(n)","n",sep="\t")
    print(20*"*")
    for i in range(1,itern):
        seed = seed - (f(seed)*(diff_tol))/(f(seed+diff_tol)-f(seed)) # execution fo the newton's method
        soln.append(seed)
        # to check if the convergence upto a certain tolerance is acheived
        if (len(soln)>2) and ((soln[-2]-soln[-1])<(sol_tol)):
            print("Convergene of solution achieved! after",i,"iterations! at seed value of:",round(seed,rounding))
            break
        print(round(f(seed),rounding),round(seed,rounding),sep="\t") # serves for pretty printing
    return seed