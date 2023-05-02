def fa(i):
 print ("now i =",i, " address i is ",id (i))   
 if i<0:
  print ("i<0")   
  return None
 if i == 0:
  print ("i=0")   
  return 1
 
 return i * fa(i-1)

print (fa(5.6))



