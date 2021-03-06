from setuptools import setup, find_packages

setup(
      install_requires=['distribute', 'Adafruit_MotorHAT>=1.3.0','PyTweening==1.0.3', 'paho-mqtt>=1.5.0'],
      extras_require={
         'test':['testfixtures','hbmqtt'],
         'nxt':['nxt-python==2.2.2']
      },
      name = '${PROJECT_NAME}',
      python_requires= '>=3.4.0',
      description = 'Hardware abstraction layer for Raspbuggy, Bit:bot and GianoPi robots',
      author = 'Brice Copy',
      author_email = 'brice.copy@gmail.com',
      url = 'https://github.com/cmcrobotics/raspbuggy',
      keywords = ['raspbuggy'],
      version = '${VERSION}',
      packages =  find_packages('.')
)
