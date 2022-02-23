def getW(alph,n):
	if n==1:
		return[ch for ch in alph]
		
		#n =2
		
	ws = getW(alph, n -1) #[ch for ch in alph]
	return [w + c for w in ws for c in alph]
