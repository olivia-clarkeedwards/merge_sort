# Merge sort on standard inputs
Implements merge sort on a sequence of names with two attributes, and prints out the list of names whose first attributes are 0 and second attributes are sorted (in ascending order)

University assignment to gain familiarity with using standard input (assignment was submitted to an automarker) and also to gain familiarity with sorting algorithms. Descriptions from the assignment below.

## Input: 

The input consists of a number of lines. Each line contains a name, a 0/1-valued attribute, and another attribute whose value is a positive integer. The names and the attributes are separated by space ‘ ’. For example:

William 1 21    
Mary 0 25  
John 1 19  
Lingling 0 21  
Rachel 0 14  
Adam 1 17  
Vivian 0 21  
Raj 1 19  

## Output:

The output also consists of a number lines. Each line contains a name. (1) Only names whose first attribute is 0 is listed; (2) The names are listed so that their corresponding second attributes are in ascending order; and (3) Whenever there are two names whose second attributes are the same, arrange the names in the same order as they appear in the input list. For example, the following output should correspond to the input above:

Rachel  
Lingling  
Vivian  
Mary  

