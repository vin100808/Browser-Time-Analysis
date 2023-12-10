import pandas as pd
import re
import os
from urllib.parse import urlparse
from collections import Counter
from specs import *
from categorization import *
from summary import summary_analysis
from daily import daily_analysis
from score import scoring_analysis

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
raw_data_path = os.path.join(base_dir, 'data', 'raw')
processed_data_path = os.path.join(base_dir, 'data', 'processed')

def new():

    df = pd.read_csv(raw_data_path + '/' + 'history_month.csv')

    # ==================================
    # ||          PREPROCESS          ||
    # ==================================
    df = df[df['transition'] != 'reload'] # Remove reload transition visits as they are not important
    df['domain'] = df['url'].apply(extract_domain) # Add extracted domains for each visit
    df['broad_category'] = df['domain'].apply(broad_categorization) # Add broad categorization type based on domain
    df['narrow_category'] = df['domain'].apply(narrow_categorization) # Add narrow categorization type based on domain
    df['date'] = pd.to_datetime(df['date']).dt.date # Convert date to datetime.date type
    df['time'] = pd.to_datetime(df['time']).dt.time # Conver time to datetime.time type
    df = df[df['domain'] != 'bohpimdoclnmgldeegbpibkhmpkhblbf'] # Reduce fraudulent data
    df['time_category'] = df['time'].apply(time_categorization) # Morning, Afternoon, Evening, Before Dawn
    df['day_type'] = df['date'].apply(day_categorization) # Weekend, Weekday

    summary_df, summary_ranking_df, summary_time_df, summary_day_df = summary_analysis(df)

    daily_df, daily_ranking_df = daily_analysis(df)
    
    summary_score_df = scoring_analysis(df)

    summary_df.to_csv(processed_data_path + '/' + 'summary_df.csv')
    summary_ranking_df.to_csv(processed_data_path + '/' + 'summary_ranking_df.csv')
    summary_time_df.to_csv(processed_data_path + '/' + 'summary_time_df.csv')
    summary_day_df.to_csv(processed_data_path + '/' + 'summary_day_df.csv')

    daily_df.to_csv(processed_data_path + '/' + 'daily_df.csv')
    daily_ranking_df.to_csv(processed_data_path + '/' + 'daily_ranking_df.csv')

    summary_score_df.to_csv(processed_data_path + '/' + 'summary_score_df.csv')

new()