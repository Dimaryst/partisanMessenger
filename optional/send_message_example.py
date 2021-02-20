import json
import socket
from datetime import datetime

#
sender_uuid = "sender_uuid_example"
recipient_uuid = "recipient_uuid_example"
recipient_ip = "localhost"
recipient_port = 7045

message = "message_some_text"
date = str(datetime.now())

package = (sender_uuid, recipient_uuid, message, date)
package = json.dumps(package)
print("Trying to send to recipient: ", " ", " ")
print(package)

sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
try:
    sock.connect((recipient_ip, recipient_port))
    print("Trying to send to recipient: ", recipient_ip, socket.SOCK_STREAM)
    print(package)
    sock.send(str(package).encode('utf-8'))

except Exception as e:
    print(f"Failed ({e})")
finally:
    sock.close()
