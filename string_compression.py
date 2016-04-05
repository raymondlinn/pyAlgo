# run length compression algorithm
def compression(s):
	
	r = ""
	l = len(s)
	
	if l == 0:
		return ""
	
	if l = 1:
		return s+"1"
	
	last = s[0]
	cnt = 1
	i = 1
	
	while i < l:
		
		if s[i] == s[i-1]:
			cnt +=1
		else:
			r = r +s[i-1] + str(cnt)
			cnt = 1
		
		i += 1
	
	r = r + s[i -1] + str(cnt)
	
	return r
	




from nose.tools import assert_equal

class TestStringCompression(object):
	
	def test(self, sol):
		assert_equal(sol(''), '')
		assert_equal(sol('AABBCC'), 'A2B2C2')
		assert_equal(sol('AAABCDDDDD'), 'A2B1C2D5')
		print 'ALL TEST CASES PASSED'
		
t = TestStringCompression()
t.test(commpression)