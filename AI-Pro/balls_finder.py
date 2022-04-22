import inputfunc
import copy

#print(inputfunc.biglist)
#checker=["A","B","C","D"]

def initial_state():
    return inputfunc.biglist

def is_goal(s):
  for i in s:
    if i[0] == i[1]:
      if i[1] == i[2]:
        if i[2] == i[3]:
          continue
        else:
          return False
          break
      else:
        return False
        break  
    else:
      return False
      break 
  return True
      
def findtop(s):
  for j in range(0,4):
    if s[j] == '_':
      continue
    else:
      return s[j]
      break
  return '_'



def successors(s):
  succ_list=[]
  indexchange = -1
  for b in s:
    indexchange += 1
    stkclone = copy.deepcopy(b)
    if b == ['_','_','_','_']:
      continue
    pick = findtop(b)
    targetidx = -1

    for y in s:
      targetidx+=1
      up = 0
      stgclone = copy.deepcopy(s)
      targetclone = copy.deepcopy(y)
      if targetclone.count('_') == 0:
        continue
      if indexchange == targetidx:
        continue
      for e in range(0,4):
        if y[e] == '_':
          up = e
  
      if pick != findtop(y):
        if findtop(y)=='_':
          stkclone[b.index(pick)] = targetclone[up]
          targetclone[up] = pick
          stgclone[indexchange] = stkclone
          stgclone[targetidx] = targetclone
          succ_list.append(stgclone)
          continue
        else:
          continue
      
      if pick == findtop(y):
        stkclone[b.index(pick)] = targetclone[up]
        targetclone[up] = pick
        stgclone[indexchange] = stkclone
        stgclone[targetidx] = targetclone
        succ_list.append(stgclone)
        continue
        
      
  #print(succ_list)
  return succ_list

    #if is_goal == False: 
    #  for i in clone:
    #   clone[i+5].append(clone[i][1])
    #   clone[i][1].pop

  # elif len(is_goal) == 0:
    # is_goal.append(s)

   #elif is_goal[0] != flask[0]:
    # break
      
    #elif is_goal[0] == flask[0]:
    # is_goal.append(flask[0])
    
  
  
      
