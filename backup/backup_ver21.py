import os
import time
#源目录
source = ['D:\\test']

#目标目录
target_dir = 'D:\\backup'


#目标目录不存在则创建目标目录
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

#将原文件打包成压缩文件
#将当前日期作为主备份目录下的子目录名称
today=target_dir+os.sep+time.strftime('%Y%m%d')
#将当前时间作为zip文件的文件名
now=time.strftime('%H%M%S')

#zip文件名称格式
target=today+os.sep+now+'.zip'

#子目录不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('successfully created directory')

#使用zip命令打包文件
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

#运行备份
print('zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')