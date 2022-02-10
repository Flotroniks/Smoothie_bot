import requests,string,datetime,Utils,json

def rootme():
    d = datetime.datetime.now()
    day=d.strftime("%H%d")
    with open('day.tmp') as f:
        contents = f.read()
    if(day!=contents):
        k=open("day.tmp", "w")
        k.write(day)
        k.close()
        f=open("Usernames.txt", "r")
        Users=f.readlines()
        Users=[x.strip() for x in Users]
        tab=[]
        
        for user in Users:
            r=requests.get('https://www.root-me.org/'+user+'?lang=fr')
            reponse=r.text
            str_reponse=str(reponse)

            a=str_reponse.find('Points')
            imnotcode=str_reponse[a-30:a-25]
            
            if(imnotcode.find(";")==-1):
                #>10.000 points
                score =imnotcode
                tab.append([user,int(score)])

            else:
                #<10.000points
                for i in range(0,len(imnotcode)):
                    if(imnotcode[i]==';'):
                        score=imnotcode[i+1:len(imnotcode)]
                        tab.append([user,int(score)])
                        
                        break
        tab=Utils.tri_rapide(tab)  #tri du tableau
        f=open("score.tmp", "w")
        f.write(str(tab))
        f.close()
    else:

        f=open("score.tmp", "r")
        tab=eval(f.read())
        f.close()
    
            
    
    #tab = Utils.normalize_username(tab, Utils.max_username_length(tab))
    
    tmp_str=""
    for i in range(0,len(tab)):        
        tmp_str+=" {0} Pts          {1}\n".format(tab[i][1],tab[i][0]) 
    


    return tmp_str


def cryptohack():
        f=open("Usernames_cryptohack.txt", "r")
        Users=f.readlines()
        Users=[x.strip() for x in Users]
        tab=[]     
        for user in Users:
            r=requests.get('https://cryptohack.org/api/user/'+user+'/')
            reponse=r.json() 
            if "username" in reponse:
                
                print(reponse["username"])
                print(reponse["score"])
                tab.append([reponse["username"],int(reponse["score"])])
        
        print(tab)
            


cryptohack()

