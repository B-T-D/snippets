/* Quicksort implementation in C */

	/* For IRL sorting: <stdlib.h> has void qsort(...args...), which quicksorts an array with elements of any type */

#include <stdio.h>
#include <assert.h>

/* qsort: sort v[left]...v[right] into increasing order */
void qsort(int v[], int left, int right)
{
	int i, last;
	void swap(int v[], int i, int j); //function prototype is allowed to be inside another function
	
	if (left >= right) /* base case--array with fewer than two element is already sorted */
		return;
	swap(v, left, (left + right) / 2 ); 
	last = left;
	for (i = left+1; i <= right; i++)
		if (v[i] < v[left])
			swap(v, ++last, i);
	swap(v, left, last); /* put back partition element */
	qsort(v, left, last-1); /* Recursive case--recursively quicksort each partitioned half */
	qsort(v, last+1, right);
}

void swap(int v[], int i, int j) /* This can work without pointers because the array is passed in as an argument. The function then mutates the array. You couldn't just pass int i and int j and swap their values in place in the calling code. You'd be changing copies of the values. You can pass pointers to the values to change the values themselves (and therefore not need to make a copy of them)--this is an example of how you could use C's manualness to be more memory-efficient than python. See p. 95 ("Because of call by value..."). */
{
	int temp;
	temp = v[i];
	v[i] = v[j];
	v[j] = temp;
}

int main()
{	
	int i;
	int nums[5] = {5, 2, 3, 4, 1};
	int expected_nums[5] = {1, 2, 3, 4, 5};

	qsort(nums, 0, 4); /* Args for left and right need to be indices of first and last elements in the list, for this simple version */

	for (i = 0; i <= 4; ++i)
		assert(nums[i] == expected_nums[i]);
	printf("Assertions ok\n");
}
