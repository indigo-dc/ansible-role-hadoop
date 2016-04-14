Hadoop Cluster Role 
==================

Installs and configure Hadoop system (version 2.X) in a cluster of nodes.

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows:

	# The type of the node: slave or master
	hadoop_type_of_node: slave
	# Hadoop base directory to install the software
	hadoop_home: /opt/hadoop-2.X
	# List of servers to download the hadoop code
	hadoop_mirrors: [ "ftp://mirror.cc.columbia.edu/pub/software/apache/hadoop/core/stable2/", 
			"ftp://apache.cs.utah.edu/apache.org/hadoop/core/stable2/",
			"ftp://apache.mirrors.tds.net/pub/apache.org/hadoop/core/stable2/",
			"ftp://ftp.osuosl.org/pub/apache/hadoop/core/stable2/" ]
	# Hadoop version to install
	hadoop_version: 2.7.2
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

