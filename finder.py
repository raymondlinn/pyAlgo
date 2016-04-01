import collections

def finder(arr1, arr2):
	
	# sort those arrays
	arr1.sort()
	arr2.sort()
	
	for num1, num2 in zip(arr1, arr2):
		if num1 != num2:
			return num1
	
	return arr1[-1]

def finder2(arr1, arr2):
	
	d = collections.defaultdict(int)
	
	for num in arr2:
		d[num] += 1
		
	for num in arr1:
		if d[num] == 0:
			return num
			
		else:
			d[num] -= 1
			
			
# finder3()third approach would be sum of arr2 substract from sum of arr1 will give
# missing num in those arrays. But too long of array or precision of those numbers
# in the arrays will be troublesome

def finder4(arr1, arr2):
	
	result = 0
	
	# perform XOR between the "Zero" and numbers in two arrays
	for num in arr1 + arr2: # arr1 + arr2 is concatenating two list
		result ^= num
		print result
	
	return result

finder4([1,2,3,4,5,6,7],[1,2,3,4,6,7])


"""
from nose.tools import assert_equal

class TestFinder(object):
	
	def test(self, sol):
		assert_equal(sol([5,5,7,7],[5,7,7]), 5)
		assert_equal(sol([1,2,3,4,5,6,7],[3,1,4,7,6,5]), 2)
		assert_equal(sol([5,2,4,3],[2,3,5]), 4)
		print "All Test Cases Passed"
	
t = TestFinder()
t.test(finder)
"""