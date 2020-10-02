class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
        self.isLeaf = True
class PrefixCodeTree(Node):
    def __init__(self):
        self.root = None
    def insert(self,codeword, symbol):
        if(self.root == None):
            self.root = Node(None)
        nodeTemp = self.root
        for elem in codeword:
            if(elem == 0):
                if(nodeTemp.l == None):
                    nodeTemp.l = Node(None)
                nodeTemp.isLeaf = False
                nodeTemp = nodeTemp.l
            else:
                if(nodeTemp.r == None):
                    nodeTemp.r = Node(None)
                nodeTemp.isLeaf = False
                nodeTemp = nodeTemp.r
            nodeTemp.v = symbol
    def getData(self,root, code):
      return root.l if(code == '0') else root.r

    def decode(self, encodedData, datalen):
        encodedData = int.from_bytes(encodedData, byteorder='big')
        encodedData = (bin(encodedData)[2:])
        result = []
        nodeTemp = self.root
        i = 0
        while(i <= datalen):
            if(nodeTemp.isLeaf == True):
                result.append(nodeTemp.v)
                nodeTemp = self.root
                i = i-1
            else:
                nodeTemp = self.getData(nodeTemp, encodedData[i])
            i = i +1
        return ''.join(result)
