Hadoop Cluster Role 
==================

Installs and configure Hadoop system (version 2.x.y or 3.x.y) in a cluster of nodes.

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows:

> #### Required variables
> ### hadoop_master
> 
> ### The type of the node: master / worker
> hadoop_node_type: worker
> ### Roles: master -> [namenode, resourcemanager] and worker -> [datanode, nodemanager]
> hadoop_node_role: all
> ### Hadoop base directory to install the software
> hadoop_home: /opt/hadoop
> ### List of servers to download the hadoop code
> hadoop_mirrors: [ 
>   "http://apache.rediris.es/hadoop/common",  
>   "http://apache.lauf-forum.at/hadoop/common",  
>   "http://www-eu.apache.org/dist/hadoop/common"  
> ]
> ### Hadoop version to install
> hadoop_version: 3.2.0
> hadoop_2: false
> ### A dictionary with a set of properties to set in the hdfs-site.xml
> hdfs_props: {
>   'dfs.replication': 1  
> }
> ### A dictionary with a set of properties to set in the yarn-site.xml
> yarn_props: {
>   'yarn.acl.enable': 0,  
>   'yarn.nodemanager.aux-services': "mapreduce_shuffle",  
>   'yarn.nodemanager.resource.memory-mb': 1536,  
>   'yarn.scheduler.maximum-allocation-mb': 1536,  
>   'yarn.scheduler.minimum-allocation-mb': 128,  
>   'yarn.nodemanager.vmem-check-enabled': false  
> }
> ### A dictionary with a set of properties to set in the mapred-site.xml
> mapred_props: {
>   'yarn.app.mapreduce.am.resource.mb': 512,  
>   'mapreduce.map.memory.mb': 256,  
>   'mapreduce.reduce.memory.mb': 256  
> }
> 
> hdfs_port: 9000
> ### A dictionary with a set of properties to set in the core-site.xml
> core_props: {
>   'hadoop.proxyuser.root.hosts': "*",  
>   'hadoop.proxyuser.root.groups': "*"  
> }
> 
> master_key: false
> ### Private and public key of master node
> master_pub_key: ""
> master_priv_key: ""
> worker_ips: [ 'localhost' ]
> 
> yarn: false
> yarn_mapred_port: 54311
> 
> httpfs: false
> httpfs_user: null
> httpfs_password: null

Example Playbook
----------------

This an example of how to install the Cluster:

In the "Worker Nodes"
```yml
  roles:
    - { role: 'indigo-dc.hadoop', hadoop_master: 'MASTER_NODE_NAME_OR_IP' }
```

In the "Manager Node"
```yml
  roles:
    - { role: 'indigo-dc.hadoop', hadoop_master: 'MASTER_NODE_NAME_OR_IP', hadoop_node_type: 'master'}
```

HADOOP ports
------------

From hadoop 3.0.0 ports are changed for several services: [bug-tracker](https://issues.apache.org/jira/browse/HDFS-9427)
This is the new configuration:

- Namenode ports:

  |  OLD | NEW  |
  |:----:|:----:|
  | 50470|9871  |
  | 50070|9870  |
  |  8020|9820  |

- Secondary NN ports:

  |  OLD | NEW  |
  |:----:|:----:|
  | 50091|9869  |
  | 50090|9868  |

- Datanode ports:

  |  OLD | NEW  |
  |:----:|:----:|
  | 50020|9867  |
  | 50010|9866  |
  | 50475|9865  |
  | 50075|9864  |

> Note: if you use the older version you have no differences

Use HTTPFS
----------

Example:

```bash
# Create the file
curl -u httpfs_user:httpfs_password -k -i -X PUT "https://master_ip:14000/webhdfs/v1/test.txt?op=CREATE&user.name=root&noredirect=true&overwrite=true"
# Upload the file
curl -u httpfs_user:httpfs_password -k -i -X PUT -H "content-type: application/octet-stream" -T /path/to/my/original/file/test.txt  "https://master_ip:14000/webhdfs/v1/test.txt?op=CREATE&data=true&user.name=root&noredirect=true&overwrite=true&data=true"
# Get the file
curl -u httpfs_user:httpfs_password -k -i -L -X GET "https://master_ip:14000/webhdfs/v1/test.txt?op=OPEN&user.name=root&noredirect=true"
```

> Note: httpfs server is used with nginx as proxy with a certificate and user and password.

License
-------

Apache Licence v2 [1]

[1] http://www.apache.org/licenses/LICENSE-2.0

