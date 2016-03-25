def rev_word1(s):
	return " ".join(reversed(s.split()))

def rev_word2(s):
	return " ".join(s.split()[:: -1])
	

def rev_word(s):

"""
Test for rev_word function
"""
from nose.tools import assert_equal

class ReversalTest(object):
	
	def test(self, sol):
		assert_equal(sol('     space before'), 'before space')
		assert_equal(sol('space after    '), 'after space')
		assert_equal(sol('    Hello John     how are you    '), 'you are John Hello')
		assert_equal(sol('1'), '1')
		print "ALL TEST CASES PASSED"

# Run and test
t = ReversalTest()
t.test(rev_word)
