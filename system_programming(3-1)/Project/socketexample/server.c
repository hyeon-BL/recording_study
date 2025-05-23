#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    struct addrinfo hints, *res;
    int sockfd, clientfd, status;
    char buffer[1024];

    // Set up socket parameters
    memset(&hints, 0, sizeof hints);
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_flags = AI_PASSIVE;
    
    // Resolve the IP address of the local host using getaddrinfo
    status = getaddrinfo(NULL, "5000", &hints, &res);
    if (status != 0) {
        fprintf(stderr, "getaddrinfo error: %s\n", gai_strerror(status));
        exit(1);
    }

    // Create a socket object and bind it to the local address
    sockfd = socket(res->ai_family, res->ai_socktype, res->ai_protocol);
    if (sockfd == -1) {
        perror("socket error");
        exit(1);
    }

    int reuse = 1;
    setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &reuse, sizeof reuse);

    status = bind(sockfd, res->ai_addr, res->ai_addrlen);
    if (status == -1) {
        perror("bind error");
        exit(1);
    }

    // Listen for incoming connections
    status = listen(sockfd, 1);
    if (status == -1) {
        perror("listen error");
        exit(1);
    }
    
    printf("Listening on port 5000...\n");

    while (1) {
        // Accept a new connection
        clientfd = accept(sockfd, NULL, NULL);
        if (clientfd == -1) {
            perror("accept error");
            continue;
        }
        
        printf("Accepted connection from client\n");

        // Receive the message from the client
        int bytes_received = recv(clientfd, buffer, sizeof buffer - 1, 0);
        buffer[bytes_received] = '\0';
        printf("Received message: %s", buffer);

        // Send a response back to the client
        const char *response = "Hello, client!\n";
        send(clientfd, response, strlen(response), 0);
        printf("Sent response to client\n");

        // Close the socket connection
        close(clientfd);
        printf("Closed connection to client\n");
    }

    // Free the address information
    freeaddrinfo(res);

    return 0;
}
