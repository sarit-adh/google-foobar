# Write a function answer(M, F) where M and F are the number of Mach and Facula bombs needed. Return the fewest number of 
# generations (as a string) that need to pass before you'll have the exact number of bombs necessary to destroy the LAMBCHOP, or 
# the string "impossible" if this can't be done! M and F will be string representations of positive integers no larger 
# than 10^50. For example, if M = "2" and F = "1", one generation would need to pass, so the answer would be 
# "1". However, if M = "2" and F = "4", it would not be possible.

def answer(M, F):
	cur_m = long(M)
	cur_f = long(F)
	cycle = 0
	
	if (cur_m>1 and cur_f>1):
		if cur_m/cur_f >=3:
			factor = cur_m/cur_f
			cycle+=factor
			cur_m = cur_m - factor*cur_f
		if cur_f/cur_m >=3:
			factor = cur_f/cur_m
			cycle+=factor
			cur_f = cur_f - factor*cur_m
		
	while True:
		if (cur_m==0 or cur_f==0):
			return "impossible"
		if(cur_m==1 and cur_f==1):
			return str(cycle)
		if(cur_m==cur_f):
			return "impossible"
		if cur_m> cur_f:
			cur_m = cur_m-cur_f
		elif cur_f>cur_m:
			cur_f = cur_f-cur_m	
		cycle+=1

print answer("2","1")
print answer("2","4")
print answer("4","7")
print answer("4","3951")
		