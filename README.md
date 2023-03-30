
## Run Locally

* Create a virtual environment
* Install the required libraries
* Run with `gunicorn` on port 80
* Go to `localhost` in a web browser

## Build and Run with Docker

* Build the Docker container (NOTE the period at the end)
  * The [`docker build`](https://docs.docker.com/engine/reference/commandline/build/) documentation

  `docker build -t web_counter .`
  
* Run the Docker container (without a volume)
  * The [`docker run`](https://docs.docker.com/engine/reference/commandline/run/) documentation
  
  `docker run -d -p 80:80 --name web_counter web_counter`
  
* Stop and remove the container
  * The [`docker stop`](https://docs.docker.com/engine/reference/commandline/stop/) documentation
  * The [`docker rm`](https://docs.docker.com/engine/reference/commandline/rm/) documentation

  `docker rm -f web_counter`
  
* Create a shell inside the running container
  * The ['docker 
exec`](https://docs.docker.com/engine/reference/commandline/exec/) 
documentation

  `docker exec -it web_counter bash`


## Mount Data Volume

* A data volume allows data persistence in a Docker container.
  * The [Volumes](https://docs.docker.com/storage/volumes/) documentation
* The local path must be absolute.
* In the shell [command substitution](https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html) is used to replace a command with its output (like a function call).

  `docker run -d -p 80:80 -v $(pwd)/data:/app/data --name web_counter web_counter`
  