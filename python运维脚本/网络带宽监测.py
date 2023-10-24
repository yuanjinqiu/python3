import psutil
import time

interface = "en0"

while True:
    net_io = psutil.net_io_counters(pernic=True)[interface]
    sent_bytes = net_io.bytes_sent
    recv_bytes = net_io.bytes_recv
    print(f"Sent: {sent_bytes} bytes | Received: {recv_bytes} bytes")
    time.sleep(1)