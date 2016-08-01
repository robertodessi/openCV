import time
import sys

def aux(toAnagram, results, output):
	if(len(toAnagram)==1):
		print "qui"
		return toAnagram
	else:
		leng = len(toAnagram)-1

		for x in xrange(leng, -1, -1):
			#output = toAnagram[x]
			#output = output + aux(toAnagram[:-1], results, output)
			print aux(toAnagram[:-1], results, output)
		#results.append(output)	
		
		#print results

#def aux2(toAnagram, result, output):
def aux2(toAnagram, result = "", res = []):	
	if len(toAnagram) == 0:
		return result
	else:
		for x in xrange(len(toAnagram)):
			temp = toAnagram.replace(toAnagram[x], "", 1)
			res.append(aux2(temp, result + toAnagram[x]))
	if len(toAnagram) == 1 :
		print result+toAnagram


def t(toAnagram, result = ""):
	if len(toAnagram) == 0:
		return [result]
	else:
		res = []
		for x in xrange(len(toAnagram)):
			res.extend(t(toAnagram[0:x] + toAnagram[x+1:], result+toAnagram[x]))
		return res
		

aux2("ciao")
print "==========="
print t("ciao")


