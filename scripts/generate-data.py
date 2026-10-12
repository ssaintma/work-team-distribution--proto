"""Génère le jeu de données fictif (100 work teams) dans data/*.json. Usage: python3 scripts/generate-data.py"""
import json, os, random
random.seed(49)
SPEC = {"PLOM":"Plomberie","ELEC":"Électricité","CARR":"Carrelage","PEIN":"Peinture","MENU":"Menuiserie","CHAU":"Chauffage","ISOL":"Isolation","MACO":"Maçonnerie","PLAQ":"Plâtrerie","SERR":"Serrurerie"}
SERV = [("49000101","Pose de robinetterie","PLOM"),("49000102","Installation chauffe-eau","PLOM|CHAU"),
("49000103","Remplacement tableau électrique","ELEC"),("49000104","Pose de prises et interrupteurs","ELEC"),
("49000105","Pose de carrelage sol","CARR"),("49000106","Pose de faïence murale","CARR|MACO"),
("49000107","Peinture intérieure","PEIN|PLAQ"),("49000108","Pose de porte intérieure","MENU"),
("49000109","Pose de fenêtre","MENU|ISOL"),("49000110","Installation chaudière","CHAU|PLOM"),
("49000111","Isolation des combles","ISOL"),("49000112","Création de cloison","PLAQ|MACO"),
("49000113","Remplacement de serrure","SERR|MENU"),("49000114","Dalle béton / chape","MACO")]
CP = ["75001","75008","75011","75015","75018","92100","92110","92200","93100","93200","94200","94300","69001","69003","69006","69007"]
pre = ["Atelier","Groupe","Maison","Équipe","Artisans","Services","Rénov","Bâti"]
suf = ["Dupont","Martin","Bernard","Lefèvre","Moreau","Garcia","Roux","Fournier","Girard","Lambert","Faure","Mercier","Blanc","Guérin","Muller","Henry","Perrin","Morin","Clément","Rey"]
teams=[]; used=set()
while len(teams)<100:
    n=f"{random.choice(pre)} {random.choice(suf)}"
    if n in used: continue
    used.add(n)
    zones=random.sample(CP, random.randint(3,8))
    sp=random.sample(list(SPEC), random.randint(2,4))
    specs="|".join(f"{s}:{'P1' if random.random()<.4 else 'P2'}" for s in sp)
    opt=random.sample([s[0] for s in SERV], random.choice([0,0,1,1,2,3]))
    teams.append({"id":f"WT{len(teams)+1:03d}","name":n,"zones":"|".join(sorted(zones)),"specialties":specs,"optouts":"|".join(sorted(opt))})
out=os.path.join(os.path.dirname(__file__),"..","data")
def w(name,obj): json.dump(obj,open(os.path.join(out,name),"w"),ensure_ascii=False)
w("workteams.json",teams)
w("services.json",[{"code":c,"label":l,"specialties":s} for c,l,s in SERV])
w("specialties.json",[{"code":k,"label":v} for k,v in SPEC.items()])
w("postcodes.json",[{"code":c} for c in CP])
