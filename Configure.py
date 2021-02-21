import os
packages_list=['pygame','json','zipfile','time']

print('Installing environmental packages...')
for package in packages_list:
	try:
		exec('import %s'%package)
	except ImportError:
		os.system('pip install %s'%package)

print('Packages have already been installed')
input('Press enter to quit')