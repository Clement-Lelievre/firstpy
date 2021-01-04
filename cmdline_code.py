''' this script uses the exec() function associated to os.system in order to run cmd line arguments'''
'''BEWARE: this involves security questions as any user could use harmful commands such as 'rm -rf *', that erases all files and folders'''
'''fyi the '-rf' part of the cmd line above does the following: -f means forced, so as to not get a prompt 'are you sure?' while -r recursively explores the directory tree in order to erase everything'''

# initial command
print('Hello and welcome. Please make sure you are located in the right directory.\n')
cmdline = str(input('Type your command line argument here:\n'))

try:
    if 'rm' not in cmdline and 'mv' not in cmdline:
        exec("import os ; os.system(cmdline)")
    else:
        print('Sorry, you cannot remove, rename nor change stuff location.')
except:
    print('Sorry dude, your command could not be run.')

# loop in case user wants to type other commands

while True:
    newcmdline = str(input('\n\nIf you need to perform another command line action, please type it, else type Q to quit.\n\n'))
    if newcmdline == 'Q':
        print('Goodbye!')
        break
    else:
        try:
            if 'rm' not in newcmdline and 'mv' not in newcmdline:
                print('')
                exec("import os ; os.system(newcmdline)")
            else:
                print('\nSorry, you cannot remove, rename nor change stuff location.')
        except:
            print('Sorry dude, your command could not be run.')