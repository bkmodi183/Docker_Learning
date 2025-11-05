**🐳 Docker Volumes**

Docker volumes are used to persist data generated and used by containers. Unlike the container’s writable layer, data stored in volumes is not deleted when the container stops, restarts, or is removed.

Volumes are managed by Docker and can be shared between multiple containers, making them ideal for storing databases, logs, configuration files, and other data that must be retained independently of a container’s lifecycle.

**Key Benefits:**

1. **Data persistence:** Keeps data safe even if containers are deleted or recreated.
2. **Container sharing:** Multiple containers can access the same data.
3. **Easy backup & restore:** Volumes can be easily backed up, restored, or moved.
4. **Better performance:** More efficient than using bind mounts for Docker-managed data.

**Example Usage**

Below we will perform steps to create a persistent storage directory, create a Docker volume, attach it to containers, inspect it, and clean up unused volumes.

1. Create a local directory for persistent data
Command: **mkdir -p /home/user/docker-data**
Description: Creates a folder on your host machine to store container data persistently.

2. Create a Docker-managed named volume
Command: **docker volume create my_volume**
Description: Creates a Docker-managed volume that can be attached to containers.

3. List all Docker volumes
Command: **docker volume ls**
Description: Displays all Docker volumes available on the system.

4. Attach a local directory to a container (bind mount)
Command: **docker run -d --name my_container -v /home/user/docker-data:/app/data nginx:latest**
Description: Runs a container and mounts the local directory to a path inside the container.

5. Attach a Docker named volume to a container
Command: **docker run -d --name my_container -v my_volume:/app/data nginx:latest**
Description: Runs a container and mounts the Docker-managed volume to a path inside the container.

6. Inspect a Docker volume
Command: **docker volume inspect my_volume**
Description: Shows details about the volume, including its mount point and usage.

7. Remove unused Docker volumes
Command: docker volume prune
Description: Deletes all Docker volumes that are not currently used by any container.

**Quick Command Summary**

* Create local directory: mkdir -p /home/user/docker-data — Creates a folder on the host for persistent container data
* Create Docker volume: docker volume create my_volume — Creates a named Docker-managed volume
* List volumes: docker volume ls — Lists all Docker volumes
* Run container with local directory: docker run -v /home/user/docker-data:/app/data nginx — Runs a container with a bind-mounted 
  local folder
* Run container with named volume: docker run -v my_volume:/app/data nginx — Runs a container with a Docker-managed volume
* Inspect volume: docker volume inspect my_volume — Shows details of the specified volume
* Remove unused volumes: docker volume prune — Deletes all unused volumes

Notes: Volumes provide a safe and efficient way to persist and share data between containers. Data stored in a volume remains               available even if the container is removed. Prefer Docker-managed named volumes for portability and easier management.
