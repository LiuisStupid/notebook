# notebook

install jetpack via SDK manager: https://blog.csdn.net/weixin_42622181/article/details/107217994

install CPPAD and IPOPT solver: https://blog.actorsfit.com/a?ID=01750-54c29171-dce7-4d58-8d95-41ca6367d5dc

how to stabilize the postion of target person(avoiding mismatch):
K_mean for 1-D depth information:   https://gist.github.com/lobrien/0f95b690644a862fb4dadb73afb7753b




no reference list of points possible in our situation, so we predict the movement of target based on the movement of vehicle, with which we can have a list of reference points


we only have terms of input(velocity and angular velocity) in our objective function, so we can't get state information or set some constraints to states directly.

introduce APF in objective function is difficult because we do not have terms of states(transformation is necessary):

   1.traditional repulsive function is not suitable:   pow( 1/distance - 1/detected_range), value if obj function changes too quick.
   
   2.modified the structure of APF. divided repulsive field in x and y direction, give them different weight respectively,with which the problem of local minimum can be addressed.
   
   3.For the fomula of repulsive field, give biases  :    1/x   ->    1/x+0.3,     to solve the problem of infinity when x->0.
   
   
We have only 2 controll viariables ,adaptive matrix of Q and R may worth a try, lossen the weight for (like theta) when in collision avoidance. 







For uncertainty:
 1. Hard for me to understand the whole content in paper and literature, there is too much content about statistics, which im not very good at, I may need to spend more     time on it .
 2. In the paper, the data is applied to estimate safety, whose order of magnitudes is 10e-6, We do not need that high accuracy for person tracking.In another word, the application of uncertainty may not have much influence on my algorithm, and it's negligible.
 3. In the paer, it's based on the conservation of conditions .For instance the distance between human joints are constant. we do not have such reference.  
