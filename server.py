import tornado.httpserver
import tornado.ioloop
from tornadows import soaphandler
from tornadows import webservices
from tornadows import xmltypes
from tornadows.soaphandler import webservice
from sql_db import cl_mySQL_DB



class RegisterUser(soaphandler.SoapHandler):
    
        @webservice(_params=[str],_returns=str)
        def add(self, userName):
                xObject = cl_mySQL_DB()
                userKey = xObject.createUser(userName)
                return 'Hello %s , save your key : %s' %(userName , userKey)


class FetchTickers(soaphandler.SoapHandler):
    
        @webservice(_params=[str,str,str,str],_returns=str)
        def getData(self, ticker, field, source, userKey):

                if userKey is None:
                        userKey = "0"            

                xObject = cl_mySQL_DB()
                dict_table = xObject.getTicker(ticker, field, source, userKey)
                xObject.closeConnection()

                #print dict_table
                return dict_table  

            

if __name__ == '__main__':
       service = [('RegisterUser',RegisterUser),('FetchTickers',FetchTickers)]
       ws = webservices.WebService(service)
       application = tornado.httpserver.HTTPServer(ws)
       application.listen(4545)
       tornado.ioloop.IOLoop.instance().start()
