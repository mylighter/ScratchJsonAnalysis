import os
required_packages_list=['pygame','json','zipfile','time']
package_to_install=[]

print('Checking required packages...\n')
for package in required_packages_list:
	try:
		exec('import %s'%package)
	except ImportError:
		package_to_install.append(package)
print('\n')
if package_to_install:
	print('Installing required packages...')
	for package in package_to_install:
		os.system('pip install %s'%package)
print('All required packages have already been installed\n')
input('Press enter to quit')