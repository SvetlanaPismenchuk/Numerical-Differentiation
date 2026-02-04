# Numerical Differentiation Experiment

## Numerical Differentiation Function

The function `dydx` estimates the derivative of a function using the central difference formula:

f'(x₀) ≈ (f(x₀ + h) − f(x₀ − h)) / (2h)

It works by checking the function a little ahead and a little behind the point, then finding the slope. This usually gives a better estimate than just using one side.


## Numerical Experiment

This program finds the derivative of

g(x) = 3x⁴ − 3x² + 12x

for many x-values. It compares two ways of doing it.

The loop method calculates each value one at a time. It works fine but gets slow when there are a lot of points.

The vectorized method uses NumPy arrays to compute everything at once, which is faster.


## Results

After running it, the vectorized version was clearly faster. The loop took longer since it had to repeat the calculation many times. This shows that vectorization is better for large data, even though both methods give similar results.


## Acknowledgements
I’d like to acknowledge Dr. Rumpf for his support in strengthening my understanding of math in Python. I also used Google AI and ChatGPT to clarify how certain functions work and to correct syntax errors.
