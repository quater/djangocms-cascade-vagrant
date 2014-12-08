from fabric.api import *
from fabric.context_managers import *
from fabric.contrib import *
from fabric.operations import *
from fabric.contrib.files import *
import os, datetime, time, sys, shutil, errno

def install_packages():
        sudo("aptitude update")
        sudo("aptitude -y install python-dev git nodejs npm")
        sudo("npm install -g bower")
        sudo("ln -s /usr/bin/nodejs /usr/bin/node")
        run("curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | sudo python2.7")
        sudo("pip install virtualenv")

def create_virtualenv():
    # Create virtual environment
    with cd("/home/vagrant/"):
        run("virtualenv cascadedemo")
        # Download the Django-Cascade examples from GitHub
        run("git clone -b 0.4.0 https://github.com/jrief/djangocms-cascade.git")
        # Place custom "manage.py" file into the /home/vagrant/djangocms-cascade/example/ directory
        put(os.getcwd() + '/manage.py', '/home/vagrant/djangocms-cascade/examples/')
        put(os.getcwd() + '/requirements.txt', '/home/vagrant/djangocms-cascade/examples/bs3demo/')
        with cd("/home/vagrant/djangocms-cascade/"):
            # Install bootstrap into the /home/vagrant/djangocms-cascade/bower_components/ directory
            run("source /home/vagrant/cascadedemo/bin/activate && bower install bootstrap --config.interactive=false")
            with cd("/home/vagrant/djangocms-cascade/examples"):
                # Install depending Python applications
                run("source /home/vagrant/cascadedemo/bin/activate && pip install -r bs3demo/requirements.txt")
                # Djangcms-Cascade 0.4.0 is not yet available in the Python Package Index and therefore it's installed directly from GitHub
                run("source /home/vagrant/cascadedemo/bin/activate  && pip install git+https://github.com/jrief/djangocms-cascade.git@0.4.0")
                run("source /home/vagrant/cascadedemo/bin/activate && python manage.py syncdb")
                
def main():

    start_time = time.time()

    install_packages()
    create_virtualenv()

    print "This programme executed in %s seconds." % (time.time() - start_time)
