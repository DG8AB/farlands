import nbtlib
from nbtlib.tag import Double, List

nbt_file = nbtlib.load('level.dat')

new_x = 12550821.0
new_y = 100.0
new_z = 12550821.0

nbt_file['Data']['Player']['Pos'] = List([Double(new_x), Double(new_y), Double(new_z)])

nbt_file.save('level_new.dat')
