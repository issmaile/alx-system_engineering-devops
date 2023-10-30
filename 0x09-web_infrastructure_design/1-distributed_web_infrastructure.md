# Three-Server Web Infrastructure for foobar.com

## Infrastructure Overview:

- **Servers (2)**: Two physical or virtual machines are being used to distribute the load and provide redundancy.

- **Domain Name (foobar.com)**: This is the human-readable label used to access the website. It is configured to point to the load balancer's IP address.

- **Load Balancer (HAproxy)**: HAproxy is a load-balancing software that distributes incoming requests across multiple servers. It ensures that the workload is evenly distributed, improving performance and reliability.

- **Web Server (Nginx)**: Nginx is a web server software responsible for handling HTTP requests. It serves static content and forwards dynamic requests to the application server.

- **Application Server**: This server executes application logic, processes dynamic content, and communicates with the database.

- **Application Files (Code Base)**: These are the files containing the code that makes up the website. They are stored on both application servers and executed as needed.

- **Database (MySQL)**: MySQL is a database management system. It stores, organizes, and manages the website's data.

## Additional Elements:

### Load Balancer (HAproxy):
- **Why**: The load balancer is added to distribute incoming requests across multiple servers. This improves performance, ensures high availability, and provides redundancy.

- **Distribution Algorithm**: The load balancer is configured with a Round Robin distribution algorithm. It cycles through the servers in a circular manner, evenly distributing requests.

- **Active-Active vs Active-Passive**:
  - The setup is Active-Active, meaning all servers are actively handling requests simultaneously. This provides high availability and load distribution.

### Database Primary-Replica Cluster:

- **How it Works**: In a Primary-Replica (Master-Slave) cluster, the Primary node (Master) handles write operations and replicates data to the Replica nodes (Slaves). Replica nodes handle read operations. This provides redundancy and improves performance.

- **Difference for Application**:
  - The application is configured to perform write operations on the Primary node, ensuring data consistency. Read operations can be distributed across both Primary and Replica nodes to balance the load.

## Issues with this Infrastructure:

### Single Points of Failure (SPOF):

- The load balancer is a potential single point of failure. If it goes down, it can disrupt the distribution of incoming requests.

### Security Issues:

- There is no mention of a firewall, which leaves the infrastructure vulnerable to unauthorized access or attacks.

- HTTPS is not mentioned, which means data transmission between the servers and users may not be encrypted, posing a security risk.

### No Monitoring:

- The infrastructure lacks a monitoring system to track server health, performance metrics, and potential issues. This could lead to delayed response in case of problems.


