# multi-drone-quiz

## Method
I have used the method mentioned in the paper "Distance Transforms of Sampled Functions" (given with the question).

We initialise two grids by setting the locations of the obstacles to 0 and others to inf. One grid will be used for maintaining the locations of the obstacles and the other for the distances.

Then we solve the 1D problem for each row. I have taken v[0] to be -1 as we don't know the location of the first obstacle unlike the feature map in the paper (where every point on the grid has a well defined function). After calculating the lower envelope of the parabolas we simply calculate the distance to the nearest obstacle for each point in a row. If a row has no obstacles, we have skipped evaluating the distances for that row.

Then we solve the 1D problem for each column. Since we have already done the row-wise calculation, we don't need to set v[0] to -1 and can simply follow the approach of the paper. But when we calculate the distance, we add the square of the y-distance to the distance at the nearest lower envelope and compare it with the existing distance at the point. We choose the lower one among the two distances.