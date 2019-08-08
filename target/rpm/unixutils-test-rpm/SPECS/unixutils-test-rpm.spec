Name: unixutils-test-rpm
Version: 1.0.0
Release: 1.0.0
Summary: unixutils-test-rpm
License: 2019, UnixUtils
Group: Development/Tools
autoprov: yes
autoreq: yes
BuildRoot: /sebi69/target/rpm/unixutils-test-rpm/buildroot

%description

%files

%attr(644,root,root) /tmp/rpm/

%pre
#!/bin/bash

pack="httpd"

if rpm -q $pack
	then
		echo "package is installed"
	else 
		echo "please install httpd package"
fi

%post
#!/bin/bash

cp /tmp/rpm/index.html /var/www/html

curl -s http://192.168.33.17/index.html | grep "small">> /dev/null 

if [ $? -eq 0 ] ; then
    echo "Success"
else
    echo "Fail"
fi
