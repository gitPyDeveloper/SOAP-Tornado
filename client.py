import suds
import zeep



url = 'http://localhost:4545/RegisterUser?wsdl'
client = zeep.Client(wsdl=url)
#print client.wsdl.dump()


# To get key
client = suds.client.Client(url,cache=None)
print client.service.add('Harry')


url = 'http://localhost:4545/FetchTickers?wsdl'
client = zeep.Client(wsdl=url)
#print client.wsdl.dump()



key = 'USE_KEY'
ticker = 'C_USA_CHN'
field = 'EXPORT'
source = 'USDA'
print client.service.getData(ticker, field, source, key)




