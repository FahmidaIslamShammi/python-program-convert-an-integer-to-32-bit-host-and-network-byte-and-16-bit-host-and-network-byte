import socket
integer_value=int(input("Enter the integer value ="))

#for 32 bit
network_byte=socket.ntohl(integer_value)
host_byte=socket.htonl(integer_value)
print("For the given integer ",integer_value ,"32 bit network byte: ", network_byte)
print("For the given integer ",integer_value ,"32 bit host byte : ", host_byte)

#for 16 bit
network_byte_16=socket.ntohs(integer_value)
host_byte_16=socket.htons(integer_value)
print("For the given integer ",integer_value ,"16 bit network byte: ", network_byte_16)
print("For the given integer ",integer_value ,"16 bit host byte : ", host_byte_16)