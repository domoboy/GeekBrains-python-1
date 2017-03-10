# lesson5-1, easy

import dir_commands as dc

dirs = ['dir_' + str(n) for n in range(1, 10)]

for cur_dir in dirs:
    dc.make_dir(cur_dir)

for cur_dir in dirs:
    dc.del_dir(cur_dir)
