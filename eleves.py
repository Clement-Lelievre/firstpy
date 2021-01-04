'''This script creates in the cwd one directory per pupil, 
then creates one text file per pupil (both named after the pupil) writing pupil grade in it,
moves textfile in the pupil folder,
finally indicates the time duration of the entire execution.'''

import random, time, os

starttime = time.time()

eleves = ['paul','liam','jean','dimitri']

for pupil in eleves:
    cmd = 'mkdir ' + pupil
    exec("os.system(cmd)")  # create folder named with pupil's name
    file = open(pupil.upper()+'.txt','w')
    file.write(pupil+"'s average grade is "+ str(random.randint(1,20)))
    file.close()
    cmd = 'mv ' + pupil.upper()+'.txt' + ' ' + pupil+'/'
    exec("os.system(cmd)")

code_exec_duration = time.time() - starttime
print('All done. Have a check in the GUI. It took me ',code_exec_duration,' seconds to do this task.')