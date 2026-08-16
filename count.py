"""Count most frequent character"""
text="banana"
count={}
for ch in text:
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1
print(count) 

highest=0
frequent=""
for ch in count:
    if count[ch]>highest:
        highest=count[ch]
        frequent=ch
print("Most Frequent Character:",frequent)
