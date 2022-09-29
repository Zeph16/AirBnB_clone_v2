# Puppet script that configures Nginx server on a brand new machine

exec {'update':
  provider => shell,
  command  => 'apt-get -y update',
  before   => Exec['install Nginx'],
}

exec {'install Nginx':
  provider => shell,
  command  => 'apt-get -y install nginx',
  before   => Exec['start Nginx'],
}

exec {'start Nginx':
  provider => shell,
  command  => 'service nginx start',
  before   => Exec['create first directory'],
}

exec {'create first directory':
  provider => shell,
  command  => 'mkdir -p /data/web_static/releases/test/',
  before   => Exec['create second directory'],
}

exec {'create second directory':
  provider => shell,
  command  => 'mkdir -p /data/web_static/shared/',
  before   => Exec['content into html'],
}

exec {'content into html':
  provider => shell,
  command  => 'echo "Hello World!" | tee /data/web_static/releases/test/index.html',
  before   => Exec['symbolic link'],
}

exec {'symbolic link':
  provider => shell,
  command  => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
  before   => Exec['put location'],
}

exec {'put location':
  provider => shell,
  command  => 'sed -i \'38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n\' /etc/nginx/sites-available/default',
  before   => Exec['restart Nginx'],
}

exec {'restart Nginx':
  provider => shell,
  command  => 'service nginx restart',
  before   => File['/data/']
}

file {'/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}
