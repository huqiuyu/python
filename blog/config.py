DIALECT = 'mysql'
DRIVER = 'pymysql'
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'db2'
USERNAME = 'root'
PASSWORD = '123456'
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
