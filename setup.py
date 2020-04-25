from setuptools import setup

setup(
    name='bareispy',
    version='0.1',
    packages=['baresipy', 'baresipy.utils'],
    url='https://github.com/JarbasAl/baresipy',
    install_requires=["ResponsiveVoice",
                      "opentone>=0.1.2",
                      "pydub",
                      "pexpect"],
    license='MIT',
    author='jarbasAI',
    author_email='jarbasai@mailfence.com',
    description='python baresip wrapper'
)