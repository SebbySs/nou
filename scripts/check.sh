#!/bin/bash

pack="httpd"

if rpm -q $pack
	then
		echo "package is installed"
	else 
		echo "please install httpd package"
fi
