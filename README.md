A simple program to use the Collatz conjecture up to an arbitrary value, providing at the end the number with the largest number of steps to converge to 1 and how many steps it took.

Collatz_Opt uses python dictionary to significantly improve the speed of this process by looking up past solved values when iterating through the range of numbers provided. This does come with the trade off of the dictionary growing very large, which may cause memory issues at high values being assessed.

Plotting is available in both by uncommenting the matplotlib lines.
