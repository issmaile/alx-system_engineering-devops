# kill a proc named killmenow

exec { 'pkill killmenow' :
	path => '/bin/'
	command => 'pkill killmenow',
	}
