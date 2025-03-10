  #!/bin/bash

  task_1(){
    apt update -y
    apt upgrade -y
    apt install -y nginx apache2-utils ufw fail2ban vim
  }


  task_2(){
      # Create user johndoe with disabled password
    sudo adduser --disabled-password --gecos "" johndoe

    # Create user janedoe with disabled password
    sudo adduser --disabled-password --gecos "" janedoe

    # Verify users are created
    cat /etc/passwd | grep -E 'johndoe|janedoe'
    sudo systemctl stop apache2 && sudo systemctl disable apache2 && sudo systemctl mask apache2 && sudo sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config && sudo sed -i 's/^#\?PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config && sudo systemctl restart ssh && echo "Security hardening completed!"

    sudo systemctl stop apache2 && sudo systemctl disable apache2 && sudo systemctl mask apache2 && sudo apt remove --purge -y apache2 apache2-utils apache2-bin apache2.2-common && sudo apt autoremove -y && sudo pkill -f apache2 && ! systemctl is-active --quiet apache2 && echo "Apache2

  }

  task_1
  task_2
