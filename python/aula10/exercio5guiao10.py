def invertnumber(n):
	return inumber(n,0)
	
def inumber(n,r)
	if n==0
		return r
	rs=n%10
	ds = n//10
	
	return inumber(ds,r*10+rs)
