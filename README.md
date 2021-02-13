# Login any WordPress site using Python
By login WordPress site using python you can scrape login protectecd data from WordPress website. Or, you can crack WordPress user using loop.

To login single user:
```
wordpress_login('https://wordpresssitelink.com', 'username_here', 'password_here') # don't include '/' after site url
```
To login multiple user:
```
any_veriable = {'user1':'password1', 'user2':'password2', 'user3':'password3', 'user4':'password4', 'userN':'passwordN'}
for u, p in any_veriable.items():
    wordpress_login('https://wordpresssitelink.com', u, p) # don't include '/' after site url
```
