import sys
from flask import Flask
from flask import request
from flaskext.mysql import MySQL
app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='jack@123'
app.config['MYSQL_DATABASE_DB']='SHIVI_DATABASE'
mysql = MySQL()
mysql.init_app(app)
@app.route("/users",methods=['GET','POST','PUT','DELETE'])

def hello():
    if request.method=='POST':
        cursor = mysql.get_db().cursor()
        db = mysql.get_db()
        data = request.json
        print data
        print type(data)
        user=data['user']
        f_name=data['user']['first_name']
        l_name=data['user']['last_name']
        email=data['user']['email']
        password=data['user']['password']
        iden=data['user']['identy']
	#print "insert into shivi_info values( {0},{1},{2},{3},{4})".format(f_name,l_name,email,password,iden)
        cursor.execute("insert into shivi_info values( '{0}','{1}','{2}','{3}','{4}')".format(f_name,l_name,email,password,iden))
        db.commit()
        #print request.path
        #print request.content_type
        #print type(request.get_data)
        #print request.data
        #print type(request.data)
        #print request.json
        #print type(request.json)
        return str(request.method)
   
    elif request.method=='GET':
       cursor=mysql.get_db().cursor()
       db=mysql.get_db()
       data = request.json
       print data
       print type(data)
       try:
                        # Execute the SQL command
          cursor.execute("select * from shivi_info")

               # Fetch all the rows in a list of lists.
          results = cursor.fetchall()
          for row in results:
             f_name = row[0]
             l_name = row[1]
             email = row[2]
             password= row[3]
             identy= row[4]
                        # Now print fetched result
             print "f_name=%s,l_name=%s,email=%s,password=%d,identy=%d" % (f_name, l_name, email, password, identy)
       except:
         print "Error: unable to fetch data"
         print "Unexpected error:", sys.exc_info()
         db.close()
     
    elif request.method=='DELETE':
        cursor = mysql.get_db().cursor()
        db = mysql.get_db()
        data = request.json
        print data
        iden=data['user']['identy']
        print type(data)
        try:
           cursor.execute("delete from shivi_info where identy='{0}'".format(iden))
           db.commit()
           #s="bcdd"
           print s
           return
        except:
          db.rollback()
          db.close()
          return "unable to delete",500


    elif request.method=='PUT':
         cursor = mysql.get_db().cursor()
         db = mysql.get_db()
         data = request.json
         f_name=data['user']['first_name']
         iden=data['user']['identy']
         print data
         print type(data)
         try:
            cursor.execute("update shivi_info set first_name='{1}' where identy='{0}'".format(iden,f_name))
            db.commit()
            return "abc"
         except:
           db.rollback()
           db.close()
           return "failed",500

if __name__ == "__main__":
    app.run(debug=True)

