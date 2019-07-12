def equal(a,b,c):
   if a == b:
      print("True")
   elif b == int(c):
      print("True")
   elif int(c) == a:
      print("True")
   else:
      print("False")

equal(6,5,5)
equal(6,5,"5") #with string

