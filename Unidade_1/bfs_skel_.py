class State:
  def __init__(self, parent, cd, md, ce, me, margem):
    self.parent = parent
    self.cd = cd
    self.md = md
    self.ce = ce
    self.me = me
    margem = margem

def showState(s):
  print("("+ s.cd, s.md, s.ce, s.me, s.margem + ")")

def initialState():
    return State(None,3,3,0,0,0)

s = initialState()
showState(s)
#def goal(s):
#  return False
#
#def action(s):
#  return State(s)
#
#def expand(s):
#  ret = []
#  #ret.append(action(s))
#  return ret
#
#def showPath(s):
#  if(s == None):
#    return
#  showPath(s.parent)
#  showState(s)
#
#queue = []
#
#def enqueue(s):
#  queue.append(s)
#
#def dequeue():
#  return queue.pop(0)
#
#s = initialState()
#enqueue(s)
#
#while(queue):
#  s = dequeue()
#
#  if(goal(s)):
#    showPath(s)
#    break
#
#  children = expand(s)
#  for child in children:
#    enqueue(child)

