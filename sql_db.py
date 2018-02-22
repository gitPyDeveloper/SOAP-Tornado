
import MySQLdb
import logging, sys
import random
import datetime
import string
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


class cl_mySQL_DB():
    

    C_HOST_NAME = "localhost"
    C_USER_NAME = "root"
    C_USER_PASSWORD = ""
    C_DB_NAME = "CRT"    
    
    
    def __init__(self):
        
        self.con_db = MySQLdb.connect(cl_mySQL_DB.C_HOST_NAME,    
                                 cl_mySQL_DB.C_USER_NAME,         
                                 cl_mySQL_DB.C_USER_PASSWORD, 
                                 cl_mySQL_DB.C_DB_NAME)
                    
        if self.con_db:
            logging.debug('Successfully connected to : %s'  %cl_mySQL_DB.C_DB_NAME )
        else:
            logging.debug('Error in connecting to : %s'  %cl_mySQL_DB.C_DB_NAME )
            
            
    def id_generator(self,size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    
    def closeConnection(self):
        self.con_db.close()
    
    
    def createUser(self, in_userName):
        
        cur_db = self.con_db.cursor()
        _id = self.id_generator()
        dateTemp = str(datetime.datetime.today()).replace(':','')
        dateTemp = dateTemp.replace(" ","")
        dateTemp = dateTemp.replace(".","")
        strDate = dateTemp.replace('-','')
        
        userKey = _id + strDate
        
        sql_stmt = "call sp_create_user('" + in_userName + "','" + userKey + "');"
        cur_db.execute(sql_stmt)
        
        oldKey = None
        for row in cur_db.fetchall():
            oldKey = row[0]
            break
        
        if oldKey is None:
            self.con_db.commit()
        else:
            userKey = oldKey

        #print "USER " , userKey      
        return userKey
      
        
    
    def getTableData(self, in_table, in_list_field,in_where_condition):
            
        # you must create a Cursor object. It will let you execute all the queries you need
        cur_db = self.con_db.cursor()
        sql_stmt = "Select %s from %s where "  %in_list_field %in_table %in_where_condition

        cur_db.execute(sql_stmt)
        dict_data = {}

        # print all the first cell of all the rows
        counter = 0
        for row in cur_db.fetchall():
            #print row
            dict_data[counter] = row
            counter += 1
            
        return dict_data
    
    
    
    
    def getTicker(self,in_ticker,in_field,in_source,in_key):

        cur_db = self.con_db.cursor()
        sql_stmt = "call sp_get_ticker('" + in_ticker + "','" + in_field + "','" + in_source + "','" + in_key + "');"
        cur_db.execute(sql_stmt)
        
        dict_data = {}
        
        for row in cur_db.fetchall():
            if len(row) == 1:
                dict_data['X'] = row[0]
                break
            dict_data[row[0]] = row[1]
            
        return dict_data
                
    
    def updTicker(self,in_ticker,in_field,in_source,in_key,in_date,in_value,in_level = 1):
        
        cur_db = self.con_db.cursor()
        sql_stmt = "call sp_upd_ticker('" + in_ticker + "','" + in_field + "','" + in_source   
        sql_stmt = sql_stmt + "','" + in_key + "'," + str(in_level) + ", '" + in_date + "'," + str(in_value) + ");"
        
        print sql_stmt
        try:
            cur_db.execute(sql_stmt)
            self.con_db.commit()
        except:
            print 'No access to update data'




