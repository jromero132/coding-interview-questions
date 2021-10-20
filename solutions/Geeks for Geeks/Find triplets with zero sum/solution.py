class Solution:   
	def findTriplets(self, array, n):
		array.sort()
		for i in range(n):
			left, right = i + 1, n - 1
			while left < right:
				sum_ = array[ i ] + array[ left ] + array[ right ]
				if sum_ == 0:
					return True
				elif sum_ < 0:
					left += 1
				else:
					right -= 1
		return False