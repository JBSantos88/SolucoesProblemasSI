class State:
  def __init__(self, parent, position, left, right):
    self.parent = parent
    self.position = position
    self.left = left
    self.right = right

def showState(s):
  print(s.position, ",", s.left, ",", s.right)

def initialState():
  return State(None, 0, 1, 1)

def goal(s):
  return s.left == 0 and s.right == 0

def moveLeft(s):
  return State(s, 0, s.left, s.right)

def moveRight(s):
  return State(s, 1, s.left, s.right)

def vacuum(s):
  if(s.position == 0):
    return State(s, s.position, 0, s.right)
  return State(s, s.position, s.left, 0)

def expand(s):
  ret = []
  ret.append(moveLeft(s))
  ret.append(moveRight(s))
  ret.append(vacuum(s))
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
