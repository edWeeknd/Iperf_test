import iperf3

# Set up test
# Remote iperf server IP
server_ip = '127.0.0.1'
test_duration = 5
bandwidth = 20 #in Mbps



# Set Iperf Client Options
# Run 10 parallel streams on port 5201 for duration w/ reverse
client = iperf3.Client()
client.server_hostname = server_ip
client.zerocopy = True
client.verbose = False
client.reverse = True
client.port = 5201
client.num_streams = 2
client.duration = int(test_duration)
client.bandwidth = bandwidth*10**6

# Run iperf3 test
result = client.run()

# extract relevant data
sent_mbps = int(result.sent_Mbps)
received_mbps = int(result.received_Mbps)

print('sent_mbps: ')
print(sent_mbps)
print('received_mbps: ')
print(received_mbps)
print("*"*10)
print(result.text)

