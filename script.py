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
    if id%4 == 0:
        size = "8"
    elif id%4 == 1:
        size = "8.5"
    elif id%4 == 2:
        size = "9"
    elif id%4 == 3:
        size = "9.5"
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
    "nikesize": size,
    "starttime": time
    }
    id += 1
    tasks.append(task)
output = open('output.txt', 'a')
output.write(json.dumps(tasks))

    