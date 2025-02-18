import os
import sql_server_init
import subprocess
import sqlite3
from termcolor import colored


class Enumeration:
    def __init__(self, ip_addr, cwd, db_path="main.db"):
        self.ip_addr = ip_addr
        self.cwd = cwd
        self.banner = colored("[+]", "green")
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def basics(self):
        print(f"{self.banner} Initial nmap scan started: {self.banner}")
        os.system('mkdir -p nmap')
        os.system(f"nmap -sC -sV {self.ip_addr} -oA nmap/{self.ip_addr}-basescan")
        

    def get_open_ports(self):
        with open(f"{self.cwd}/nmap/{self.ip_addr}-basescan.gnmap", "r") as nmap_out:
            
            pass


#TODO:: add options to choose what service to enumerate
# e.g: ALL, LDAP, SMB, FTP, HTTP, SSH, etc...