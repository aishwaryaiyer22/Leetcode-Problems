a = [1,2,3]
k = 4
start = 0
max_words = 0
end = start
curr_length = 0
curr_wc = 0
while(end < len(a)):
    curr_length += a[end]
    curr_wc += 1
    end += 1
    while (curr_length > k and start < end):
        curr_length -= a[start]
        start += 1
        curr_wc -= 1
    if(curr_wc > max_words):
        max_words = curr_wc
print max_words