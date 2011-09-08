
import os

for fname in os.listdir('.'):
    if fname[-4:] == '.rst':
        tmpname = fname + '.tmp'
        fdin = open(fname)
        fdout = open(tmpname, 'wb')
        for line in fdin:
            if line.startswith('**2008-07-15:**'):
                for i in range(6):
                    fdin.next()
                continue
            elif line.startswith('[`comment on/'):
                break
            fdout.write(line)
        fdin.close()
        fdout.close()
        os.remove(fname)
        os.rename(tmpname, fname)







