install_dependencies:
	@printf "\033[36mInstalling dependencies. Superuser password required.\n\033[0m"
	sudo apt-get update -y
	sudo apt-get install python3.8 -y
	sudo apt-get install python3-pip -y
	pip install build
	wget https://github.com/zricethezav/gitleaks/releases/download/v7.5.0/gitleaks-linux-amd64
	mv gitleaks-linux-amd64 gitleaks
	mv gitleaks ~/.local/bin 
	@printf "\033[36mDependencies installed successfully.\n\033[0m"


install:
	@printf "\033[36mInstalling project.\n\033[0m"
	python3 -m build
	pip install dist/vulDetect-0.5.tar.gz
	@printf "\033[36mvulDetect installed successfully\n\033[0m"


clean:
	@printf "\033[96mClearing working folder\n\033[0m"
	rm -r *


all: install_dependencies install
