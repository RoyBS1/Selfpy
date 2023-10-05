
def sort_anagrams(list_of_strings):
    anagram = []
    not_anagrams = []
    for word in list_of_strings:
        word = sorted(word)
        anagram.append(word)
    anagram.sort()
    #print(anagram)
    
    new_list = []
    for word1 in anagram:
        if word1 not in new_list:
            new_list.append(word1)
    #print(new_list)
    new_list2 = []
    for word2 in list_of_strings:
        word2 = sorted(word2)
        if(word2 in new_list):
            new_list2.append(word2)
    print(new_list2)
    
    
list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
sort_anagrams(list_of_words)
