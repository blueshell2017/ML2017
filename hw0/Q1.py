def readtext(path):
    with open(path,'r') as f:
        text = f.readlines()
        return text

def index(text):
    '''
        text to index
    '''
    myindex = []
    words = text[0].strip().split(" ")
    dicts = dict()
    for temp in words:
        if dicts.get(temp) == None:
            myindex.append(temp)
            dicts[temp] = 1
        else:
            dicts[temp] += 1
    for item,temp in enumerate(myindex):
        with open("A1.txt","a") as f:
            s = str(temp)+" " + str(item) + " " + str(dicts[temp]) + "\n"
            f.write(s)
if __name__ == '__main__':
    text = readtext(r"words.txt")
    index(text)