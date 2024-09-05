from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'L3n0v0.13'
app.config['MYSQL_DATABASE_DB'] = 'crudb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

