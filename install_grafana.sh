# install_grafana.sh
# Script de instalação do Grafana em versão estável em Ubuntu Server 18.04
# modificado por Vitor Mazuco

curl https://packages.grafana.com/gpg.key | sudo apt-key add -
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb beta main"
sudo apt-get update
sudo apt-get -y install grafana
sudo systemctl start grafana-server ; sudo systemctl enable grafana-server
sudo ufw allow proto tcp from any to any port 3000


