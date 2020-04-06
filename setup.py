from distutils.core import setup
setup(
  name = 'MADict',         # How you named your package folder (MyLib)
  packages = ['MADict'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Con madprofiling tenemos una vista 360° del data set. Sabemos el formato de cada campo (‘type’), sabemos si el campo es categorico o no (‘categorical’), sabemos el total de registros de cada campo (‘total’), el número de registros únicos por campo (‘unique’), el número de registros nulos por campo (‘null’), el número de registros tipo ‘na’ por campo y finalmente el porcentaje de registros tipo null y tipo na por campo.',   # Give a short description about your library
  author = 'Miguel Angel Diaz Rodriguez',                   # Type in your name
  author_email = 'ma.diaz216@uniandes.edu.co',      # Type in your E-Mail
  url = 'https://github.com/megelon/MADict',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/megelon/MADict/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['PROFILING', 'DATA', 'UNDERSTANDING'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'pandas',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Data Scientists',      # Define that your audience are developers
    'Topic :: Data Science',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)