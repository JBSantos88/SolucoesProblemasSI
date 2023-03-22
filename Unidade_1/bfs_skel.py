class State:
  def __init__(self, parent):
    self.parent = parent

def showState(s):
  pass

def initialState():
  return State(None)

def goal(s):
  return False

def action(s):
  return State(s)

def expand(s):
  ret = []
  #ret.append(action(s))
  return ret

def showPath(s):
  if(s == None):
    return
  showPath(s.parent)
  showState(s)

queue = []

def enqueue(s):
  queue.append(s)

def dequeue():
  return queue.pop(0)

s = initialState()
enqueue(s)

while(queue):
  s = dequeue()

  if(goal(s)):
    showPath(s)
    break

  children = expand(s)
  for child in children:
    enqueue(child)
