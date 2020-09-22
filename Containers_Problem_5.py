

# favourite musicians and favourite songs of them


fav_mus = {"Sean Price": ["Mad Man", "Definition of God"], "Led Zeppelin":
           ["Stairway to Heaven", "Whole Lotta Love"], "Tupac": ["Hit em up"
           , "California Love"]}


n = input("type in a musician of mine:")
if n in fav_mus:
    a = fav_mus[n]
    print(a)
    
else:
    print("Not found!")
