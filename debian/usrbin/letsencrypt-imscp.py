#!/usr/bin/python
# -*- coding: utf-8 -*-

# Dieses Skript kann Zertifikate nur updaten. Ist noch kein Zertifikat vorhanden, wird es aber von
# letsencrypt-auto erstellt und muss dann einmalig manuell in i-MSCP zu der jeweiligen Domain
# hinzugefügt werden.

# Autoren: seppel (i-mscp.net user)
# f4Nm1Z9k2P (i-mscp.net user)

# letzte Änderung: 2016-05-02

import subprocess
import os
import MySQLdb
username="root"
pw=""
pfadLetsencryptauto="/root/letsencrypt/letsencrypt-auto"
db = MySQLdb.connect( host="localhost",
 user=username,
 passwd=pw,
 db="imscp")
cur = db.cursor()
cur.execute("SELECT domain_name FROM domain;");
for domainTmp in cur.fetchall():
 domain = domainTmp[0]
 print domain
 domainListe = []
 cmd = pfadLetsencryptauto+" certonly --apache --keep -d "+domain+" -d www."+domain
 cur.execute("select subdomain_name,subdomain_mount from subdomain where domain_id=(select domain_id from domain where domain_name='"+domain+"');");
 for subdomain in cur.fetchall():
  domainListe.append(subdomain[0]+"."+domain);
  cmd = cmd +" -d "+(subdomain[0]+"."+domain)
 print domainListe
 print cmd
 os.system(cmd)
 pkey = open("/etc/letsencrypt/live/"+domain+"/privkey.pem",'r').read() #default-pfad
 chain = open("/etc/letsencrypt/live/"+domain+"/chain.pem",'r').read() #default-pfad
 cert = open("/etc/letsencrypt/live/"+domain+"/cert.pem",'r').read() #default-pfad
 cur.execute("""update ssl_certs set
 ca_bundle=%s,
 private_key=%s,
 certificate=%s,
 status=%s
 where
 domain_type='dmn'
 AND domain_id=(select domain_id from domain where domain_name=%s)
 """
 ,(chain,pkey,cert,'tochange',domain));
 foo = cur.execute("""update ssl_certs set
 ca_bundle=%s,
 private_key=%s,
 certificate=%s,
 status=%s
 where domain_type='sub'
 AND domain_id IN (select subdomain_id
 from subdomain
 where domain_id= (select domain_id from domain where domain_name=%s)
 );
 """,(chain,pkey,cert,'tochange',domain));
 cur.execute("update domain set domain_status='tochange'");
 cur.execute("update subdomain set subdomain_status='tochange'");
 db.commit();
os.system("/var/www/imscp/engine/imscp-rqst-mngr")