def sepaEvenOdd(l):
  even=[]
  odd=[]
  for x in l:
    if x%2==0:
      even.append(x)
    else:
      odd.append(x)
  return even, odd

l=[10,11,12,16,31]
even,odd=sepaEvenOdd(l)
print(even)
print(odd)