# Cuda-project


Welcome to the Flask Metrics Tracker, or FMT by Harrison Lane, this guide will walk you through how to pull, configure & manage your own Grafana setup, alongside prometheus & Flask, using what we already have configured. 

It’s important to note that this will be using Docker as a way to host & manage the instances in question




Basic Setup:
if you simply wish for a list of commands here's what we've used
```
git clone https://github.com/Hlanetest/Cuda-project.git
cd Cuda-project
docker-compose up -d
http://172.16.238.10:8080/simple
http://172.16.238.12:3000
Username: admin
Password: MYPASS123
```

First thing we need is to ensure Docker/Docker-compose are installed & ready to go. 
If you’re unfamiliar please follow the links to setup docker & docker-compose:
Windows:
https://docs.microsoft.com/en-us/virtualization/windowscontainers/quick-start/set-up-environment?tabs=Windows-Server

Linux:
https://docs.docker.com/engine/install/ubuntu/

Docker-Compose:
https://docs.docker.com/compose/install/

After docker installation:
Now we move on to the configuration & setup.
In the elevated powershell, Run the following command:

**git clone https://github.com/Hlanetest/Cuda-project.git**
Once it’s cloned, run 
**cd Cuda-project**
Once inside run:
**docker-compose up -d**
This above command will tell docker-compose to use the file in our Current working directory, it’ll start pulling all the structure we need. This will run for a few moments and once it completes you should be returned to your normal screen

Once completed go to the following address
http://172.16.238.10:8080/simple
Refresh the page about 5 five times, then go to:
http://172.16.238.12:3000
Once there enter the following credentials
Username: **admin**
Password: **MYPASS123**

Click Login and once inside click the four blocks right above the compass, and click ‘Manage’
From manage you should see an ‘example Dashboard’ click that and you should see your request data being pipped through, alongside the CPU & memory data. 
