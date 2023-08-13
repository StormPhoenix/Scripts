use mysql;
create user 'wordpress'@'%' identified by 'your-password';
grant all privileges on wordpress_db.* to 'wordpress'@'%';
