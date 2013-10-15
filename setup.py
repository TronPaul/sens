import setuptools

setuptools.setup(name='Sens',
      version='0.0.4',
      description='A dynamic Twitch status image generator',
      author='Mark McGuire',
      author_email='???',
      url='https://github.com/TronPaul/sens',

      install_requires=['Pillow>=2.2.1'],

      entry_points={
          'console_scripts': ['sens = sens.application:main'],
      },
      packages=setuptools.find_packages(),
      zip_safe=True,
)
