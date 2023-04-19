## SETUP ONE TIME
- Make ec2 instance and ssh to it
- Set up ec2 instance
	- `sudo yum install -y git`
	- `git clone https://github.com/geoffrey-kleinberg/csci220_final.git`
	- `sudo yum install -y docker`
	- `sudo service docker start`
	- `sudo usermod -a -G docker ec2-user`
	- `cd csci220_final`
	- `mkdir data`
- Create a file in the home directory of the ec2 instance called `redeploy` with the following code:
	- `docker rm -f web_counter`
	- `cd csci220_final`
	- `git pull`
	- `docker build -t web_counter .`
	- `docker run -d -p 80:80 -v $(pwd)/data:/app/data --name web_counter web_counter`
- Run the following command: `chmod +x redeploy`
  
