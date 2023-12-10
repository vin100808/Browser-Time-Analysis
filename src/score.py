import pandas as pd
import re
import os
import numpy as np
from urllib.parse import urlparse
from collections import Counter
# from specs import *
from definition import *

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
raw_data_path = os.path.join(base_dir, 'data', 'raw')
processed_data_path = os.path.join(base_dir, 'data', 'processed')

# Aggregate data into dict
def score_data_to_row(domain, total_visits, transition_count, score):
    row = {
        'domain': domain,
        'total_visits': total_visits,
        'score': score
    }

    for key, value in transition_count.items():
        row[key] = value

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

def calculate_domain_score(transition_count, number_of_visits, max_visits):
    # Define relative weights for transition types
    weights = {
        'typed': 0.8,
        'auto_bookmark': 0.8,
        'form_submit': 0.4,
        'link': 0.6,
        'reload': 0.6,
        'auto_toplevel': 0.3,
        'generated': 0.3
    }
    
    # Calculate the weighted interaction score
    weighted_interaction_score = sum(transition_count.get(t, 0) * w for t, w in weights.items())
    
    # Normalize the weighted interaction score by the total possible score for this domain
    max_possible_score_for_domain = number_of_visits * max(weights.values())
    normalized_intent_score = weighted_interaction_score / max_possible_score_for_domain * 100
    
    return round(normalized_intent_score, 2)

# Example usage:
# score = calculate_domain_score(typed=50, auto_bookmark=25, form_submit=10, link=50, auto_toplevel=5, generated=10)
# print(score)  # This will give you a score out of 100, factoring in total visits

def scoring_analysis(df):

    summary_score_df = pd.DataFrame(columns=scoring_columns)

    grouped_df = df.groupby('domain')
    domain_visit_counts = Counter(df['domain'])
    most_visited_url = domain_visit_counts.most_common(1)[0][0]
    most_visited_count = domain_visit_counts[most_visited_url]

    for domain, domain_data in grouped_df:

        total_visits = domain_data.shape[0]

        transition_count = {
            'typed': 0,
            'auto_bookmark': 0,
            'form_submit': 0,
            'link': 0,
            'reload': 0,
            'auto_toplevel': 0,
            'generated': 0}
    
        transition_count.update(Counter(domain_data['transition']))
        domain_score = calculate_domain_score(transition_count, total_visits, most_visited_count)
        score_entry = score_data_to_row(domain, total_visits, transition_count, domain_score)

        score_entry = {col: score_entry.get(col, scoring_default[col]) for col in scoring_columns}
        summary_score_df = summary_score_df.append(score_entry, ignore_index=True)

    return summary_score_df

