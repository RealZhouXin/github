import os
import time

source_dir = 'D:\\test'
source =source_dir+'.txt'
target = ['D:\\backup']

'''if not os.path.exists(target_dir):
    os.mkdir(target_dir)'''

move_command = 'move {0} {1}'.format(source, ' '.join(target))

print('move command is:')
print(move_command)
print('Running:')
if os.system(move_command) == 0:
    print('Successful move to', target)
else:
    print('Move FAILED')
