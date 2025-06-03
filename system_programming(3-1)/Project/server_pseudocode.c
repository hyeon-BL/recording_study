#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/select.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <ctype.h>      // for isprint()
#include "cJSON.h"      // cJSON header
#define HOST "10.150.21.133"
#define PORT 12345
#define BUFFER_SIZE 4096
#define TIMEOUT_SEC 3.0
int connect_to_server(void) {
    int sockfd;
    struct sockaddr_in serv_addr;
    // 1. Create a TCP/IP socket
    //    AF_INET: IPv4, SOCK_STREAM: TCP
    // 2. Zero out the server address structure
    // 3. Convert HOST from text to binary form and store in serv_addr.sin_addr
    // 4. Attempt to connect to the server
    //    connect() returns 0 on success, -1 on error
    // 5. If we reach here, the socket is connected successfully
    return sockfd;
}
int read_response_line(int sockfd, char *buf, int maxlen) {
    int total_read = 0;
    fd_set readfds;
    struct timeval tv;
    char c;
    int ret;
    // Continue reading until we fill maxlen-1 bytes or encounter '\n'
    while (total_read < maxlen - 1) {
        // 1. Initialize the file descriptor set for select()
        // 2. Set the timeout for select()
        // 3. Wait for data to be available on sockfd, or for timeout
        // 4. Data is available; read one byte
        // 5. If the received character is newline, stop reading further
        // 6. Otherwise, store the character in buf
    }
    // 7. Null-terminate the string
    buf[total_read] = '\0';
    return total_read;
}
char *build_payload(int index) {
    cJSON *root = NULL;
    char *json_str = NULL;
    switch (index) {
        case 0:  // register with valid username
            root = cJSON_CreateObject();
            cJSON_AddStringToObject(root, "type", "register");
            cJSON_AddStringToObject(root, "username", "Alice");
            break;
        case 1:  // register with missing username
            root = cJSON_CreateObject();
            cJSON_AddStringToObject(root, "type", "register");
            cJSON_AddStringToObject(root, "username", "");
            break;
        case 2:  // register_fail explicit
            root = cJSON_CreateObject();
            cJSON_AddStringToObject(root, "type", "register_fail");
            cJSON_AddStringToObject(root, "reason", "username taken");
            break;
        case 3:  // invalid_move with reason
            root = cJSON_CreateObject();
            cJSON_AddStringToObject(root, "type", "invalid_move");
            cJSON_AddStringToObject(root, "reason", "out of bounds");
            break;
        case 4:  // not_your_turn
            root = cJSON_CreateObject();
            cJSON_AddStringToObject(root, "type", "not_your_turn");
            break;
        case 5:  // move with missing fields (invalid payload)
            root = cJSON_CreateObject();
            cJSON_AddStringToObject(root, "type", "move");
            cJSON_AddStringToObject(root, "username", "Alice");
            cJSON_AddNumberToObject(root, "sx", 1);
            cJSON_AddNumberToObject(root, "sy", 1);
            // deliberately omit tx, ty
            break;
        case 6:  // move with valid fields
            root = cJSON_CreateObject();
            cJSON_AddStringToObject(root, "type", "move");
            cJSON_AddStringToObject(root, "username", "Alice");
            cJSON_AddNumberToObject(root, "sx", 1);
            cJSON_AddNumberToObject(root, "sy", 1);
            cJSON_AddNumberToObject(root, "tx", 2);
            cJSON_AddNumberToObject(root, "ty", 2);
            break;
        case 7:  // pass
            root = cJSON_CreateObject();
            cJSON_AddStringToObject(root, "type", "pass");
            break;
        case 8:  // game_start
            root = cJSON_CreateObject();
            cJSON_AddStringToObject(root, "type", "game_start");
            break;
        case 9:  // your_turn
            root = cJSON_CreateObject();
            cJSON_AddStringToObject(root, "type", "your_turn");
            cJSON_AddNumberToObject(root, "timeout", 5);
            break;
        case 10: // game_over
            root = cJSON_CreateObject();
            cJSON_AddStringToObject(root, "type", "game_over");
            break;
        case 11: // unrecognized type
            root = cJSON_CreateObject();
            cJSON_AddStringToObject(root, "type", "foo_bar");
            cJSON_AddNumberToObject(root, "data", 123);
            break;
        case 12: // Malformed JSON: return raw string
            // Return a strdup of the malformed JSON
            return strdup("This is not JSON");
        default:
            return NULL;
    }
    // Convert cJSON object to string without formatting
    json_str = cJSON_PrintUnformatted(root);
    cJSON_Delete(root);
    return json_str;
}
int main(void) {
    const int num_payloads = 13;
    for (int i = 0; i < num_payloads; i++) {
        char *payload = build_payload(i);
        if (!payload) {
            fprintf(stderr, "Failed to build payload #%d\n\n", i + 1);
            continue;
        }
        printf("== Test Payload (%d/%d) ==\n%s\n", i+1, num_payloads, payload);
        int sockfd = connect_to_server();
        if (sockfd < 0) {
            fprintf(stderr, "Failed to connect to server for payload #%d\n\n", i+1);
            free(payload);
            continue;
        }
        // Send payload + newline
        size_t len = strlen(payload);
        char *sendbuf = malloc(len + 2);
        if (!sendbuf) {
            perror("malloc()");
            close(sockfd);
            free(payload);
            continue;
        }
        memcpy(sendbuf, payload, len);
        sendbuf[len] = '\n';
        sendbuf[len + 1] = '\0';
        if (send(sockfd, sendbuf, len + 1, 0) < 0) {
            perror("send()");
            close(sockfd);
            free(sendbuf);
            free(payload);
            printf("\n");
            continue;
        }
        // Read up to two response lines
        char respbuf[BUFFER_SIZE];
        int ret;
        // First response (ack or unrecognized_JSON_format)
        ret = read_response_line(sockfd, respbuf, BUFFER_SIZE);
        if (ret > 0) {
            printf("Response 1: %s\n", respbuf);
        } else if (ret == 0) {
            printf("Response 1: [connection closed]\n");
        } else {
            printf("Response 1: [timeout or error]\n");
        }
        // Second response (actual payload-specific response), if any
        ret = read_response_line(sockfd, respbuf, BUFFER_SIZE);
        if (ret > 0) {
            printf("Response 2: %s\n", respbuf);
        } else if (ret == 0) {
            printf("Response 2: [connection closed]\n");
        } else {
            printf("Response 2: [timeout or error]\n");
        }
        close(sockfd);
        free(sendbuf);
        free(payload);
        printf("\n");
        // Small pause between tests
        usleep(100000);  // 100 ms
    }
    return 0;
}









