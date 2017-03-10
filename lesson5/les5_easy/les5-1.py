# lesson5-1, easy
import os
import mkdir
import deldir

dirs = ['dir_' + str(n) for n in range(1, 10)]

for cur_dir in dirs:
    mkdir.make_dir(cur_dir)

for cur_dir in dirs:
    deldir.del_dir(cur_dir)
