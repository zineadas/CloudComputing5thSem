def readFile():
    l=[]
    with open('text.txt','r') as f:
        for line in f:
            for word in line.split():
                word=word.replace('.','')
                word=word.replace(',','')
                word=word.lower()
                l.append(word)
    return l

def topTenWords(l):
    freq_dict={}
    for x in l:
        freq_dict[x]=l.count(x)
    sorted_freq=sorted(freq_dict.items(), key=lambda x: x[1],reverse=True)
    return sorted_freq[:10]

def main():
    l=readFile()
    print("Top 10 Words are: ")
    lis=topTenWords(l)
    for x in lis:
        print(x[0],x[1])


if __name__=="__main__":
    main()