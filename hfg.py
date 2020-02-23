import re
import math

TAG = 'teststand'
DFI = math.atan(0.255/0.495)
R = math.sqrt(0.255**2+0.495**2)
FLIPS = {  # v - vertical, h - horizontal (both work in axes of horizontal flag, not a vertical banner)
    'bs,':  {'v': 'bs,',  'h': 'ts,'},
    'ts,':  {'v': 'ts,',  'h': 'bs,'},
    'ls,':  {'v': 'rs,',  'h': 'ls,'},
    'rs,':  {'v': 'ls,',  'h': 'rs,'},
    'drs,': {'v': 'dls,', 'h': 'dls,'},
    'dls,': {'v': 'drs,', 'h': 'drs,'},
    'ld,':  {'v': 'rud,', 'h': 'lud,'},
    'rud,': {'v': 'ld,',  'h': 'rd,'},
    'lud,': {'v': 'rd,',  'h': 'ld,'},
    'rd,':  {'v': 'lud,', 'h': 'rud,'},
    'vh,':  {'v': 'vhr,', 'h': 'vh,'},
    'vhr,': {'v': 'vh,',  'h': 'vhr,'},
    'hh,':  {'v': 'hh,',  'h': 'hhb,'},
    'hhb,': {'v': 'hhb,', 'h': 'hh,'},
    'bl,':  {'v': 'br,',  'h': 'tl,'},
    'br,':  {'v': 'bl,',  'h': 'tr,'},
    'tl,':  {'v': 'tr,',  'h': 'bl,'},
    'tr,':  {'v': 'tl,',  'h': 'br,'},
    'bt,':  {'v': 'bt,',  'h': 'tt,'},
    'tt,':  {'v': 'tt,',  'h': 'bt,'},
    'bts,': {'v': 'bts,', 'h': 'tts,'},
    'tts,': {'v': 'tts,', 'h': 'bts,'},
    'gra,': {'v': 'gra,', 'h': 'gru,'},
    'gru,': {'v': 'gru,', 'h': 'gra,'},
}


def calculate_rotation(nesw):
    dirs = {'n': 90, 'e': 180, 's': 270, 'w': 0}
    if 's' in nesw:
        dirs['w'] = 360
    rot = (dirs[nesw[0]] + dirs[nesw[-1]]) / 2
    if len(nesw) == 3:
        rot = (rot + dirs[nesw[1]]) / 2
    return rot


def flip(data, vh):
    fpd = data
    for let in vh:
        for pat in FLIPS:
            if pat in fpd:
                fpd = fpd.replace(':' + pat, ':&&' + FLIPS[pat][let])
        fpd = fpd.replace(':&&', ':')
    return fpd


#/setblock 36 72 1174 minecraft:red_wall_banner[facing=north]{Patterns:[{Pattern:"ss",Color:0},{Pattern:"tr",Color:11}]}
#/setblock 21 67 1165 minecraft:red_banner[rotation=12]{Patterns:[{Pattern:"ss",Color:0},{Pattern:"tr",Color:11}]}
#minecraft:red_banner{BlockEntityTag:{Patterns:[{Pattern:ss,Color:0},{Pattern:bl,Color:11}]}}
flag = input('Flag F3+I data: ')
pole = input('Flag pole top F3+I data: ')
args = casefold(input('Options ([n,e,s,w,nww,se...], [c,a,ca], [l,r], [u,d]): ')).split()
rot = 90
side = 'ca'
fpv = 'l'
fph = 'u'
for arg in args:
    if arg in 'nneennwwsseessww' and len(arg) in (1, 2, 3):
        rot = calculate_rotation(arg)
    elif arg in 'aca' and len(arg) in (1, 2):
        side = arg
    elif arg in 'rl' and len(arg) == 1:
        fpv = arg
    elif arg in 'ud' and len(arg) == 1:
        fph = arg
    else:
        try:
            rot = round(float(arg) - 90, 1)
        except ValueError:
            pass
# print(rot, side, fpv, fph)  # print used settings
x, y, z = (int(i) for i in pole.split()[1:4])
x += 0.5
y -= 0.875
z += 0.5
x1 = x - round(math.cos(math.radians(rot + 180) - DFI) * R, 2)
z1 = z - round(math.sin(math.radians(rot + 180) - DFI) * R, 2)
x2 = x - round(math.cos(math.radians(rot + 180) + DFI) * R, 2)
z2 = z - round(math.sin(math.radians(rot + 180) + DFI) * R, 2)
y = round(y, 2)

if 'banner' not in flag:  # NotBanner exception
    print('Not a banner')
    input()
    raise Exception('The input was not of a banner item')

flag = flag.split(' ')[-1]  # extract block info
flag = flag.replace('wall_banner', 'banner')  
flag = flag.replace('"', '')
m = re.search('\[facing=.....?\]', flag)
if m is not None:
    flag = flag.replace(m.group(0), '')
m = re.search('\[rotation=..?.?\]', flag)
if m is not None:
    flag = flag.replace(m.group(0), '')
flag = flag.replace('banner', 'banner{BlockEntityTag:')
if fpv == 'r':
    flag = flip(flag, 'v')
if fph == 'd':
    flag = flip(flag, 'h')
# print(x1, z1, x2, z2, y)
inv_nog = 'Invisible:{},NoGravity:{}'.format(1, 1)
if 'c' in side:
    summon = '/summon minecraft:armor_stand {} {} {} '.format(x1, y, z1)
    xyz_find = 'x={},y={},z={}'.format(round(x1-0.1, 2), round(y-0.1, 2), round(z1-0.1, 2))
    print(summon + '{{Rotation:[{}f],{},Tags:[{}_cw],DisabledSlots:2039583,Pose:{{Head:[0f,180f,-90f]}}}}'.format(rot, inv_nog, TAG))
    print('/replaceitem entity @e[tag={}_cw,limit=1,{},dx=0.2,dy=0.2,dz=0.2] armor.head {}}}'.format(TAG, xyz_find, flip(flag, 'vh')))
if 'a' in side:
    summon = '/summon minecraft:armor_stand {} {} {} '.format(x2, y, z2)
    xyz_find = 'x={},y={},z={}'.format(round(x2-0.1, 2), round(y-0.1, 2), round(z2-0.1, 2))
    print(summon + '{{Rotation:[{}f],{},Tags:[{}_acw],DisabledSlots:2039583,Pose:{{Head:[0f,0f,-90f]}}}}'.format(rot, inv_nog, TAG))
    print('/replaceitem entity @e[tag={}_acw,limit=1,{},dx=0.2,dy=0.2,dz=0.2] armor.head {}}}'.format(TAG, xyz_find, flip(flag, 'h')))
input()
