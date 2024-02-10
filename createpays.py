from fichier import Fichier
import json
from country import Country
hey=json.loads(Fichier("./public","temp.json").lire())
db=Country()
for x in hey["pays"]:
  print(x)
  db.create({"name":x["country"],"code":x["unicode"]})
  
