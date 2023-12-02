import pandas as pd
import re
import os
from urllib.parse import urlparse
from collections import Counter
from specifications import *

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
raw_data_path = os.path.join(base_dir, 'data', 'raw')
processed_data_path = os.path.join(base_dir, 'data', 'processed')

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

# Aggreate daily data for one entry into a dict
def daily_data_to_row(date, total_visits, most_visited_url,
                most_visited_count, broad_percentages, narrow_percentages):
    row = {'date': date,
           'total_visits': total_visits,
           'most_visited_url': most_visited_url,
           'most_visited_count': most_visited_count}
    
    for key, value in broad_percentages.items():
        row[key] = round(value, 4)
    
    for key, value in narrow_percentages.items():
        row[key] = round(value, 4)

    return row

# Extract the domain from a URL
def extract_domain(url):
    domain = urlparse(url).netloc

    # Removing the 'www.' if it exists in the domain
    if domain.startswith('www.'):
        domain = domain[4:]

    # Handle the google country-specified domains to generic one
    if re.match(r'google\.[a-z\.]+', domain):
        domain = 'google.com'

    return domain

# Categorization of domains
def broad_categorization(domain):
    if domain in broad_educational_domains or domain in broad_productivity_domains:
        return 'study(%)'
    elif domain in broad_entertainment_domains:
        return 'entertainment(%)'
    else:
        return 'other_broad(%)'

def narrow_categorization(domain):
    if domain in narrow_coding_domains:
        return 'coding(%)'
    elif domain in narrow_streaming_domains:
        return 'streaming(%)'    
    elif domain in narrow_medical_domains:
        return 'medical(%)'
    elif domain in narrow_financial_domains:
        return 'financial(%)'
    elif domain in narrow_educational_domains:
        return 'educational(%)'
    elif domain in narrow_gaming_domains:
        return 'gaming(%)'
    elif domain in narrow_social_media_domains:
        return 'social_media(%)'
    elif domain in narrow_news_media_domains:
        return 'news_media(%)'
    else:
        return 'other_narrow(%)'

# reload: The page was reloaded. This might not necessarily indicate a new visit but rather a refresh of the current page. It's typically not counted as a new visit in terms of analytics.
# link: You navigated to the page by clicking on a link. This is a standard navigation method and usually counts as a new visit.
# auto_bookmark: The page was accessed through a bookmark. Depending on the browser's definition, this may or may not count as a new visit.
# typed: You typed the URL directly into the browser's address bar. This is often considered a strong indicator of intent and is usually counted as a new visit.
# generated: The page was visited through some other unspecified mechanism. This could be from an application or any other non-standard method of accessing the webpage.
# auto_toplevel: This might indicate the first page visit in a new browser window or tab, or a homepage visit.
# form_submit: You navigated to this page by submitting a form, which could be a search form or any other kind of user input form.

# TODO:
# take into account of other transitions] develop an algorithm to rank websites based on intention, passive, active, intentional

# take into the account of what time and what type of domain were visited

def main():

    summary_df = pd.DataFrame(columns=summary_columns)
    daily_df = pd.DataFrame(columns=daily_columns)
    ranking_df = pd.DataFrame(columns=ranking_columns)

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
    
    # print(df)

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
        ranking_df = ranking_df.append(row, ignore_index=True)
    
    # ==================================
    # ||            DAILY             ||
    # ==================================

    grouped_df = df.groupby('date')
    for daily_date, daily_data in grouped_df:
        # `daily_date` is the current date of the group
        # `daily_data` is a DataFrame with data for that date

        daily_total_visits = daily_data.shape[0]
        daily_domain_visit_counts = Counter(daily_data['domain'])
        daily_most_visited_url = daily_domain_visit_counts.most_common(1)[0][0]
        daily_most_visited_count = daily_domain_visit_counts[daily_most_visited_url]

        daily_broad_percentages = daily_data['broad_category'].value_counts(normalize=True) 
        daily_narrow_percentages = daily_data['narrow_category'].value_counts(normalize=True) 

        daily_entry = daily_data_to_row(daily_date, daily_total_visits, daily_most_visited_url,
                                 daily_most_visited_count, daily_broad_percentages,
                                 daily_narrow_percentages)

        # Ensure daily_entry has all the columns with default values
        daily_entry = {col: daily_entry.get(col, daily_default[col]) for col in daily_columns}


        daily_df = daily_df.append(daily_entry, ignore_index=True)

        daily_domain_visited_rank = daily_domain_visit_counts.most_common()
        # Append entries: One entry per domain
        for domain, counts in daily_domain_visited_rank:
            row = {'date': daily_date, 'domain': domain, 'counts': counts}
            ranking_df = ranking_df.append(row, ignore_index=True)

    summary_df.to_csv(processed_data_path + '/' + 'summary_df.csv')
    daily_df.to_csv(processed_data_path + '/' + 'daily_df.csv')
    ranking_df.to_csv(processed_data_path + '/' + 'ranking_df.csv')





main()