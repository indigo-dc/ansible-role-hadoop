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


License
-------

Apache Licence v2 [1]

[1] http://www.apache.org/licenses/LICENSE-2.0

