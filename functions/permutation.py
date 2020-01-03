from factorial import factorial as F

def permutaion(n, k):
	perm = (F(n)/F(n-k))
	return float(perm)
