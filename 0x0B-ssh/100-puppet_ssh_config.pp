#!/usr/bin/env bash
# making changes to the configuration file using puppet

file { 'etc/ssh/ssh_cofig':
	ensure => present,

content =>"

	#SSH client configuration
	host*
	IdentifyFile ~/.ssh/school
	PasswordAuthentication no
