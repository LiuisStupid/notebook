# notebook

install jetpack via SDK manager: https://blog.csdn.net/weixin_42622181/article/details/107217994

install CPPAD and IPOPT solver: https://blog.actorsfit.com/a?ID=01750-54c29171-dce7-4d58-8d95-41ca6367d5dc

how to stabilize the postion of target person(avoiding mismatch):
K_mean for 1-D depth information:   https://gist.github.com/lobrien/0f95b690644a862fb4dadb73afb7753b




no reference list of points possible in our situation, so we predict the movement of target based on the movement of vehicle, with which we can have a list of reference points


we only have terms of input(velocity and angular velocity) in our objective function, so we can't get state information or set some constraints to states directly.

introduce APF in objective function is difficult because we do not have terms of states(transformation is necessary):
   1.traditional repulsive function is not suitable:   pow( 1/distance - 1/detected_range), value if obj function changes too quick.

