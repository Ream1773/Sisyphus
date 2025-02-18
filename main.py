#!/usr/bin/python3
import enumerate
from revshell import Generate
import argparse
from os import getuid, getcwd
import sys
from termcolor import colored
#import logger 


def banner():

    print(r"""         
     _                 _               
    (_)               | |              
 ___ _ ___ _   _ _ __ | |__  _   _ ___ 
/ __| / __| | | | '_ \| '_ \| | | / __|
\__ \ \__ \ |_| | |_) | | | | |_| \__ \
|___/_|___/\__, | .__/|_| |_|\__,_|___/
            __/ | |                    
           |___/|_|  
          

         _          ________
        / \_       /        \
        \ /       /          \
        /_______//            \
       /________/|            |                       ||||||||
      /          |            |                  |||||
     /           |            |          ||||||||
    / \           \          /   ||||||||
    |  \            \______/|||||
    |   |       ||||||||||||
   /    |_ |||||
  /_  |||||
||||||""")
    print("\nScript must be run with sudo!")
    print("""\nPlease enter a module:\n\nEnumeration\nReverse Shell\n\t""")


if __name__ == '__main__':

    banner_chars = [colored("[-]", "red"), colored("[+]", "green")]

    parser = argparse.ArgumentParser(
        prog="sisyphus.py",
        description="Almost all-inclusive PT tool.",
        usage="%(prog)s [options]")
    parser.add_argument('-i', '--ip', required=True, type=str, help="Target IP address")

    if getuid() != 0:
        print(f" {banner_chars[0]} {colored("ERROR:", "red")} This script must be run as r00t! {banner_chars[0]}")
        sys.exit(1)
    else:
        cwd = getcwd()
        args = parser.parse_args()
        banner()
        enum_obj = enumerate.Enumeration(args.ip, cwd).basics()
