#https://github.com/itzmestar/duneanalytics
from duneanalytics import DuneAnalytics
import pandas as pd

# initialize client
dune = DuneAnalytics('sakamotoryuichi', '131199ht')

# try to login
dune.login()

# fetch tokens
dune.fetch_auth_token()

# fetch query result id using query id
# query id for any query can be found from the url of the query:
# for example: 
# https://dune.com/queries/4494/8769 => 4494x
# https://dune.com/queries/3705/7192 => 3705
# https://dune.com/queries/3751/7276 => 3751


for x in [
1000879,
1015242,
1015323,
1015353,
1023396,
1023403,
1023444,
1024421,
1106235,
1109644,
1023853,1125605,
1105405,1106018,1125609
]:

    result_id = dune.query_result_id(query_id=x)


    # fetch query result
    data = dune.query_result(result_id)
    
    res = data.get('data').get('get_result_by_result_id')

    # for record in res:
    #     print(record.get('data'))
    res = list(map(lambda item: item.get('data'), res))

    # print(res)
    
    
   
    df = pd.DataFrame.from_dict(res)
    path = r"{}_{}_dune.csv".format(df.iloc[0]['token_name'],df.iloc[0]['id'])
    df.to_csv(path, index=False)
    print(df.iloc[0]['token_name']) #check


