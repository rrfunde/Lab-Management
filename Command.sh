
if [[ $EUID -ne 0 ]]; then

	echo "You must be root to perform this action"


else


	cp /run/media/dbsl/FEDORA-LIVE/Mysql.py /home/dbsl/Templates/

	cp /run/media/dbsl/FEDORA-LIVE/status.sh /bin/

	rpm -ivh /run/media/dbsl/FEDORA-LIVE/MySQL-python-1.2.3-8.fc20.x86_64.rpm

	echo "Type: \"bash status.sh\" to update your status"

	exit
fi
