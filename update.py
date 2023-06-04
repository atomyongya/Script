#!/usr/bin/env python3

import os

def update():
    print('***************** Updating ******************')
    os.system('sudo apt-get update')
    print('\n')

def upgrade():
    print('***************** Upgrading ******************')
    os.system('sudo apt-get upgrade')
    print('\n')

def remove():
    print('***************** Removing ******************')
    os.system('sudo apt-get autoremove')
    print('\n')

def purge():
    print('***************** Purging ******************')
    os.system('sudo apt-get autopurge')
    print('\n')

def clean():
    print('***************** Cleaning ******************')
    os.system('sudo apt-get autoclean')
    print('\n')
    print('***************** Update Complete ******************')

def main():
    update()
    upgrade()
    remove()
    purge()
    clean()

if __name__ == "__main__":
    main()
