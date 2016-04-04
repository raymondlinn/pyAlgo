def rev_word1(s):
	return " ".join(reversed(s.split()))

def rev_word2(s):
	return " ".join(s.split()[:: -1])
	

def rev_word3(s):
	
	words = []
	length = len(s)
	spaces = [' ']
	
	i = 0
	
	# strings loop
	while i < length:
	
		if s[i] not in spaces:
			
			word_start = i
			
			# words loop
			while i < length and s[i] not in spaces:
				
				i += 1
			
			words.append(s[word_start:i])
		
		i += 1
	
	#return " ".join(reversed(words))
	return final_output(words)
	
def final_output(words):
	
	rev = ""
	length = len(words)
	
	for i in range(length):
		rev += words[length - 1 - i]
		if i < length - 1 :
			rev += ' '
	
	return rev

"""
Test for rev_word function
"""
from nose.tools import assert_equal

class ReversalTest(object):
	
	def test(self, sol):
		assert_equal(sol('     space before'), 'before space')
		assert_equal(sol('space after    '), 'after space')
		assert_equal(sol('    Hello John     how are you    '), 'you are how John Hello')
		assert_equal(sol('1'), '1')
		print "ALL TEST CASES PASSED"

# Run and test
t = ReversalTest()
t.test(rev_word3)

