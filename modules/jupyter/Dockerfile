FROM maxjiang/rpi-jupyter

RUN apt-get update && apt-get install -y apt-utils && apt-get install -y python-dev python-pip git i2c-tools python-smbus 
RUN git clone https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library.git
RUN cd Adafruit-Motor-HAT-Python-Library && python setup.py install

# Simplecv dependencies (python 3)
RUN apt-get install ipython python-opencv python-scipy python-numpy python-pygame
RUN pip2 install svgwrite
RUN pip2 install drivar
RUN pip2 install https://github.com/sightmachine/SimpleCV/zipball/master

# Install python 2.7 kernel
RUN python2 -m pip install ipykernel
RUN python2 -m ipykernel install

RUN sed -i "/c.KernelSpecManager.whitelist/c c.KernelSpecManager.whitelist=[\"python2\"]" /root/.jupyter/jupyter_notebook_config.py

CMD ["jupyter", "notebook"]
