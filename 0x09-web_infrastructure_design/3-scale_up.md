# Scaling Up Web Infrastructure

## Infrastructure Overview:

- **Servers (2)**: Two physical or virtual machines are being used to distribute the load and provide redundancy.

- **Domain Name (foobar.com)**: This is the human-readable label used to access the website. It is configured to point to the load balancer's IP address.

- **Load Balancer Cluster (HAproxy)**: HAproxy is a load-balancing software that distributes incoming requests across multiple servers. This cluster setup ensures high availability and redundancy.

- **Web Server (Nginx)**: Nginx is a web server software responsible for handling HTTP requests. It serves static content and forwards dynamic requests to the application server.

- **Application Server**: This server executes application logic, processes dynamic content, and communicates with the database.

- **Application Files (Code Base)**: These are the files containing the code that makes up the website. They are stored on both application servers and executed as needed.

- **Database (MySQL)**: MySQL is a database management system. It stores, organizes, and manages the website's data.

## Additional Elements:

### Load Balancer Cluster:

- **Why**: The load balancer cluster is added to distribute incoming requests across multiple servers. This improves performance, ensures high availability, and provides redundancy.

## Issues with this Infrastructure:

### Scaling Limitation:

- While this setup provides redundancy and improved performance, it may still struggle to handle a sudden surge in incoming traffic. Adding more servers or considering additional scalability options may be necessary.


