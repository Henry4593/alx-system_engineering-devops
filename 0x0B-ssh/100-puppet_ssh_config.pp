# make changes to 'ssh_config' file using puppet codes
file{ '/etc/ssh/ssh_config':
    ensure => present,	
    content =>"
    	#SSH client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAunthentication no
	",
}
