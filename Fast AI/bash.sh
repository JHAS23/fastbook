echo Setting up server...
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs -q
pip install jupyter jupyterlab --upgrade -q
pip install jupyter_contrib_nbextensions && jupyter contrib nbextension install -q
pip install -r /content/deep-learning/Fast\ AI/requirements.txt -q
wget -q -c -nc https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip -qq -n ngrok-stable-linux-amd64.zip