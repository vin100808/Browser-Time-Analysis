import pandas as pd
import os
from collections import Counter
# from categorization import *
from definition import *

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
raw_data_path = os.path.join(base_dir, 'data', 'raw')
processed_data_path = os.path.join(base_dir, 'data', 'processed')

# ==================================
# ||            HELPER            ||
# ==================================
# Aggreate summary data for one entry into a dict
def summary_data_to_row(start_date, end_date, total_visits, most_visited_url,
                most_visited_count, broad_percentages, narrow_percentages):
    row = {'start_date': start_date,
           'end_date': end_date,
           'total_visits': total_visits,
           'most_visited_url': most_visited_url,
           'most_visited_count': most_visited_count}
    
    for key, value in broad_percentages.items():
        row[key] = round(value, 4)
    
    for key, value in narrow_percentages.items():
        row[key] = round(value, 4)

    return row

# Aggregate time analysis data for one entry into dict
def time_data_to_row(time_category, total_visits, most_visited_url,
                     most_visited_count, broad_percentages, narrow_percentages):
    row = {'time_category': time_category,
           'total_visits': total_visits,
           'most_visited_url': most_visited_url,
           'most_visited_count': most_visited_count}
    
    for key, value in broad_percentages.items():
        row[key] = round(value, 4)
    
    for key, value in narrow_percentages.items():
        row[key] = round(value, 4)

    return row

# Aggregate day analysis data for one entry into dict
def day_data_to_row(day_type, total_visits, most_visited_url,
                    most_visited_count, broad_percentages, narrow_percentages):
    row = {'day_type': day_type,
           'total_visits': total_visits,
           'most_visited_url': most_visited_url,
           'most_visited_count': most_visited_count}
    if day_type == 'Weekday':
        row['average_visits_per_day'] = total_visits/5
    else:
        row['average_visits_per_day'] = total_visits/2

    for key, value in broad_percentages.items():
        row[key] = round(value, 4)
    
    for key, value in narrow_percentages.items():
        row[key] = round(value, 4)

    return row

def summary_analysis(df):
    summary_df = pd.DataFrame(columns=summary_columns)
    summary_ranking_df = pd.DataFrame(columns=ranking_columns)
    summary_time_df = pd.DataFrame(columns=time_analysis_columns)
    summary_day_df = pd.DataFrame(columns=day_analysis_columns)

    # df = pd.read_csv(raw_data_path + '/' + 'history.csv')

    # # ==================================
    # # ||          PREPROCESS          ||
    # # ==================================
    # df = df[df['transition'] != 'reload'] # Remove reload transition visits as they are not important
    # df['domain'] = df['url'].apply(extract_domain) # Add extracted domains for each visit
    # df['broad_category'] = df['domain'].apply(broad_categorization) # Add broad categorization type based on domain
    # df['narrow_category'] = df['domain'].apply(narrow_categorization) # Add narrow categorization type based on domain
    # df['date'] = pd.to_datetime(df['date']).dt.date # Convert date to datetime.date type
    # df['time'] = pd.to_datetime(df['time']).dt.time # Conver time to datetime.time type
    # df = df[df['domain'] != 'bohpimdoclnmgldeegbpibkhmpkhblbf'] # Reduce fraudulent data
    # df['time_category'] = df['time'].apply(time_categorization) # Morning, Afternoon, Evening, Before Dawn
    # df['day_type'] = df['date'].apply(day_categorization) # Weekend, Weekday

    # ==================================
    # ||           ALL TIME           ||
    # ==================================
    start_date = df['date'].min()
    end_date = df['date'].max()
    total_visits = df.shape[0]
    domain_visit_counts = Counter(df['domain'])
    most_visited_url = domain_visit_counts.most_common(1)[0][0]
    most_visited_count = domain_visit_counts[most_visited_url]

    broad_percentages = df['broad_category'].value_counts(normalize=True)   
    narrow_percentages = df['narrow_category'].value_counts(normalize=True) 

    summary_entry = summary_data_to_row(start_date, end_date, total_visits, most_visited_url,
                                 most_visited_count, broad_percentages,
                                 narrow_percentages)
    
    # Ensure entry has all the columns with default values
    summary_entry = {col: summary_entry.get(col, summary_default[col]) for col in summary_columns}

    summary_df = summary_df.append(summary_entry, ignore_index=True)

    # Ranks of domain based on visit counts
    domain_visited_rank = domain_visit_counts.most_common()
    
    # Append entries: One entry per domain
    for domain, counts in domain_visited_rank:
        row = {'date': end_date, 'domain': domain, 'counts': counts}
        summary_ranking_df = summary_ranking_df.append(row, ignore_index=True)

    # ==================================
    # ||        Time Analysis         ||
    # ==================================
    grouped_df = df.groupby('time_category')
    for time_category, time_data in grouped_df:
        total_visits = time_data.shape[0]
        domain_visit_counts = Counter(time_data['domain'])

        most_visited_url = domain_visit_counts.most_common(1)[0][0]
        most_visited_count = domain_visit_counts[most_visited_url]

        broad_percentages = time_data['broad_category'].value_counts(normalize=True)   
        narrow_percentages = time_data['narrow_category'].value_counts(normalize=True) 

        time_entry = time_data_to_row(time_category, total_visits, most_visited_url,
                                    most_visited_count, broad_percentages,
                                    narrow_percentages)
        
        # Ensure entry has all the columns with default values
        time_entry = {col: time_entry.get(col, time_analysis_default[col]) for col in time_analysis_columns}

        summary_time_df = summary_time_df.append(time_entry, ignore_index=True)

    # ==================================
    # ||      Day Type Analysis       ||
    # ==================================
    grouped_df = df.groupby('day_type')
    for day_type, day_data in grouped_df:
        total_visits = day_data.shape[0]
        domain_visit_counts = Counter(day_data['domain'])

        most_visited_url = domain_visit_counts.most_common(1)[0][0]
        most_visited_count = domain_visit_counts[most_visited_url]

        broad_percentages = day_data['broad_category'].value_counts(normalize=True)   
        narrow_percentages = day_data['narrow_category'].value_counts(normalize=True) 

        day_entry = day_data_to_row(day_type, total_visits, most_visited_url,
                                    most_visited_count, broad_percentages,
                                    narrow_percentages)
        
        # Ensure entry has all the columns with default values
        day_entry = {col: day_entry.get(col, day_analysis_default[col]) for col in day_analysis_columns}

        summary_day_df = summary_day_df.append(day_entry, ignore_index=True)




    return summary_df, summary_ranking_df, summary_time_df, summary_day_df
