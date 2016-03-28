def anagram(s1, s2):
	s1 = s1.replace(' ', '').lower()
	s2 = s2.replace(' ', '').lower()
	
	return sorted(s1) == sorted(s2)
	


def anagram2(s1, s2):
	s1 = s1.replace(' ', '').lower()
	s2 = s2.replace(' ', '').lower()
	
	# edge case
	if len(s1) != len(s2):
		return False
	
	# dictionary
	count = {}
	
	# adding 
	for letter in s1:
		if letter in count:
			count[letter] += 1
		else:
			count[letter] = 1
			
	# subtracting
	for letter in s2:
		if letter in count:
			count[letter] -= 1
		else:
			count[letter] = 1
	
	for k in count:
		if count[k] != 0:
			return False
			
	return True
	

from nose.tools import assert_equal

class AnagramTest(object):
	
	def test(self, sol):
		assert_equal(sol('go go go', 'gggooo'), True)
		assert_equal(sol('abc', 'cba'), True)
		assert_equal(sol('hi man', 'hi     man'), True)
		assert_equal(sol('aabbcc','aabbc'), False)
		assert_equal(sol('123', '1 2'), False)
		print "All Test Cases Passed"


# Run tests
t = AnagramTest()
t.test(anagram)
