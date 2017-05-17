# I noticed that my crawler was wasting a lot of time visiting the same pages
# over and over, so I made a set, visited, where I'm storing URLs I've already
# visited. How can I trim down the amount of space taken up by visited?

class Trie:
    def __init__(self):
        self.root_node = {}

    def check_present_and_add(self, word):
        current_node = self.root_node
        is_new_word = False

        for char in word:
            print '===word===', word
            print 'char',char
            if char not in current_node:
                is_new_word = True
                current_node[char] = {}

            # for each new character, add a dictionary within a dictionary
            # or if already in the dictionary, add a new key    
            current_node = current_node[char]
            print "current node", current_node

        if "End of Word" not in current_node:
            is_new_word = True
            current_node["End of Word"] = {}
            print "current node", current_node



        return is_new_word

trie = Trie()
trie.check_present_and_add('donut.net')
trie.check_present_and_add('dogood.org')
trie.check_present_and_add('dog.com')
trie.check_present_and_add('dog.com/about')
trie.check_present_and_add('dog.com/pug')
trie.check_present_and_add('dog.org')
