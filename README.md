## Overview
This project demonstrates continuous integration (CI) and continuous deployment (CD) using GitHub Actions. It runs the Dockerized web_counter app on an Amazon EC2 instance, with an `isEven()` function that sets the color of the text based on if the number is even. CI is demonstrated by an action that fires every time a pull request is made and tests the `isEven()` function. CD is demonstrated by an action that fires every time there is a push to main that redeploys the website with the new changes.

## Setup
- Set up an EC2 instance with the following commands
	- `sudo yum install -y git`
	- `git clone https://github.com/geoffrey-kleinberg/csci220_final.git`
	- `sudo yum install -y docker`
	- `sudo service docker start`
	- `sudo usermod -a -G docker ec2-user`
- Modify the `REMOTE_HOST` in `.github/workflows/redeploy.yml` with the EC2 IP address

Then, whenever a pull request or a push to main occurs, the actions will fire automatically.
  
## Technologies Used

- [GitHub Actions](https://github.com/features/actions)
- [Amazon EC2](https://aws.amazon.com/ec2/)
- [Docker](https://www.docker.com/)

## Background Sources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [How to Make GitHub Secrets (Secure Authentication)](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [Use GitHub Actions to SSH to Amazon EC2 Instance](https://dev.to/aldora/github-actions-ssh-into-aws-ec2-25ib)
