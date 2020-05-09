import json

productlink = input("Insert link: ")
sku = input("Insert sku: ")
proxy = input("Insert proxylist: ")
time = input("Insert time (ex. 06:00:00): ")

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

id = 1
tasks = []
for line in lines:
    data = line.split(':')
    task = {
    "task_id": str(id),
    "site": "Snkrs CA",
    "product": productlink,
    "sku": sku,
    "profile": data[2],
    "proxies": proxy,
    "nikeemail": data[0],
    "nikepassword": data[1],
    "nikesize": data[3],
    "starttime": time
    }
    id += 1
    tasks.append(task)
output = open('output.txt', 'w')
output.write(json.dumps(tasks))

    