# -*- mode: ruby -*-
# vi: set ft=ruby :

# For development, it is not needed when run on the production environment.
#Vagrant.require_plugin "vagrant-fabric"

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  # Run "fabfile.py" during initial "vagrant up"
  config.vm.provision :fabric do |fabric|
    fabric.fabfile_path = "./fabfile.py"
    fabric.tasks = ["main", ]
  end

  # Allocate sufficient resources
  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
    v.cpus = 2
  end

end
