def aux2(toAnagram, result = "", res = []):	
	if len(toAnagram) == 0:
		return result
	else:
		for x in xrange(len(toAnagram)):
			temp = toAnagram.replace(toAnagram[x], "", 1)
			res.append(aux2(temp, result + toAnagram[x]))
	return res


def t(toAnagram, result = ""):
	if len(toAnagram) == 0:
		return [result]
	else:
		res = []
		for x in xrange(len(toAnagram)):
			res.extend(t(toAnagram[0:x] + toAnagram[x+1:], result+toAnagram[x]))
		return res
		

print(aux2("ciao"))
print "==========="
print t("ciao")


