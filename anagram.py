def group_anagrams(list_words):
    anagram_dict = {}
    for word in list_words:
    
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    
    
    return list(anagram_dict.values())

# Example usage
if __name__ == "__main__":
    print("enter the list")
    
    list_words=list(map(str,input().split()))

    output_sets = group_anagrams(list_words)
    print(output_sets)

