This project focuses on solving the Tower of Hanoi problem and using the computation times to analyse exponential computation. 
Tower_of_Hanoi.py solves the TOH problem under 0 constraints.
Time_TOH.py times TOH.py for every inetegral value of N (number of discs) and plots the data. 

The data collected using Time_TOH.py was fed into function fitting programmes (https://wwww.mycurvefit) to generate an approximate function for the computation time for integral values of N. 
The functions collcted, listed below were used to estimate times for higher values of N (values for which my computer is too slow and I am too impatient). 



Analysis results:

y = 0.001603698 - (-1.130191e-7/-0.6775888)*(1 - e^(+0.6775888*x)) (Exponential)

y = 258680100000.00003*e^(-(x - 97.7404)^2/(2*10.29855^2)) (Gaussian)
y = 9137501 + (0.01914009 - 9137501)/(1 + (x/57.58763)^17.61528) (4PL - Symmetrical Sigmoidal)
y = d + (a - d)/(1 + (x/c)^b)^m (5PL - Assymetrical sigmoidal)
y = 6.900517 - 3.312393*x + 0.4952936*x^2 - 0.0287213*x^3 + 0.0005640618*x^4 (Quadratic regression)
y = -7.527687 + 4.517271*x - 0.9351295*x^2 + 0.08581233*x^3 - 0.003576079*x^4 + 0.00005524505*x^5 (Quintic Regression)

Natural Cubic Spline
Akima Cubic Spline


