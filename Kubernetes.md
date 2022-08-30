[toc]

# Kubernetes

## 概述

- Master: k8s的主控组件，对应的对象是node。
- Node: 是k8s集群的机器节点，相当于master-node。一个node就对应一个具体的物理机或者虚拟机。
- Container: 是一个镜像容器，一个container是一个镜像实例
- Pod: 是k8s集群的最小单元，一个pod可以包含一个或者多个container
- Service: 多个相同的pod组成一个服务，统一对外提供服务。
- Volume: 存储卷，pod对外暴露的共享目录，它可以挂载在宿主机上，这样就能让同node上多个pod共享一个目录。
- Replication Controller: 用于控制pod集群的控制器，可以制定各种规则来让它控制一个service中的多个pod的创建和消亡, 很多地方简称为rc。
- Namespace: 命名空间，用于将一个k8s集群隔离成不同的空间，pod, service, rc, volume 都可以在创建的时候指定其namespace。
- StatefulSet: 有状态集群，比如一个主从的mysql集群就是有状态集群，需要先启动主再启动从，这就是一种有状态的集群。
- Persistent Volume: 持久存储卷。之前说的volume是挂载在一个pod上的，多个pod(非同node)要共享一个网络存储，就需要使用持久存储卷，简称为pv。
- Persistent Volume Claim: 持久存储卷声明。他是为了声明pv而存在的，一个持久存储，先申请空间，再申明，才能给pod挂载volume，简称为pvc。
- Label: 标签。我们可以给大部分对象概念打上标签，然后可以通过selector进行集群内标签选择对象概念，并进行后续操作。
- Secret: 私密凭证。密码保存在pod中其实是不利于分发的。k8s支持我们创建secret对象，并将这个对象打到pod的volume中，pod中的服务就以文件访问的形式获取密钥。
- EndPoint: 用于记录 service 和 pod 访问地址的对应关系。只有 service 配置了 selector, endpoint controller 才会自动创建endpoint对象。

### Master节点（默认不参加实际工作）

- Kubectl：客户端命令行工具，作为整个K8s集群的操作入口；
- Api Server：在K8s架构中承担的是“桥梁”的角色，作为资源操作的唯一入口，它提供了认证、授权、访问控制、API注册和发现等机制。客户端与k8s群集及K8s内部组件的通信，都要通过Api Server这个组件；
- Controller-manager：负责维护群集的状态，比如故障检测、自动扩展、滚动更新等；
- Scheduler：负责资源的调度，按照预定的调度策略将pod调度到相应的node节点上；
- Etcd：担任数据中心的角色，保存了整个群集的状态；





### Node节点

- Kubelet：负责维护容器的生命周期，同时也负责Volume和网络的管理，一般运行在所有的节点，是Node节点的代理，当Scheduler确定某个node上运行pod之后，会将pod的具体信息（image，volume）等发送给该节点的kubelet，kubelet根据这些信息创建和运行容器，并向master返回运行状态。（自动修复功能：如果某个节点中的容器宕机，它会尝试重启该容器，若重启无效，则会将该pod杀死，然后重新创建一个容器）；
- Kube-proxy：Service在逻辑上代表了后端的多个pod。负责为Service提供cluster内部的服务发现（Kube-proxy始终监视着apiserver中有关service的变动信息，获取任何一个与service资源相关的变动状态，通过watch监视，一旦有service资源相关的变动和创建，kube-proxy都要转换为当前节点上的能够实现资源调度规则）和负载均衡（外界通过Service访问pod提供的服务时，Service接收到的请求后就是通过kube-proxy修改iptables来转发到pod上的）；
- container-runtime：是负责管理运行容器的软件，比如docker
- Pod

## Network

### 概述

pod的ip在重启后会发生改变，当再想要进行访问时就访问不到了。K8s为了解决这样的问题提出了service的方式。Service背后定义了服务访问的入口地址，背后是由pod副本组成的集群，Service与Pod间通过LabelSerlector完成对接。

kube-proxy提供了负载均衡策略，将对Service的请求转发到和Service匹配的某个pod实例上，并实现会话保持的机制。

K8S还为ClusterIP提供了DNS映射，可以直接用service name访问。

### IP类型

NodeIP: Node的IP地址，是k8s集群中节点的物理网卡ip，真实存在的物理网络，可以和所有属于这个网络的服务器通信使用，集群外服务访问集群内部时，需要使用该ip访问。

PodIP：每个POD的IP地址，是Docker Engine根据Docker0网桥的IP地址段分配的，是一个虚拟的二层网络，集群内部POD之间通信时就是使用该podIP访问，真实的TCP/IP流量通过NodeIP所在的物理网卡流出。

ClusterIP：Service的虚拟ip，仅作用于Service这个对象，由k8s管理和分配，智能解析serviceport组成通信端，不具备TCP/IP通信的基础。

### HeadlessService

pod访问HeadlessService时，HeadlessService会返回他所指向的pod列表。当pod通过HeadlessService拿到列表后会采用自己的负载均衡策略或者其他的一些什么策略来访问pod。

```yaml
spec:
  ports:
  - port: 80
    name: web
  clusterIP: None #HeadlessService
```



## 集群内访外

### Ip+port

pod可以直接通过ip+port的方式访问外部服务

### OutService

定义一个空的service，它不选择任何集群内的pod。但是可以配置与他对应的Endpoint（与service具有相同的名字)，pod通过访问service的DNS时就可以访问到集群外部的服务。

```yaml
# cat nginx-svc-external.yaml 
apiVersion: v1
kind: Service
metadata:
  labels:
    app: nginx-svc-external
  name: nginx-svc-external
spec:
  ports:
  - name: http 
    port: 80
    protocol: TCP 
    targetPort: 80 
  sessionAffinity: None
  type: ClusterIP 


# cat nginx-ep-external.yaml 
apiVersion: v1
kind: Endpoints
metadata:
  labels:
    app: nginx-svc-external
  name: nginx-svc-external
  namespace: default
subsets:
- addresses:
  - ip: 192.7.44.33 #外部服务的ip地址
  ports:
  - name: http
    port: 80 #外部服务的端口号
    protocol: TCP
```



## 集群外访内

### NodePort

集群外部可以通过访问 `nodeIP:nodePort` 访问该服务

### LoadBalancer

Load balancer组件独立于k8s集群之外，通常是一个硬件的负载均衡器或者以软件的方式实现，例如HAProxy或者Nginx。



## 其他

### **探针**

针对container。

类型：

1.  livenessProbe探针，失败重启
2.  ReadinessProbe探针，失败移除endpoint无法访问，成功放回
3. startupProbe探针，防止启动较慢

方式：

1. Exec,执行命令，返回的值为“0”，则表示健康，如果为非0，则表示异常
2. httpget，返回的状态码为200-399则表示容器健康
3. tcpSocket，能够建立TCP连接，则表明容器健康



### **镜像的下载策略imagePullPolicy**

- Always：镜像标签为latest时，总是从指定的仓库中获取镜像；
- Never：禁止从仓库中下载镜像，也就是说只能使用本地镜像；
- IfNotPresent：仅当本地没有对应镜像时，才从目标仓库中下载。
- 默认的镜像下载策略是：当镜像标签是latest时，默认策略是Always；当镜像标签是自定义时（也就是标签不是latest），那么默认策略是IfNotPresent。



### **标签与标签选择器**

标签：是当相同类型的资源对象越来越多的时候，为了更好的管理，可以按照标签将其分为一个组，为的是提升资源对象的管理效率。

标签选择器：就是标签的查询过滤条件。目前API支持两种标签选择器：

- 基于等值关系的，如：“=”、“”“==”、“！=”（注：“==”也是等于的意思，yaml文件中的matchLabels字段）；
- 基于集合的，如：in、notin、exists（yaml文件中的matchExpressions字段）；

> 注：in:在这个集合中；notin：不在这个集合中；exists：要么全在（exists）这个集合中，要么都不在（notexists）；

使用标签选择器的操作逻辑：

- 在使用基于集合的标签选择器同时指定多个选择器之间的逻辑关系为“与”操作（比如：- {key: name,operator: In,values: [zhangsan,lisi]} ，那么只要拥有这两个值的资源，都会被选中）；
- 使用空值的标签选择器，意味着每个资源对象都被选中（如：标签选择器的键是“A”，两个资源对象同时拥有A这个键，但是值不一样，这种情况下，如果使用空值的标签选择器，那么将同时选中这两个资源对象）
- 空的标签选择器（注意不是上面说的空值，而是空的，都没有定义键的名称），将无法选择出任何资源；

在基于集合的选择器中，使用“In”或者“Notin”操作时，其values可以为空，但是如果为空，这个标签选择器，就没有任何意义了。

两种标签选择器类型（基于等值、基于集合的书写方法）：

```text
selector:
  matchLabels:           #基于等值
    app: nginx
  matchExpressions:         #基于集合
    - {key: name,operator: In,values: [zhangsan,lisi]}     #key、operator、values这三个字段是固定的
    - {key: age,operator: Exists,values:}   #如果指定为exists，那么values的值一定要为空
```



# Docker

## 概述

Linux 命名空间、控制组和 UnionFS 三大技术支撑了目前 Docker 的实现，也是 Docker 能够出现的最重要原因。

![在这里插入图片描述](https://img-blog.csdnimg.cn/53de044ef67d4b1e9592a065645f778a.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p625p6E5biILeWwvOaBqQ==,size_20,color_FFFFFF,t_70,g_se,x_16)

- namespace，命名空间

命名空间，容器隔离的基础，保证A容器看不到B容器.
6个命名空间：User，Mnt，Network，UTS，IPC，Pid

- cgroups，Cgroups 是 Control Group 的缩写，控制组

cgroups 容器资源统计和隔离

主要用到的cgroups子系统：cpu，blkio，device，freezer，memory

实际上 Docker 是使用了很多 Linux 的隔离功能，让容器看起来像一个轻量级虚拟机在独立运行，容器的本质是被限制了的 Namespaces，cgroup，具有逻辑上独立文件系统，网络的一个进程。

- unionfs 联合文件系统

例如aufs/overlayfs，是分层镜像实现的基础。

UnionFS 其实是一种为 Linux 操作系统设计的用于把多个文件系统『联合』到同一个挂载点的文件系统服务。

## Network

### **四类网络模式**

| Docker网络模式 | 配置                      | 说明                                                         |
| -------------- | ------------------------- | ------------------------------------------------------------ |
| host模式       | –net=host                 | 容器和宿主机共享Network namespace。                          |
| container模式  | –net=container:NAME_or_ID | 容器和另外一个容器共享Network namespace。 kubernetes中的pod就是多个容器共享一个Network namespace。 |
| none模式       | –net=none                 | 容器有独立的Network namespace，但并没有对其进行任何网络设置，如分配veth pair 和网桥连接，配置IP等。 |
| bridge模式     | –net=bridge               | （默认为该模式）                                             |

### **host模式**

如果启动容器的时候使用host模式，那么这个容器将不会获得一个独立的Network Namespace，而是和宿主机共用一个Network Namespace。容器将不会虚拟出自己的网卡，配置自己的IP等，而是使用宿主机的IP和端口。但是，容器的其他方面，如文件系统、进程列表等还是和宿主机隔离的。

使用host模式的容器可以直接使用宿主机的IP地址与外界通信，容器内部的服务端口也可以使用宿主机的端口，不需要进行NAT，host最大的优势就是网络性能比较好，但是docker host上已经使用的端口就不能再用了，网络的隔离性不好。



### **container模式**

这个模式指定新创建的容器和已经存在的一个容器共享一个 Network Namespace，而不是和宿主机共享。新创建的容器不会创建自己的网卡，配置自己的 IP，而是和一个指定的容器共享 IP、端口范围等。同样，两个容器除了网络方面，其他的如文件系统、进程列表等还是隔离的。两个容器的进程可以通过 lo 网卡设备通信。



### **none模式**

使用none模式，Docker容器拥有自己的Network Namespace，但是，并不为Docker容器进行任何网络配置。也就是说，这个Docker容器没有网卡、IP、路由等信息。需要我们自己为Docker容器添加网卡、配置IP等。



### **bridge模式**

当Docker进程启动时，会在主机上创建一个名为docker0的虚拟网桥，此主机上启动的Docker容器会连接到这个虚拟网桥上。虚拟网桥的工作方式和物理交换机类似，这样主机上的所有容器就通过交换机连在了一个二层网络中。

从docker0子网中分配一个IP给容器使用，并设置docker0的IP地址为容器的默认网关。在主机上创建一对虚拟网卡veth pair设备，Docker将veth pair设备的一端放在新创建的容器中，并命名为eth0（容器的网卡），另一端放在主机中，以vethxxx这样类似的名字命名，并将这个网络设备加入到docker0网桥中。可以通过brctl show命令查看。