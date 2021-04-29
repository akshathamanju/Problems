words = ["cat", "act", "dog" , "tac" ]

# This is effectively an adjacency list, but we use a map as the implementation.
# anagram_neighbors_map = {}
for word1 in words:
  anagram_neighbors_map[word1] = []
  for word2 in words:
    if word1 != word2:
      # If word1 equals word2 when sorted they are anagrams.
      if sorted(word1) == sorted(word2):
        anagram_neighbors_map[word1].append(word2)

for word in anagram_neighbors_map:
  print(word,anagram_neighbors_map[word])

# This prints
# "cat" : ["act", "tac"]
# "act" : ["cat", "tac"]
# "dog" : []
# "tac" : ["act", "cat"]