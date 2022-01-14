# Big Fake Orders

I want to create a big csv file (2GB) containing fake orders related to an Ecommerce.

I made it using two differents techniques:
1. Using streams to send the datas in chunks and reduce the RAM usage.
2. Using the classic append sync method, creating n rows in blocks and add them to the original file.


## Installation

Use the Dockerfile to generate a project image and run a container or download it from [Docker Hub](https://hub.docker.com/repository/docker/francescodb86/td-challenge).


## How to run

```bash
node index.js
```

```javascript
// Select how you want to create the csv file.
Do you want to create the csv using streams (0) or in append sync mode (1)? 

// enter 0
Ok Streams!

// enter 1
Ok Sync!

// Every 100k rows
Updated block 0
Updated block 1
Updated block 2
ecc...
```