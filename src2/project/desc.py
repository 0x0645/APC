import json , psycopg2 , time , requests

url = "https://www.jumia.com.eg/smartphones/?page="

page = 1
a = True
while a:
      def connn():
                conn = psycopg2.connect(database="APC", user = "postgres", password = "dana20499", host = "127.0.0.1", port = "5432")
                cur = conn.cursor()
                return(conn , cur) 

      payload={}
      headers = {
              'authority': 'www.jumia.com.eg',
              'pragma': 'no-cache',
              'cache-control': 'no-cache',
              'accept': 'application/json',
              'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
              'referer': 'https://www.jumia.com.eg/smartphones/',
              'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            }
            response = requests.request("GET", url+str(page), headers=headers).json()
            x = response.get("viewData")
            y = x.get("products")

            def des():
                  conn,cur=connn() 
                  url = "https://www.jumia.com.eg/smartphones/?page="
                  response1 = requests.request("GET", url, headers=headers, data=payload)
                  if(response1.status_code==429):
                    print('error 429')
                    time.sleep(20)
                    a=des()
                  else:
                    response1=response1.json()
                    a=response1['x']['y']['head']['property']
                    m=0
                    for name  in a:   
                      print(name[m]['name'],name[m]['value'])
                      m+=1
                  return(a)

            des()
