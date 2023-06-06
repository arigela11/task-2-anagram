here the time complexity=O(N*|S|*log|S|)
 space complexity: O(N*|S|)
 operations:
 when we pass list to function(print_anagrams)
 In this function :
 1)I created one dictionary, and
 2) I  used for loop ,
 3)so every word in list  will be sorted and 
 4)check wheter the sorted_word is present in dictionary,
 5)if not present it will store sorted_word as "key" and   store (the word in list) and assign as a "value" 
  like ex: dict={act:[act,cat]}
 6) if present just append the word to list
 7)lastly it will return the list of dictionary values
 TIME COMPLEXITY:
  N=no of values in list:
  |s| is the length of string
  log|S| is lgorithm's maximum running time is proportional to the logarithm of the string size

 