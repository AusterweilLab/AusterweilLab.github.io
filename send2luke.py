#Package up webapp dir and send to server (Luke)

import os, sys

localdir = '_site'
tarname = 'webtar'
serverdirbase = '/var/services/web/'
#serverdir = 'catgen_midbotABC'

#tarzip local
os.system('tar -cvzf {}.tar.gz {}'.format(tarname,localdir))
#scp it over 
os.system('scp -i ~/Dropbox/.ssh/luke -P 1202 {}.tar.gz xian@alab.psych.wisc.edu:{}'.format(tarname,serverdirbase))

#mk new dir on host and untar the tar
cdcmd = 'cd {}'.format(serverdirbase)
untarcmd = 'tar -xvzf {}.tar.gz -C ./'.format(tarname)
#renamecmd = ''
renamecmd = 'rsync -r {}/* ./'.format(localdir)
#rm the tar on host
removecmd = 'rm {}.tar.gz'.format(tarname)
#run it all
os.system('ssh -i ~/Dropbox/.ssh/luke -p 1202 -t xian@alab.psych.wisc.edu  \'{};{};{};{}\' '.format(cdcmd,untarcmd,renamecmd,removecmd))

#rm the tar locally
os.system('rm {}.tar.gz'.format(tarname))

