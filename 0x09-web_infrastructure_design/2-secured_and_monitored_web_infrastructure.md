# Secured Three-Server Web Infrastructure for foobar.com

## Infrastructure Overview:

- **Servers (3)**: Three physical or virtual machines provide redundancy and distribute the load.

- **Domain Name (foobar.com)**: Human-readable label used to access the website. It points to the load balancer's IP address.

- **Load Balancer (HAproxy)**: Distributes incoming requests across multiple servers, improving performance and ensuring high availability.

- **Firewalls (3)**: Provide security by controlling incoming and outgoing traffic based on an applied rule set. They protect against unauthorized access and potential security threats.

- **SSL Certificate**: Enables HTTPS, encrypting the traffic between the server and the user's browser.

- **Monitoring Clients (Sumologic)**: Collect data for monitoring services to track server health, performance metrics, and potential issues.

- **Web Server (Nginx)**, **Application Server**, **Database (MySQL)**, and **Application Files (Code Base)** are also part of the infrastructure.

## Additional Elements:

### Firewalls (3):
- **Why**: Firewalls are added to enhance security. They control traffic flow, ensuring only authorized connections are allowed and protecting against potential threats.

### SSL Certificate:
- **Why HTTPS**: Traffic is served over HTTPS to encrypt data transmission between the server and the user's browser. This ensures confidentiality and integrity of sensitive information.

### Monitoring (Sumologic):
- **What it's Used For**: Monitoring is used to track server health, performance, and identify potential issues or anomalies. It provides insights for proactive maintenance.

- **Data Collection**: The monitoring tool (Sumologic) collects data by deploying monitoring clients on each server. These clients gather performance metrics, logs, and other relevant data.

### Monitoring Web Server QPS:
- To monitor web server QPS (Queries Per Second), set up custom metrics in the monitoring tool to track incoming requests and measure the server's processing capacity.

## Issues with this Infrastructure:

### Terminating SSL at Load Balancer Level:
- This is an issue because it means that the traffic between the load balancer and the web servers is not encrypted. If intercepted, sensitive information could be compromised.

### Single MySQL Server Accepting Writes:
- This is a potential single point of failure for write operations. If the MySQL server fails, it could result in data loss or service interruption.

### Identical Components on Servers:
- Having servers with identical components (database, web server, and application server) might be a problem because it could lead to a lack of diversity in the infrastructure. A failure in one component may affect all servers.


