import re
from urllib.parse import urlparse
from specs import *

# Day Categorization sort
def day_categorization(given_date):
    # Check if the date is a weekend
    if given_date.weekday() >= 5:  # 5 for Saturday, 6 for Sunday
        return 'Weekend'
    else:
        return 'Weekday'

# Determine timeframe for time
def time_categorization(time):
    if morning_start <= time < noon_start:
        return 'Morning'
    elif noon_start <= time < evening_start:
        return 'Afternoon'
    elif evening_start <= time < before_midnight:
        return 'Evening'
    else:
        return 'Before Dawn'

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