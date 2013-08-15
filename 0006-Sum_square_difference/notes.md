The problem can be represented as the difference of the sums of two series
(with the second series being squared before the difference is taken).
We will refer to the first sum as S_A and the second as S_B.

![equation](http://latex.codecogs.com/gif.latex?S_A%3D%5Cdisplaystyle%5Csum%5Climits_%7Bi%3D0%7D%5En%20i%5E2)

![equation](http://latex.codecogs.com/gif.latex?S_B%3D%5Cdisplaystyle%5Csum%5Climits_%7Bi%3D0%7D%5En%20i)

So our formula is:

![equation](http://latex.codecogs.com/gif.latex?S%20%3D%20S_A%20-%20S_B%5E2)

The closed form for each is:

![equation](http://latex.codecogs.com/gif.latex?S_A%20%3D%20%5Cfrac%7Bn%28n&plus;1%29%282n&plus;1%29%7D%7B6%7D)

![equation](http://latex.codecogs.com/gif.latex?S_B%20%3D%20%5Cfrac%7Bn%28n&plus;1%29%7D%7B2%7D)

So the closed form of the solution can be written as:

![equation](http://latex.codecogs.com/gif.latex?S%20%3D%20%5Cfrac%7Bn%28n&plus;1%29%282n&plus;1%29%7D%7B6%7D%20-%20%5Cleft%28%5Cfrac%7Bn%28n&plus;1%29%7D%7B2%7D%5Cright%29%5E2)

With some algebraic manipulation, this can be reduced down to:

![equation](http://latex.codecogs.com/gif.latex?S%20%3D%20%5Cfrac%7B-n%283n%5E3&plus;4n%5E2-1%29%7D%7B6%7D)

Which should be the closed form solution to the problem.
