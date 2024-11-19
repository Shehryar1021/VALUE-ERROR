
try :
  num=int(input("ENTER YOUR NUMBER :"))
  print(num)
except ValueError as ex:
  print("EXCEPTION : ",ex)
 
  print("I AM OUTSIDE THE TRY BLOCK")