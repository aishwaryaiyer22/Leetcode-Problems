import math
def spaceString(num):
    tmp = ""
    for i in xrange(num):
        tmp += " "
    return tmp  
def getNumberOfSpaces(space1, space2):
    # space1 * x + space2 *(spaces - x) = space_left
    # x * (space1 - space2) = space_left - space2 * spaces
    x = (space_left - (space2 * spaces)) / (space1 - space2)
    return x


def getString():
    global spaces
    line = ""
    if i == len(words) -1:
        spaces -= 1
        end_space = spaceString(int(space_left-spaces))
        for word in line_words:
            if spaces != 0:
                line += word + " "
            else:
                line += word
            spaces -= 1    
        line += end_space
    else:     
        spaces = max(spaces-1, 1)
        og_spaces =  spaces
        if space_left % spaces == 0:
            space = spaceString(int(space_left / spaces))
            for word in line_words:
                if spaces != 0:
                    line += word + space
                else:
                    line += word
                spaces -= 1     
            
        else:
            space1 = spaceString(int(math.ceil(space_left / spaces)))
            space2 = spaceString(int(math.floor(space_left / spaces)))
            print "uneven spaces"
            print int(math.ceil(space_left / spaces))
            print int(math.floor(space_left / spaces))
            num_big_space = getNumberOfSpaces(len(space1), len(space2))
            print num_big_space
            for word in line_words:
                if num_big_space > 0:
                    line += word + space1
                elif spaces != 0:
                    print "putting smaller space"
                    line += word + space2
                else:
                    line += word
                spaces -= 1
                num_big_space -= 1.0
            # print line      
    print len(line)        
    result.append(line)

"""
:type words: List[str]
:type maxWidth: int
:rtype: List[str]
"""
words = ["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."]
maxWidth = 30
line_words = []
result = []
i = 0
space_left = maxWidth
spaces = 0.0
while i < len(words):  
    if  len(words[i]) + spaces <= space_left :
        # print "should come here"
        line_words.append(words[i])
        spaces += 1
        space_left -= len(words[i])
        if i == len(words) -1:
            getString()
    else:
        # print line_words
        i -= 1
        getString()    
        line_words = []
        space_left = maxWidth
        spaces = 0.0   
    i += 1
print result