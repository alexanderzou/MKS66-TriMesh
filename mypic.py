def numConv(num):
    new = str(num)
    if len(new) == 1:
        return '00' + new
    if len(new) == 2:
        return '0' + new
    if len(new) == 3:
        return new

f = open('orbit','w')
f.write('sphere\n100 250 0 50\nsphere\n400 250 0 50\n')
fNum = 1
f.write('save\npic{}.jpg\n'.format(numConv(fNum)))
fNum += 1
while fNum < 20:
    f.write('ident\nmove\n-250 0 0\napply\nident\nrotate\ny 10\napply\nident\nmove\n250 0 0\napply\n')
    f.write('save\npic{}.jpg\n'.format(numConv(fNum)))
    fNum += 1
f.write('display\n')
f.close()