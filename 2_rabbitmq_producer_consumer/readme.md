# parallel data preprocessing example using producer consumer pattern with rabbitmq

## setting rabbitmq with docker

    docker run -d --name rabbitmq -p 5672:5672 -p 8080:15672 rabbitmq:3-management
    
monitoring ip: 127.0.0.1:8080 <br>
default username: guest <br>
default password: guest <br>
