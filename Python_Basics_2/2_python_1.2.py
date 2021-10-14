t = 'likes this'
n = 'no one likes this'
i = 2
likes = []

if len(likes) == 0:
    print(n)
    likes.append(input())
for nik in likes:
    if len(likes) == 1:
        print(likes[0], t, sep=' ')
        likes.append(input())
    elif len(likes) == 2:
        print(likes[0], 'and', likes[1], t, sep=' ')
        likes.append(input())
    elif len(likes) == 3:
        print(likes[0], ',', likes[1], 'and', likes[2], t, sep=' ')
        likes.append(input())
    elif len(likes) >= 4:
        print(likes[0], ',', likes[1], 'and', i, 'others', t, sep=' ')
        i += 1
        likes.append(input())
        

    

        
    
                
