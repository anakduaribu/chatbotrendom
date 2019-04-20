def lastOccurence(string, size): 
    listLO = [-1 for i in range(256)]
  
    for i in range(size): 
        if (ord(string[i])-32>=65 and ord(string[i])-32<=90):
            listLO[ord(string[i])-32] = i
        if (ord(string[i])+32>=97 and ord(string[i])+32<=122):
            listLO[ord(string[i])+32] = i
        listLO[ord(string[i])] = i; 
  
    return listLO 
  
def boyerMoore(text, pattern): 
    count = 0
    solusi = []
    size_text = len(text)
    size_pattern = len(pattern)
    listLO = lastOccurence(pattern, size_pattern)  
    shift = 0
    max_ratio =  0

    while(shift <= size_text-size_pattern and max_ratio != 1):
        count = 0
        j = size_pattern-1

        while (j>=0 and (pattern[j] == text[shift+j] or ord(pattern[j])+32 == ord(text[shift+j]) or ord(pattern[j])-32 == ord(text[shift+j]) or ord(pattern[j])<65 or ord(pattern[j])>122)): 
            j -= 1
            count += 1
  
        if j<0: 
            if (shift+size_pattern<size_text):
                shift += size_pattern-listLO[ord(text[shift+size_pattern])]
            else:
                shift += 1
        else: 
            shift += max(1, j-listLO[ord(text[shift+j])]) 
       
        if (count/size_text > max_ratio):
            max_ratio = count/size_text
            
    return max_ratio
        
def main(): 
    text = "Apakah chatBot itu manusia?"
    pattern = "apakah chAtbot itu"
    found = boyerMoore(text, pattern) 
    print(found*100)
    print(len(text))
  
if __name__ == '__main__': 
    main() 