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
                
             
                tab.append([reponse["username"],int(reponse["score"]),reponse["rank"]])
        
        
        tab=Utils.tri_rapide(tab)  #tri du tableau
        tmp_str=""
        rang_max=len(str(tab[len(tab)-1][2]))
        max_username_length=Utils.max_username_length(tab)
        score_max=len(str(tab[0][2]))
        #print(rang_max)
        for i in range(0,len(tab)):        
            tmp_str+="Rangs {0} : {1} ({2}pts) \n".format(str(tab[i][2]).rjust(rang_max),tab[i][0].ljust(max_username_length),tab[i][1])#affichage du tableau
        
        return tmp_str
cryptohack()

