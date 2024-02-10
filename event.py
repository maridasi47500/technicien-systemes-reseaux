# coding=utf-8
import sqlite3
import sys
import re
from moussaillons import Moussaillon
from model import Model
class Event(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.dbMoussaillons=Moussaillons()
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists event(
        id integer primary key autoincrement,
        name text,
            stuff_id text,
            periode_id text
                    );""")
        self.con.commit()
        #self.con.close()
    def getallbypersonid(self,personid):
        self.cur.execute("select event.*,m.person_id as moussaillonid,person.name nommoussaillon,periode.name as nomperiode,stuff.name as nomstuff,g.name as groupstuffname,pays.code as moussaillonpays,pays.name as nompays,periode.name as nomperiode from event left join moussaillons m on m.event_id = event.id left join periode on periode.id = event.periode_id left join person on m.person_id = person.id left join country pays on pays.id = person.country_id left join periode on periode.id = event.periode_id left join stuff on stuff.id = event.stuff_id left join group_stuff g on g.id = stuff.group_stuff_id group by event.id having moussaillonid = ? ",(personid,))

        row=self.cur.fetchall()
        return row
    def getall(self):
        self.cur.execute("select * from event")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from event where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from event where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        myhash={}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H")
        moussaillonids=myhash["person_ids"]

        
        del myhash["person_ids"]
        print(myhash,myhash.keys())
        myid=None
        try:
          self.cur.execute("insert into event (name,stuff_id,periode_id) values (:name,:stuff_id,:periode_id)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
          for a in moussaillonids.split(","):
              self.dbMoussaillons.create({"event_id":myid,"person_id":a})
        except Exception as e:
          print("my error"+str(e))

        azerty={}
        azerty["event_id"]=myid
        azerty["notice"]="votre event a été ajouté"
        return azerty




