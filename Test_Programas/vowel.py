str="Rohit is a very good boy and never disrespect anyone"
vowel=['a','e','i','o','u']
new_vow=[]

for c in str:
  if c in vowel:
    if c not in new_vow:
      new_vow.append(c)

print("Vowels in Strings are",new_vow)