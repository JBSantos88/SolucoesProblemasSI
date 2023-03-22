lab = [
  ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x' ],
  ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x' ],
  ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x' ],
  ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x' ],
  ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x' ],
  ['x', ' ', 'G', ' ', ' ', ' ', ' ', ' ', ' ', 'x' ],
  ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x' ],
  ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x' ],
  ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x' ],
  ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x' ],
  ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x' ],
  ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x' ]
]


class State:

  def __init__(self, parent, linha, coluna):
    self.parent = parent
    self.linha = linha
    self.coluna = coluna


caminho  = []

def showState(s):
  print(f"Linha : {s.linha} / coluna: {s.coluna}")
  


def initialState():
  return State(None, 1, 1)


def goal(s):
  return s.linha == 6 and s.coluna == 3
  

def actionEsquerda(s):
  return State(None, s.linha, s.coluna -1)


def actionDireita(s):
  return State(s, s.linha, s.coluna + 1)


def actionCima(s):
  return State(s, s.linha + 1, s.coluna)


def actionBaixo(s):
  return State(s, s.linha - 1, s.coluna)


def expand(s):
  ret = []
  if (lab[s.linha][s.coluna] == 'x'):
    return []
  ret.append(actionDireita(s))
  ret.append(actionEsquerda(s))
  ret.append(actionCima(s))
  ret.append(actionBaixo(s))

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