def BinaryTree(r):
	return [r,[],[]]
def insertLeft(root,newBranch):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1,[newBranch,t,[]])
	else:
		root.insert(1,[newBranch,[],[]])
	return root
	
def insertRight(root,newBranch):

def getRootVal(root):

def setRootVal(root,newVal):

def getLeftChild(root):