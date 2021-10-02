from setuptools import setup

setup(
      name='helper_bot',
      version='1.1',
      description='Console bot for contact book managing',
      author='Andriy Onufriyenko',
      author_email='7206130@gmail.com',
      license='MIT',
      entry_points={'console_scripts': ['helper_bot = helper_bot.bot:main']},
      packages=['helper_bot']
      )
