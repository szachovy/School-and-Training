from distutils.core import setup

setup(
    name='MyCreatedPackage',
    version='1.0',
    description='My first all created Package',
    author='Wiktor Maj',
    author_email='prorokenp@gmail.com',
    url='https://github.com/WJMaj',
    packages=['Package'],
    package_dir={'Package': '/home/wiktor/Publiczny/Python/newSPOJ/Dwie Cyfry Silni/Package'},
    classifiers=[
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Operating System :: LINUX',
          'Programming Language :: Python',
          ],
)