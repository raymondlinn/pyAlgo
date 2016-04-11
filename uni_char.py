def uni_char(s):
	return len(set(s)) == len(s)
	
def uni_char2(s):
	
	chars = set()
	
	for let in s:
		if let in chars:
			return False;
		else:
			chars.add(let)
	
	return True
		

from nose.tools import assert_equal

class TestUniqueChar(object):
	def test(self, sol):
		assert_equal(sol(''), True)
		assert_equal(sol('goo'), False)
		assert_equal(sol('abcdefg'), True)
		print 'All Test Cases Passed'
	
t = TestUniqueChar()
t.test(uni_char2)