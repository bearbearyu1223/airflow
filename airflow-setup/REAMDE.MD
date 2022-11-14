## Study Notes
___
### Nov 13, 2022
* Read this blog post on Medium: [Setting Up Apache Airflow with Docker-Compose in 5 Minutes](https://towardsdatascience.com/setting-up-apache-airflow-with-docker-compose-in-5-minutes-56a1110f4122). 
  * Need install homebrew on Apple Silicon Mac
  ```
  $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)
  ```
  * Then install postgresql via *homebrew*
  ```
  $ brew install postgresql
  ```
  * Need install docker by following the instruction [here](https://docs.docker.com/desktop/install/mac-install/). 
  * To use `docker compose` on Apple silicon macs, install Rosetta 2 with `softwareupdate --install-rosetta`, 
then uncheck *Use Docker Compose V2*  in *Docker Dashboard -> Settings -> General*.
  * Check out a quick intro to Docker Compose [here](https://www.baeldung.com/ops/docker-compose).
* Airflow uses Fernet to encrypt passwords in the connection configuration and the variable configuration. It guarantees that a password encrypted using it cannot be manipulated or read without the key. Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography.See Airflow documentation [here](https://airflow.apache.org/docs/apache-airflow/stable/security/secrets/fernet.html).  
  * To generate a Fernet key, install cryptography
    
  ```
    $ pip install cryptography
  ```
    then generate a fernet key via:
  ```
    $ python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
  ```
* To run the Airflow DAGs inside the container, cd to the *airflow* directory: 
  * Head over to the terminal and spin up all the necessary containers by running
  ```
  $ docker-compose up -d --remove-orphans
  ```
  * Run the following command in our terminal
  ```
  $ docker exec -it --user airflow airflow-scheduler bash -c "airflow dags list"
  ```
  * Check the results and the Airflow Web UI by visiting *http://localhost:8080*
  * Stop the running containers by simply executing
  ```
  $ docker-compose down
  ```
  