from factorial import factorial as F

def combination(n, k):
	comb = F(n)/(F(k)*F(n-k))
	return float(comb)
