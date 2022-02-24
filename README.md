# mc-horizontal-flag-generator
Allows to generate horizontal flags in Minecraft Java Edition using a normal banner

------------------------------------------------------------------------------------------------------------------------

## Details:
- Works for Minecraft **1.13** and higher
- **The main file is *hfg-1.17.py*** (if your Minecraft version is older than 1.17, use *hfg.py*)
- For now it looks best on a pole made of wooden fences
- The flag consists of two invisible armor stands with tilted heads, wearing the banner as a hat
- The flag has two segments - in the front and in the back
- The flag is being flipped and rotated automatically

------------------------------------------------------------------------------------------------------------------------

## HOW TO USE:
1. Choose a banner design using any of these methods:
    - In Minecraft point to the _banner_ (standalone or on a wall) and press **F3+I**. Paste the new clipboard into the program. 
    - EXPERIMENTAL: You may just type a two letter code of a country (ISO 3166-1 alpha-2 standard). Data is stored in 'countries_dict.py' file. **The file has to be in the same directory as the hfg.py**. Some territories are not yet available.
2. In Minecraft point to the _wooden fence_ block to which the flag is going to be attached and press **F3+I**. Paste into the program
3. Additional settings (one line, separated by spaces, in any sequence):
    - **n, e, s, w, ne, sw, see, nnw...** - flag facing direction
    - **45, 90.0, 277.3** - flag facing direction
    - **c** - only the clockwise segment
    - **a** - only tha anticlockwise segment
    - **ca** - both c and a ('ac' is also accepted)
    - **l, r** - bottom flag part is in the left/right (recpectively) part of the banner
    - **u, d** - part of the flag attached to the pole is in the upper/bottom (respectively) part of the banner
    - If particular type of setting appears more than once, the last appearance wins
    - Invalid settings are ignored
    - Default settings: **'n ca l u'**
4: Use all (two with 'c' or 'a' setting, four with 'ca' setting) generated commands in given sequence. Remember to have the pole's chunk generated while using the commands. WARNING: Minecraft may not accept commands over 256 characters. In that situation you will have to use a commandblock.

_If you need to remove a flag (or an empty armorstand that has been summoned by a mistake) stand right next to it and type **/kill @e[type=armor_stand,distance=..1.5,limit=2]**. Be extremely careful, as you can kill every single entity in the world if you forget about 'type', 'distance' or 'limit' settings. If there are more than two armorstands in that place, you can increase the limit or repeat the command._
