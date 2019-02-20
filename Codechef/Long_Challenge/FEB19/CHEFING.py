letters_dic = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
for _ in range(int(input())):
    n = int(input())
    letters_dic = letters_dic.fromkeys(letters_dic,0)
    ans = []
    for temp in range(n):
        s = input()
        for i in set(s):
            letters_dic[i] += 1
            if letters_dic[i] == n:
                ans.append(i)
    print(len(ans))
    #print(ans)
