import requests

def wordpress_login(url, username, password):
	wp_login = url + '/wp-login.php'
	wp_admin = url + '/wp-admin/'
	uname = username
	upass = password

	s = requests.Session()
	header = {'Cookie':'wordpress_test_cookie=WP Cookie check'}
	data = {'log':uname, 'pwd':upass, 'wp-submit':'Log In', 'redirect_to':wp_admin, 'testcookie':'1'}
	res = s.post(wp_login, headers = header, data = data)
	html = res.text

	if 'The password you entered for the username' in html or 'Invalid username' in html:
		print(f"U: {uname}, P:{upass} - Login Failed.")
	else:
		print(f"U: {uname}, P:{upass} - Login Success.")
