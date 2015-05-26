Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provision :shell, path: "bootstrap.sh"
  config.vm.network "forwarded_port", guest: 5000, host: 5050
  config.vm.network "forwarded_port", guest: 8888, host: 8889

  # Add memory (needed to install Pandas, munge data, etc.)
  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
  end
end
