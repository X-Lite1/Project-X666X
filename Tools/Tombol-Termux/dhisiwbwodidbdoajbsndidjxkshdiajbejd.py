import os
import sys
from time import sleep

a = '\x1b[1;31m'
b = '\x1b[1;33m'
c = '\x1b[1;32m'
d = '\x1b[1;34m'
e = '\x1b[1;35m'
f = '\x1b[1;36m'

os.system('clear')
print b + '\nProsess Crack Home...'
sleep(3)
print f + '[~]Berhasil !'
sleep(1.3)
print b + '\nProsess Menembus Data...'
sleep(2)
try:
    os.mkdir('/data/data/com.termux/files/home/.termux')
except:
    pass

print f + '[~]Berhasil !'
sleep(1)
print b + '\nMenambahkan Tombol Spesial...'
sleep(1.6)
key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
with open('/data/data/com.termux/files/home/.termux/termux.properties', 'w') as fout:
    fout.write(key)

sleep(1)
print f + '[~] Berhasil !'
sleep(1.3)
print b + '\nMembersihkan Hasil Crack...'
sleep(2)
os.system('termux-reload-settings')
print f + '[!] Berhasil !! ^_^' + c + '\n\nTombol Berhasil DiTambahkan ^_^\n\n'
sleep(4)
os.system('clear')
sys.exit
# os.system('python2 X666X.py')
