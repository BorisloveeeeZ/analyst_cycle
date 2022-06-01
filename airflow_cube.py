from datetime import datetime, timedelta
import pandas as pd
from io import StringIO
import requests
from airflow.decorators import dag, task
from airflow.operators.python import get_current_context

def ch_get_df(query, host = 'https://clickhouse.lab.karpov.courses', user = 'student', password = 'dpo_python_2020'):
    '''connection to db'''
    r = requests.post(host, data = query.encode('utf-8'), auth=(user, password), verify = False)
    result = pd.read_csv(StringIO(r.text), sep='\t')
    return result


default_args = {
    'owner':'b.zubanov',
    'depends_on_past' : False,
    'retries' : 2,
    'retry_delay' : timedelta(minutes = 5),
    'start_date' : datetime(2022,3,10),

}

schedule_interval = '0 23 * * *'

@dag
def default_dag(schedule_interval = schedule_interval, default_args = default_args, catchup = False):
    @task
    def extract(): 
        '''query task'''
        query = '''SELECT
            toDate(time) as event_date,
            country,
            source,
            count() as likes
            FROM simulator_20220320.feed_actions
            where
                toDate(time) = '2022-03-26'
                and action = 'like'
            group by
                event_date,
                country,
                source

                '''
        df_cube = ch_get_df(query=query)
        return df_cube    

    df_cube = extract()

dag_example = default_dag    