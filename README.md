# Vagrant Box to showcase Djangocms-Cascade

This Vagrant start up script allows you to evaluate the [*DjangoCMS 3*](https://github.com/divio/django-cms) with [*Djangocms-Cascade 0.4.0*](https://github.com/jrief/djangocms-cascade/tree/0.4.0), [*Bootstrap*](http://getbootstrap.com/) example, without efforts.

Presuming you have [Vagrant](https://docs.vagrantup.com/v2/getting-started/index.html) setup already, this Vagrant start script will get you a working *DjangoCMS* with *Djangocms-Cascade* up and running in literally minutes.

**Download from GitHub**

`$ git clone https://github.com/quater/djangocms-cascade-vagrant.git`

`$ cd djangocms-cascade-vagrant`

**Vagrant up**

`$ vagrant up`

> This script will run for a couple of minutes. At the end, ou will be prompted to enter a password for the **admin** user.

**SSH into the Vagrant machine**

`$ vagrant ssh`

**Start the runserver**

`$ source /home/vagrant/cascadedemo/bin/activate && cd /home/vagrant/djangocms-cascade/examples/ && python manage.py runserver 0.0.0.0:8000`

**Connect**

Open browser on your Vagrant host by using the URL:
`http://localhost:8000/`

> Login with user **admin** and the password which you have set during *vagrant up*.

**Add a page**

Navigate to **example.com > Administration > Pages > Add Page**

> Once you have a page created and edited, you will have the **Page** menu item in the navigation bar available as well. Now, follow the instructions on [*Read The Docs*](http://djangocms-cascade.readthedocs.org/en/latest/).
