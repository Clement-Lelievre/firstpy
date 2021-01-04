import os
from pathlib import Path

''' the below function parses the directory tree from the cwd and retrieves the name of the folder containing 
the largest number of files, together with the number of files'''

def filescount(path):
    file_count = {}
    for folderName, subfolders, filenames in os.walk(path): # this will start searching from the current working directory
        file_count[folderName] = 0
        for filename in filenames:
                file_count[folderName] += 1
        # for subfolder in subfolders:
        #     file_count[subfolder] = 0
        #     for filename in filenames:
        #         file_count[subfolder] += 1
    print(file_count)
    file_count_sorted = {key: value for key, value in sorted(file_count.items(), key=lambda item: item[1])}
    topfoldername,topfolderfilenb = list(file_count_sorted.keys())[-1], list(file_count_sorted.values())[-1]
    # managing potential ties between largest folders
    if list(file_count_sorted.values()).count(max(list(file_count_sorted.values()))) == 1:
        print(f'\nThe folder named {topfoldername} has the largest number of files: {topfolderfilenb}\nThere are', len(file_count),'folders (including parent dir) and there is a total of',sum(list(file_count.values())),'files')
    else:
        print('There are ties:',list(file_count_sorted.values()).count(max(list(file_count_sorted.values()))),'folders contain',max(list(file_count_sorted.values())),'files. In total, there are',sum(list(file_count.values())),'files in',len(file_count),'folders.')
    #print(file_count_sorted)
    
    return ''

# let's try it on the current directory:
filescount(path=Path.cwd())