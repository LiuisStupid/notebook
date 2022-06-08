# notebook

install jetpack via SDK manager: https://blog.csdn.net/weixin_42622181/article/details/107217994

install CPPAD and IPOPT solver: https://blog.csdn.net/qq_35632833/article/details/116233665
how to stabilize the postion of target person(avoiding mismatch):
K_mean for 1-D depth information:   https://gist.github.com/lobrien/0f95b690644a862fb4dadb73afb7753b

how to ensure that cuda works inside docker(OSError: libcurand.so.10: cannot open shared object file: No such file or directory): https://stackoverflow.com/questions/64482976/oserror-libcurand-so-10-cannot-open-shared-object-file-no-such-file-or-direct

problem(ImportError: /usr/lib/aarch64-linux-gnu/libcudnn.so.8: file too short): do not use the lastest version of l4t-ml!!!!!!!!!!!!!!!!


advantage of MPC controller: optimizer makes controll of underactuated syetem better. 




no reference list of points possible in our situation, so we predict the movement of target based on the movement of vehicle, with which we can have a list of reference points


we only have terms of input(velocity and angular velocity) in our objective function, so we can't get state information or set some constraints to states directly.

introduce APF in objective function is difficult because we do not have terms of states(transformation is necessary):

   1.traditional repulsive function is not suitable:   pow( 1/distance - 1/detected_range), value if obj function changes too quick.
   
   2.modified the structure of APF. divided repulsive field in x and y direction, give them different weight respectively,with which the problem of local minimum can be addressed.
   
   3.For the fomula of repulsive field, give biases  :    1/x   ->    1/x+0.3,     to solve the problem of infinity when x->0.
   
   
We have only 2 controll viariables ,adaptive matrix of Q and R may worth a try, lossen the weight for (like theta) when in collision avoidance. 







For uncertainty:

 2. In the paper, the data is applied to estimate safety, whose order of magnitudes is 10e-6(15), We do not need that high accuracy for person tracking.In another word, the application of uncertainty may not have much influence on my algorithm, and it's negligible.
 3. In the paer, it's based on the conservation of conditions .For instance the distance between human joints are constant. we do not have such reference.  
 4. many time steps(psuedo code in 10) to obtain data of (for example distance between human and camera) - >Bootstrapping(14 Figure6), maybe impossible for our real time system?
 5. How to map from uncertainty directly to one dangerous failure per 10e4 hours(15)




trying to introduce odom for some auxiliary functions.
