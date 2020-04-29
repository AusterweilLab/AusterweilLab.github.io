#Package up webapp dir and send to server (Luke)
#Uses bash, so probably better to use on some Unix-based OS. Otherwise it should work with Cygwin on Windows??

import os, sys
narg = len(sys.argv)
if __name__ == "__main__" and narg>1:
    user = sys.argv[1]
else:
    raise Exception('User not provided. Please enter valid username as first argument.')

users = {'xian':{'username':'xian',
                 'keylocation':'~/Dropbox/.ssh/luke'},
         'blake':{'username':'blake',
                  'keylocation':'/cygdrive/c/Users/blake/.ssh/Luke'},
         'jeff':{'username':'jeff',
                  'keylocation':'~/.ssh/id_rsa.pub'}
         }

if user in users:
    username = users[user]['username']
    keylocation = users[user]['keylocation']
else:
    raise Exception('User \'%s\' not recognized.' % user)


localdir = '_site'
tarname = 'webtar'
serverdirbase = '/var/services/web/'


#tarzip local
os.system('tar -cvzf {}.tar.gz {}'.format(tarname,localdir))
#scp it over 
os.system('scp -i {} -P 1202 {}.tar.gz {}@alab.psych.wisc.edu:{}'.format(keylocation,tarname,username,serverdirbase))

#mk new dir on host and untar the tar
cdcmd = 'cd {}'.format(serverdirbase)
untarcmd = 'sudo tar -xvzf {}.tar.gz -C ./'.format(tarname)
renamecmd = 'sudo rsync -r {}/* ./'.format(localdir)
#rm the tar on host
removecmd = 'sudo rm {}.tar.gz'.format(tarname)
#Also remove the _site folder
rmsite = 'sudo rm -r {}'.format(localdir)
#run it all
os.system('ssh -i {} -p 1202 -t {}@alab.psych.wisc.edu  \'{};{};{};{};{}\' '.format(keylocation,username,cdcmd,untarcmd,renamecmd,removecmd,rmsite))

#rm the tar locally
os.system('rm {}.tar.gz'.format(tarname))

