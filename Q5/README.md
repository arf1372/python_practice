# Question 5
consider there is a picture from some biological tissues.
after some process that image is converted to a matrix which its contains 0,1.
the cancer parts values is one and regular areas are zero.
the question asks to implement a function in which it can find the biggest influenced area.
your function should accept a single `numpy.array` and should return a dictionary which contains the cancer-contained pixels as tuple.

## Example
**Input**
```
#0 1 2 3 4 5 6 7 8 9
[
[0,0,0,0,0,0,0,0,0,0], # 0
[0,0,0,0,0,0,0,0,0,0], # 1
[0,0,0,0,0,0,0,0,0,0], # 2
[0,0,0,1,1,0,0,0,0,0], # 3
[0,0,1,1,1,1,0,0,0,0], # 4
[0,0,0,1,1,0,0,0,0,0], # 5
[0,0,0,0,0,0,0,0,0,0], # 6
[0,0,0,0,0,0,0,0,0,0], # 7
[0,0,0,0,0,0,0,0,0,0], # 8
[0,0,0,0,0,0,0,0,0,0]  # 9
]
```
**Output**
```
{
  (3,3),(3,4),
  (4,2),(4,3),(4,4),(4,5),
  (5,3),(5,4),
}
```
