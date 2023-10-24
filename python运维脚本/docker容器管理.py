import docker

client = docker.from_env()

# 列出所有容器
containers = client.containers.list()

for container in containers:
    print(container.name)
    print(container.id)
    print(container)


# 启动容器
# container = client.containers.get('container_id')
# container.start()

# # 停止容器
# container.stop()
#
# # 删除容器
# container.remove()

