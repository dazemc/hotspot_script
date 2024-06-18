!# /bin/bash
wget https://github.com/dazemc/hotspot_script/archive/refs/heads/master.zip
cd hotspot_script-master
chmod +x hotspot_autostart.sh
touch hotspot_autostart.service
mv hotspot_autostart.sh /usr/sbin/hotspot_autostart.sh
mv hotspot_autostart.service /etc/systemd/systemd/hotspot_autostart.service
python3 main.py
systemctl daemon-reload && systemctl enable hotspot_autostart.service
reboot