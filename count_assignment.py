"""Count frequency of each character"""

# text="python"
# count={}
# for ch in text:
#     if ch in count:
#         count[ch]+=1
#     else:
#         count[ch]=1
# print(count)


"""Find the least frequent character"""

# text="banana"
# count={}
# for ch in text:
#     if ch in count:
#         count[ch]+=1
#     else:
#         count[ch]=1
# print(count)
# least=999
# frequent=""
# for ch in count:
#     if count[ch]<least:
#         least=count[ch]
#         frequent=ch
# print("Least frequent character :",frequent)


"""Find the character appearing more than once"""

# text="banana"
# count={}
# for ch in text:
#     if ch in count:
#         count[ch]+=1
#     else:
#         count[ch]=1
# print(count)
# appearance=[]
# for ch in count:
#     if count[ch]>1:
#         appearance.append(ch)
# print("Character appearing more than once:",appearance)

"""Find the character appearing exactly once"""

# text="kerala"
# count={}
# for ch in text:
#     if ch in count:
#         count[ch]+=1
#     else:
#         count[ch]=1
# print(count)
# appearence=[]
# for ch in count:
#     if count[ch]==1:
#         appearence.append(ch)
# print("Character appearing exactly once:",appearence)

"""Find the first repeated character"""

# text="apple"
# count={}
# for ch in text:
#     if ch in count:
#         count[ch]+=1
#     else:
#         count[ch]=1
# print(count)
# repeated=""
# for ch in count:
#     if count[ch]>1:
#         repeated=ch
# print("The first repeated character is:",repeated)

"""Find the first non repeated character"""

# text="alaska"
# count={}
# for ch in text:
#     if ch in count:
#         count[ch]+=1
#     else:
#         count[ch]=1
# print(count)
# non_repeated=""
# for ch in count:
#     if count[ch]==1:
#         non_repeated=ch
#         break
# print("The first non repeated character is:",non_repeated)

"""Find the second most frequent character"""

# text="banana"
# count={}
# for ch in text:
#     if ch in count:
#         count[ch]+=1
#     else:
#         count[ch]=1
# print(count)
# heighest=0
# second=0
# second_frequent=""
# for ch in count:
#     if count[ch]>heighest:
#         second=heighest
#         second_frequent=ch
#         heighest=count[ch]
#     elif count[ch] > second:
#         second=count[ch]
#         second_frequent=ch
        
# print("Second Most Frequent Character is:",second_frequent)

"""Find the Number of Unique Characters"""

# text="banana"
# unique={}
# for ch in text:
#     unique[ch] = 1
# print(len(unique))

"""Find the Most Frequent Number"""

# numbers=[2,3,5,9,2,5,2,9,2]
# count={}
# for num in numbers:
#     if num in count:
#         count[num]+=1
#     else:
#         count[num]=1
# print(count)
# heighest=0
# frequent=0
# for num in count:
#     if count[num]>heighest:
#         heighest=count[num]
#         frequent=num
# print("The most Frequent number:",count[num])
        
"""Find the Least Frequent Number"""

# numbers=[2,3,1,5,3,2,8,1,3,5]
# count={}
# for num in numbers:
#     if num in count:
#         count[num]+=1
#     else:
#         count[num]=1
# print(count)
# least=999
# frequent=""
# for num in count:
#     if count[num]<least:
#         least=count[num]
#         frequent=num
# print(frequent)

"""Most Purchased Product"""

# orders = ["Laptop", "Mouse", "Laptop", "Keyboard","Mouse", "Laptop"]
# count={}
# for order in orders:
#     if order in count:
#         count[order]+=1
#     else:
#         count[order]=1
# count[order]
# most=0
# frequent=""
# for order in count:
#     if count[order] > most:
#         most=count[order]
#         frequent=order
# print("The Most Purchased Product:",frequent)

"""The Most common Vote"""

# votes = ["A", "B", "A", "C", "B", "A", "B"]
# count={}
# for vote in votes:
#     if vote in count:
#         count[vote]+=1
#     else:
#         count[vote]=1
# print(count)
# most=0
# frequent=""
# for vote in count:
#     if count[vote]>most:
#         most=count[vote]
#         frequent=vote
# print("The Most common Vote:",frequent)

"""The Most common Word"""

# text = "apple mango apple orange mango apple"
# words=text.split()
# count={}
# for word in words:
#     if word in count:
#         count[word]+=1
#     else:
#         count[word]=1
# print(count)
# common=0
# frequent=""
# for word in count:
#     if count[word]>common:
#         common=count[word]
#         frequent=word
# print("The Most Frequent Word:",frequent)

"""The Most Common Student Name"""

# names = ["Anu", "Rahul", "Anu", "Meera", "Rahul", "Anu"]
# count={}
# for name in names:
#     if name in count:
#         count[name]+=1
#     else:
#         count[name]=1
# print(count)
# common=0
# frequent=""
# for name in count:
#     if count[name]>common:
#         common=count[name]
#         frequent=name
# print("The most common name is:",frequent)

"""The most common Error Code"""

errors = [404, 500, 404, 403, 404, 500]
count={}
for error in errors:
    if error in count:
        count[error]+=1
    else:
        count[error]=1
common=0
frequent=""
for error in count:
    if count[error]>common:
        common=count[error]
        frequent=error
print("The most common Error code is:",frequent)
