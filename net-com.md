#wip

1. A 'Link' shall consist of 3 parts: 'Domain', 'Path' and 'Element', each of which are a string of characters.
2. A Domain is resolved to an IPV4 or IPV6 address using DNS, this address is the 'Server IP'

# Establishment Packet
| Byte 0 till 15 (16 bytes) | Byte 16 till 47 (32 Bytes) | Byte 48 till 79 (32 Bytes) | Byte 80 till 111 (32 Bytes) |
| :-: | :-: | :-: | :-: |
| Temporary Connection ID | Encryption Algorithm Options | Verification Algorithm Options | Key Establishment Options |
1. The 'Temporary Connection ID' is a random number chosen by the client.

| Byte 0 till 15 (16 bytes) | Byte 16 till 31 (16 Bytes) | Byte 16 till 16 (1 Byte) | Byte 17 till 17 (1 Byte) | Byte 18 till 18 (1 Bytes) | Byte 19 till N (N Bytes) |
| :-: | :-: | :-: | :-: | :-: | :-: |
| Temporary Connection ID | Chosen Connection ID | Chosen Encryption | Chosen Verification | Chosen Key Establishment Algorithm | Key Establishment Part |
1. The 'Chosen Connection ID' is the final Connection ID

| Byte 0 till 15 (16 bytes) | Byte 16 till N (N Bytes) |
| :-: | :-: |
| Connection ID | Key Establishment Part |

# Packet
1. A 'Packet' consists of a UDP header with the below format imemdiately following it.
| Byte 0 till 15 (16 Bytes) | Byte 16 till 23 (8 Bytes) | Byte 24 till 24 (1 Byte) | Byte 25 till 32 (8 Bytes) | Byte 33 till 34 (2 Bytes)  | Byte 27 till N (N Bytes) | Byte N+1 till N+4 (4 Bytes) | Byte N+5 till M (M Bytes) | Byte M+1 till M+4 (4 Bytes) |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |  :-: |
| Connection ID | Packet Number | GET (0) / PUSH (1) / PATCH (2) | Link Element | Length of Link Path | Link Path | Length of Data | Data | Sign |
2. A Packet is used for all data going to the 'Server'.
3. A Packet's Data, Link Element, Length of Link Path, Link Path and Length of Data are always encrypted using the established encryption algorithm.
