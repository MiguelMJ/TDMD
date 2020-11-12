import sys

def nfmc(N,M):
	if (N == 0):
		return 1
	sum = 0
	for m in range(1,1+M):
		sum += nfmc(N-1, m)
	return sum

if(__name__ == '__main__'):
	if(len(sys.argv) != 3):
		N = 3
		M = 3
	else:
		N = int(sys.argv[1])
		M = int(sys.argv[2])
	total = nfmc(N, M)
	print('N: {}\nM: {}\nNº de FMC: {}'.format(N,M,total))		