Hadoop Cluster Role 
==================

Installs and configure Hadoop system (version 3.b.c) in a cluster of nodes.

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows:

	# The type of the node: slave or master or resourcemanager or nodemanager or datanode or namenode 
	hadoop_type_of_node: slave
	# Hadoop base directory to install the software
	hadoop_home: /opt/hadoop
	# List of servers to download the hadoop code
	hadoop_mirrors: [ 
		"http://apache.rediris.es/hadoop/common",
		"http://apache.panu.it/hadoop/common",
		"http://apache.lauf-forum.at/hadoop/common",
		"http://apache.mindstudios.com/hadoop/common",
		"http://www-eu.apache.org/dist/hadoop/common"
	]
	# Hadoop version to install
	hadoop_version: 3.1.0
	# A dictionary with a set of properties to set in the core-site.xml
	hdfs_props: {}
	# A dictionary with a set of properties to set in the yarn-site.xml
	yarn_props: {}

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
    - { role: 'indigo-dc.hadoop', hadoop_master: 'MASTER_NODE_NAME_OR_IP', hadoop_type_of_node: 'master'}
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

License
-------

Apache Licence v2 [1]

[1] http://www.apache.org/licenses/LICENSE-2.0

