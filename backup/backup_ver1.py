import os
import time

source = ['D:\\test']

target_dir = 'D:\\backup'
target=target_dir+'/'+time.strftime('%Y%m%d%H%M%S') + '.zip'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backuo to', target)
else:
    print('Backup FAILED')
