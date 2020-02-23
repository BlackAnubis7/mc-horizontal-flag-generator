# mc-horizontal-flag-generator
Allows to generate horizontal flags in Minecraft using a normal banner

------------------------------------------------------------------------------------------------------------------------

Details:
- Works for Minecraft 1.13 and higher
- For now it looks best on a pole made of wooden fences
- The flag consists of two invisible armor stands with tilted heads, wearing the banner as a hat
- The flag has two segments - in the front and in the back
- The flag is being flipped and rotated automatically

------------------------------------------------------------------------------------------------------------------------

HOW TO USE:
1. In Minecraft point to the banner (standalone or on a wall) and press F3+I. Paste into the program
2. In Minecraft point to the wooden fence block to which the flag is going to be attached and press F3+I. Paste into the program
3. Additional settings (one line, separated by spaces, in any sequence):
    n, e, s, w, ne, sw, see, nnw... - flag facing direction
    45, 90.0, 277.3 - flag facing direction
    c - only the clockwise segment
    a - only tha anticlockwise segment
    ca - both c and a ('ac' is also accepted)
    l, r - bottom flag part is in the left/right (recpectively) part of the banner
    u, d - part of the flag attached to the pole is in the upper/bottom (respectively) part of the banner
    If particular type of setting appears more than once, the last appearance wins
    Invalid settings are ignored
    Default settings: 'n ca l u'
4: Use all (two with 'c' or 'a' setting, four with 'ca' setting) generated commands in given sequence
