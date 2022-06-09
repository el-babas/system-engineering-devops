# User limit

exec {'user-limit':
  provider => shell,
  command  => 'sudo sed -i "s/holberton hard nofile 5/holberton hard nofile 500/" /etc/security/limits.conf && 
            sudo sed -i "s/holberton soft nofile 4/holberton soft nofile 400/" /etc/security/limits.conf'
}
