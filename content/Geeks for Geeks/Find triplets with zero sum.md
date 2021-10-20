Title: Find triplets with zero sum
Status: published
Date: 2021-10-21 17:30
Tags: practice, basic, two-pointers, sorting-searching
Author: José A. Romero
Summary: Find a triplet of numbers in an array summing up to zero.

[TOC]

## <i class="fa fa-book-open title-icon"></i>&nbsp;Problem statement
<a href="https://practice.geeksforgeeks.org/problems/find-triplets-with-zero-sum/1/" target="_blank">Here</a> is the problem statement.

## <i class="fa fa-lock title-icon"></i>&nbsp;Constraints

$1 \le n \le 10^4$  
$-10^6 \le A_i \le 10^6$

Expected Time Complexity: $\mathcal{O}\left(n^2\right)$  
Expected Auxiliary Space: $\mathcal{O}(1)$

## <i class="fa fa-pencil-alt title-icon"></i>&nbsp;Explanation

### <i class="fa fa-lightbulb title-icon"></i>&nbsp;Brute Force Approach

A naive approach to solve this problem would be to consider all the triplets present in the array and check if any of them sums up to zero.

Below is the implementation in pseudocode of the above approach:  
```
for i = 0 to n - 1 do
	for j = i + 1 to n - 1 do
		for k = j + 1 to n - 1 A do
			if A[i] + A[j] + A[k] = 0 then
				return true
return false
```

* **Time complexity:** $\mathcal{O}\left(n^3\right)$  
    Because those three nested loops are required.

* **Auxiliary space:** $\mathcal{O}(1)$  
    No extra space required.

* **Final verdict:** not a valid solution due to our constraints.

### <i class="fa fa-lightbulb title-icon"></i>&nbsp;Hashing Approach

Now it's time for a question: do we really need to check all the triplets?, of course not! (otherwise this interview question would be meaningless &#x1F602;). A second approach is due to if $x + y + z = 0$ then $x = -y - z$. So we just need to find a triplet where the first number is the opposite of the sum of second and third number. We could do this using almost eny kind of hashing data structure.

Below is the implementation in pseudocode of the above approach:  
```
H <- hash_map
for i = 0 to n - 1 do
	for j = i + 1 to n - 1 do
		if H.contains(-A[i] - A[j]) then
			return true
	H.insert(A[ i ])
return false
```

* **Time complexity:** $\mathcal{O}\left(n^2\right)$  
    Because those two nested loops are required and time complexity for checking if a value exists in a hash map is $\mathcal{O}(1)$.

* **Auxiliary space:** $\mathcal{O}(n)$  
    Because at the end the hash map will contain $n$ elements.

* **Final verdict:** not a valid solution due to our constraints.


### <i class="fa fa-lightbulb title-icon"></i>&nbsp;Two Pointers Approach

Another approach, and our final approach, is sorting the array $A$ and then try to find a triplet $(i, j, k)$ such that $0 \le i \lt j \lt k \lt n$ and $A_i + A_j + A_k = 0$. Given any triplet $(i, j, k)$ such that $0 \le i \lt j \lt k \lt n$ then there are just $3$ options we need to check.

$$A_i + A_j + A_k \left\{\begin{array}{cl}
= 0 & \text{We found a solution!}\\
\lt 0 & \text{Then } A_i + A_j + A_k \le A_i + A_{j+1} + A_k\\
\gt 0 & \text{Then } A_i + A_j + A_k \ge A_i + A_j + A_{k-1}
\end{array}\right.$$

Following the above idea, we could iterate through every $0 \le i \lt n$ and search for a valid pair of $(j, k)$ in the range $[i+1,n-1]$.

Demonstration&nbsp;&nbsp;<span class="circle-plus closed" data-toggle="collapse" data-target="demonstration">
<span class="circle">
	<span class="horizontal"></span>
	<span class="vertical"></span>
</span>
</span>

<div markdown="1" id="demonstration" class="expandable demonstration">
If there is no sulution, it's pretty obviuos that we don't find a solution, because we check the sum of $3$ numbers and it will never be $0$.

Let's assume there exists a triplet $(i, j, k)$ such that $0 \le i \lt j \lt k \lt n$ and $A_i + A_j + A_k = 0$. It is obviuos that our algorithm will reach $i$ after some steps (maybe none). After that, it is also straightforward to see that we will reach either $j$ or $k$, because we iterate through every $i \lt v \lt n$ and $i \lt j,k$.

* Suppose we reach $j$ before $k$, then with the right pointer we are at position $k \lt p \lt n$ and $\forall p: k \lt p \lt n \implies A_i + A_j + A_p \ge 0$ because $A_i + A_j + A_k = 0$ and $A_k \le A_p$ given that the array is sorted.  
  So either we found another valid solution with triplet $(i, j, p)$ or we have to decrease our right pointer until we reach $k$ or another valid solution.
* Suppose we reach $k$ before $j$, then with the left pointer we are at position $i \lt p \lt j$ and $\forall p: i \lt p \lt j \implies A_i + A_p + A_k \le 0$ because $A_i + A_j + A_k = 0$ and $A_p \le A_j$ given that the array is sorted.  
  So either we found another valid solution with triplet $(i, p, k)$ or we have to increase our left pointer until we reach $j$ or another valid solution.
</div>

## <i class="fa fa-keyboard title-icon"></i>&nbsp;Solution

Here is the solution code of this problem in multiple languages.

<div class="tab">
	<button class="tablinks" data-target="C-code">C</button>
	<button class="tablinks" data-target="Cpp-code" id="defaultOpen">C++</button>
	<button class="tablinks" data-target="Csharp-code">C#</button>
	<button class="tablinks" data-target="Python-code">Python</button>
	<button class="tablinks" data-target="Java-code">Java</button>
	<button class="tablinks" data-target="Javascript-code">Javascript</button>
</div>

<div id="C-code" class="tabcontent">
```c
{! Geeks for Geeks/Find triplets with zero sum/solution.c !}
```
</div>

<div id="Cpp-code" class="tabcontent">
```cpp
{! Geeks for Geeks/Find triplets with zero sum/solution.cpp !}
```
</div>

<div id="Csharp-code" class="tabcontent">
```csharp
{! Geeks for Geeks/Find triplets with zero sum/solution.cs !}
```
</div>

<div id="Python-code" class="tabcontent">
```python
{! Geeks for Geeks/Find triplets with zero sum/solution.py !}
```
</div>

<div id="Java-code" class="tabcontent">
```java
{! Geeks for Geeks/Find triplets with zero sum/solution.java !}
```
</div>

<div id="Javascript-code" class="tabcontent">
```javascript
{! Geeks for Geeks/Find triplets with zero sum/solution.js !}
```
</div>

* **Time complexity:** $\mathcal{O}\left(n^2\right)$  
    Because those two nested loops are required and all internal operations are $\mathcal{O}(1)$.

* **Auxiliary space:** $\mathcal{O}(1)$  
    No extra space needed.

* **Final verdict:** valid solution!

## <i class="fa fa-comment-dots title-icon"></i>&nbsp;Final thoughts

This is a pretty simple and easy problem to understand two pointers approach.