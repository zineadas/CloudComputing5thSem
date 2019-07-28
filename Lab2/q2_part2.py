def readFile(stopWords):
    l=[]
    with open('text.txt','r') as f:
        for line in f:
            for word in line.split():
                word=word.replace('.','')
                word=word.replace(',','')
                word=word.lower()
                if word not in stopWords:
                    l.append(word)
    return l

def topTenWords(l):
    freq_dict={}
    for x in l:
        freq_dict[x]=l.count(x)
    sorted_freq=sorted(freq_dict.items(), key=lambda x: x[1],reverse=True)
    if len(sorted_freq)>=10:
        return sorted_freq[:10]
    else:
        return sorted_freq

def main():
    stopWords = ['is', 'the', 'it', 'and', 'of', 'in','a']
    l=readFile(stopWords)

    print("Top 10 Words except stop words are: ")
    lis=topTenWords(l)
    for x in lis:
        print(x[0],x[1])


if __name__=="__main__":
    main()