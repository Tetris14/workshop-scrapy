def anagrams(str, list):
    i = 0
    res = []
    while i < len(list):
        if sorted(str) == sorted(list[i]):
            res.append(list[i])
        i += 1
    print(res)
    
anagrams("abab", ["abba", "bbaa", "cbaa", "abcd"])