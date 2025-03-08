noOfServers = 8401
batchServers = 1000
batchCount = 0
cnt = 1

for server in range(1, noOfServers, batchServers):
    batchCount = batchCount + 1
    cnt += 1

print(f"The total batchCount is : {batchCount}")

# noOfServers = 84670
# batchServers = 1000
# batchCount = 0
# cnt = 1
#
# for server in range(1, 8401, 1000):
#     print(f"{cnt}: Patching batch-{cnt} of servers")
#     batchCount = batchCount + 1
#     cnt += 1
# print(f"The total batchCount is : {batchCount}")
