#!/usr/bin/python3
#from enumerate import Enumeration
#from revshell import Generate
import os
import argparse
import base64


def banner():
    print("""         
     _                 _               
    (_)               | |              
 ___ _ ___ _   _ _ __ | |__  _   _ ___ 
/ __| / __| | | | '_ \| '_ \| | | / __|
\__ \ \__ \ |_| | |_) | | | | |_| \__ \\
|___/_|___/\__, | .__/|_| |_|\__,_|___/
            __/ | |                    
           |___/|_|  
          

         _          ________
        / \_       /        \\
        \ /       /          \\
        /_______//            \\
       /________/|            |                       ||||||||
      /          |            |                  |||||
     /           |            |          ||||||||
    / \           \          /   ||||||||
    |  \            \______/|||||
    |   |       ||||||||||||
   /    |_ |||||
  /_  |||||
||||||""")
    print("""Please enter a module:
            \tEnumeration\n\tReverse Shell\n\t""")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="sisyphus.py",
        description="Almost all-inclusive PT tool.",
        usage="%(prog)s [options]")
    parser.add_argument('-i', '--ip', required=True, type=str, help="Target IP address")
    #parser.add_argument('')
    banner()
