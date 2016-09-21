apt-get update
apt-get install -y --no-install-recommends wget pv apt-utils apt-transport-https
apt-get install -y --no-install-recommends python python-dev python-pip python-virtualenv
wget -q https://packagecloud.io/gpg.key -O - | sudo apt-key add -
echo 'deb https://packagecloud.io/Hypriot/Schatzkiste/debian/ jessie main' | sudo tee /etc/apt/sources.list.d/hypriot.list
apt-get update
apt-get install -y docker-hypriot

#  (!) the container needs to be run as PRIVILEGED to mount shared memory
