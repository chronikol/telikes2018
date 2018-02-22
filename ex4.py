nums=[[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]
lat=''
n=input("dose enan arithmo: ")
while n > 0:
	for i, r in nums:
		while n >= i:
			lat=lat+r
			n=n-i
print lat
