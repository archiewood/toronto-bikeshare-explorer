import requests
import datetime as dt
import pandas as pd
import sqlalchemy
import json

station_status_url = 'https://toronto-us.publicbikesystem.net/customer/ube/gbfs/v1/en/station_status'
# url2='https://toronto-us.publicbikesystem.net/customer/ube/gbfs/v1/en/system_information'
# url3='https://toronto-us.publicbikesystem.net/customer/ube/gbfs/v1/en/system_pricing_plans'
# station_info_url='https://toronto-us.publicbikesystem.net/customer/ube/gbfs/v1/en/station_information'

status_info_packed = pd.read_json(station_status_url)
status_info_df = pd.DataFrame(status_info_packed.data.values.tolist()[0])
status_info_df['timestamp'] = dt.datetime.now()
status_info_df['num_bikes_available_types'] = status_info_df['num_bikes_available_types'].apply(
    json.dumps)


uri='postgresql://mdwrjwzjwstaye:cc37772581c95d3bebd4ec3430966160b15d172fd110b59abc6feb8a4ae65e30@ec2-107-22-83-3.compute-1.amazonaws.com:5432/dejif9jh7jj58m'

engine=sqlalchemy.create_engine(uri)

status_info_df.to_sql('station_status_log',engine,if_exists='append')