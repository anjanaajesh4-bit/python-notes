"""Count most frequent character"""
text="banana"
count={}   #creates an empty dictionary
for ch in text:  #goes through each character in text
    if ch in count:   #checks whether the character is already in the dictionary
        count[ch]+=1  #increments the count
    else:
        count[ch]=1   #adds new character with count 1
print(count) 

highest=0
frequent=""
for ch in count:
    if count[ch]>highest:
        highest=count[ch]
        frequent=ch
print("Most Frequent Character:",frequent)
