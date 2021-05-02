command_not_found_handle() {
	/data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
}

PS1='\033[91m\t\033[96m • '

clear
cd /data/data/com.termux/files/home/termux
python2 irul.py