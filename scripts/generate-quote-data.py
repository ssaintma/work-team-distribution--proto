"""Génère le jeu de données fictif de la variante Quote Framework dans data/q-*.json.
Usage: python3 scripts/generate-quote-data.py  (les codes postaux sont partagés avec data/postcodes.json)"""
import json, os, random
random.seed(77)
FAM = {"Plomberie":["Robinetterie","Chauffe-eau","Évacuation","Sanitaires"],
"Électricité":["Tableau électrique","Prises et interrupteurs","Éclairage","VMC"],
"Revêtements":["Carrelage sol","Faïence murale","Parquet","Peinture intérieure"],
"Menuiserie":["Porte intérieure","Fenêtre","Placard sur mesure","Volet roulant"],
"Gros œuvre":["Dalle béton / chape","Cloison placo","Isolation combles","Ouverture de mur"],
"Chauffage":["Chaudière gaz","Pompe à chaleur","Radiateurs","Plancher chauffant"]}
WI=[];n=1
for f,l in FAM.items():
    for x in l: WI.append({"code":f"OUV{n:03d}","label":x,"family":f});n+=1
CP=[c["code"] for c in json.load(open(os.path.join(os.path.dirname(__file__),"..","data","postcodes.json")))]
pre=["Atelier","Groupe","Maison","Équipe","Artisans","Services","Rénov","Bâti"]
suf=["Dupont","Martin","Bernard","Lefèvre","Moreau","Garcia","Roux","Fournier","Girard","Lambert","Faure","Mercier","Blanc","Guérin","Muller","Henry","Perrin","Morin","Clément","Rey"]
fams=list(FAM);teams=[];used=set()
while len(teams)<100:
    nm=f"{random.choice(pre)} {random.choice(suf)}"
    if nm in used: continue
    used.add(nm)
    mine=random.sample(fams,random.randint(2,3))
    codes={w["code"] for w in WI if w["family"] in mine and random.random()<.8}
    codes|={w["code"] for w in random.sample(WI,random.randint(1,2))}
    items="|".join(f"{c}:{'P1' if random.random()<.4 else 'P2'}" for c in sorted(codes))
    teams.append({"id":f"WT{len(teams)+1:03d}","name":nm,"zones":"|".join(sorted(random.sample(CP,random.randint(3,8)))),"workitems":items})
out=os.path.join(os.path.dirname(__file__),"..","data")
json.dump(teams,open(os.path.join(out,"q-workteams.json"),"w"),ensure_ascii=False)
json.dump(WI,open(os.path.join(out,"q-workitems.json"),"w"),ensure_ascii=False)
