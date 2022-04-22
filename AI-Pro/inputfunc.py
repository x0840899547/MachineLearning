biglist=[]
def inputfuction():
  global biglist
  f_1=[]
  f_2=[]
  f_3=[]
  f_4=[]
  f_5=["_","_","_","_"]
  f_6=["_","_","_","_"]
  biglist=[f_1,f_2,f_3,f_4,f_5,f_6]

  balls=["A","B","C","D"]

  try:
    for q in range(4):
      b1, b2, b3, b4 = input(str(q+1)+"row: ").split()

      if b1 and b2 and b3 and b4 in balls:
        f_1.append(b1)      
        f_2.append(b2)
        f_3.append(b3)
        f_4.append(b4) 
        #print(biglist)
      else:
        print('Wrong Type of Input')   
        break
    
  except ValueError:
    print('Wrong Number of Inputs')
