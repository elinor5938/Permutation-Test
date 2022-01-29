# Permutation test for comparing between two histograms distribution :
The parameters include: the distribution mean , median , variance , interquartile range. Skewness and kurtosis . 

the idea behinds the test works as follows:
1.	Observed substruction between two histograms descriptive parameters were calculated.
2.	The two histograms’ data was shuffled .
3.	Random 500 observations were taken to represent the examined simulations.
4.	Descriptive parameters were calculated for each random simulation .
5.	Substruction between the two randomly histograms’ descriptive statistics was calculated  .
6.	Steps 4 and 5 were done 9999 times .
7.	Pvalue was calculated for each parameter by calculating the sum of occurrence where the subsection between the random histograms parameters values were greater or equal to the observed difference and then the divided by 10000 .
