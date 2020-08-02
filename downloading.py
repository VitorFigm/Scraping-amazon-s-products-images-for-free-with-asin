from urllib import request
#url to query with .format
url = "https://ws-eu.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=GB&ASIN={}&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=SL250"



p_asin = 'B00004CXX9'
with open(f'imgs/{p_asin}.jpg','wb') as file:
    req_file = url.format(p_asin)   ##url of the request
    file.write(  request.urlopen(req_file).read()     )    ##save = the request in file 
    size = file.tell()   #get file size
    
    if(size!=0):    ##if size is zero,  
        print(f'name:{p_asin}.jpg   size:{ round(size/1024,2) }KiB  downloaded')
    else: print('error in '+p_asin)
