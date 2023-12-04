from datetime import time

morning_start = time(5, 0)
noon_start = time(12, 0)
evening_start = time(17, 0)  # Assuming evening starts at 5 PM
before_dawn_end = time(5, 0)  # Assuming before dawn ends at 5 AM
before_midnight = time(23, 59, 59)

time_analysis_columns = [
    'time_category', 
    'total_visits', 
    'most_visited_url', 
    'most_visited_count', 
    'study(%)', # Broad
    'entertainment(%)',            # Broad
    'other_broad(%)',              # Broad
    'coding(%)',                   # Narrow
    'streaming(%)',                # Narrow
    'medical(%)',                  # Narrow
    'financial(%)',                # Narrow
    'educational(%)',              # Narrow
    'gaming(%)',                   # Narrow
    'social_media(%)',             # Narrow
    'news_media(%)',               # Narrow
    'other_narrow(%)'
]

time_analysis_default = {
    'time_category': 'N/A', 
    'total_visits': 0, 
    'most_visited_url': 'N/A', 
    'most_visited_count': 0, 
    'study(%)': 0, # Broad
    'entertainment(%)': 0,            # Broad
    'other_broad(%)': 0,              # Broad
    'coding(%)': 0,                   # Narrow
    'streaming(%)': 0,                # Narrow
    'medical(%)': 0,                  # Narrow
    'financial(%)': 0,                # Narrow
    'educational(%)': 0,              # Narrow
    'gaming(%)': 0,                   # Narrow
    'social_media(%)': 0,             # Narrow
    'news_media(%)': 0,               # Narrow
    'other_narrow(%)': 0
}

daily_columns = [
    'date', 
    'total_visits', 
    'most_visited_url', 
    'most_visited_count', 
    'study(%)', # Broad
    'entertainment(%)',            # Broad
    'other_broad(%)',              # Broad
    'coding(%)',                   # Narrow
    'streaming(%)',                # Narrow
    'medical(%)',                  # Narrow
    'financial(%)',                # Narrow
    'educational(%)',              # Narrow
    'gaming(%)',                   # Narrow
    'social_media(%)',             # Narrow
    'news_media(%)',               # Narrow
    'other_narrow(%)'              # Narrow
]

daily_default = {
    'date': 'N/A', 
    'total_visits': -1, 
    'most_visited_url': 'N/A', 
    'most_visited_count': -1, 
    'study(%)': 0, # Broad
    'entertainment(%)': 0,            # Broad
    'other_broad(%)': 0,              # Broad
    'coding(%)': 0,                   # Narrow
    'streaming(%)': 0,                # Narrow
    'medical(%)': 0,                  # Narrow
    'financial(%)': 0,                # Narrow
    'educational(%)': 0,              # Narrow
    'gaming(%)': 0,                   # Narrow
    'social_media(%)': 0,             # Narrow
    'news_media(%)': 0,               # Narrow
    'other_narrow(%)': 0              # Narrow
    }

summary_columns = [
    'start_date',
    'end_date', 
    'total_visits', 
    'most_visited_url', 
    'most_visited_count', 
    'study(%)', # Broad
    'entertainment(%)',            # Broad
    'other_broad(%)',              # Broad
    'coding(%)',                   # Narrow
    'streaming(%)',                # Narrow
    'medical(%)',                  # Narrow
    'financial(%)',                # Narrow
    'educational(%)',              # Narrow
    'gaming(%)',                   # Narrow
    'social_media(%)',             # Narrow
    'news_media(%)',               # Narrow
    'other_narrow(%)'              # Narrow
]

summary_default = {
    'start_date': 'N/A', 
    'end_date': 'N/A',
    'total_visits': -1, 
    'most_visited_url': 'N/A', 
    'most_visited_count': -1, 
    'study(%)': 0, # Broad
    'entertainment(%)': 0,            # Broad
    'other_broad(%)': 0,              # Broad
    'coding(%)': 0,                   # Narrow
    'streaming(%)': 0,                # Narrow
    'medical(%)': 0,                  # Narrow
    'financial(%)': 0,                # Narrow
    'educational(%)': 0,              # Narrow
    'gaming(%)': 0,                   # Narrow
    'social_media(%)': 0,             # Narrow
    'news_media(%)': 0,               # Narrow
    'other_narrow(%)': 0              # Narrow
    }

ranking_columns = [
    'date',
    'domain',
    'counts'
]

# ==================================
# ||        BROAD DOMAINS         ||
# ==================================
# Broad categories are more general and encompass a wider range of websites.

# Entertainment related domains (Broad)
broad_entertainment_domains = [
    'youtube.com', 'netflix.com', 'spotify.com', 'hulu.com', 
    'twitch.tv', 'vimeo.com', 'disneyplus.com', 'soundcloud.com', 
    'pandora.com', 'instagram.com'
]

# Educational related domains (Broad)
broad_educational_domains = [
    'coursera.org', 'edx.org', 'khanacademy.org', 'udemy.com',
    'academia.edu', 'researchgate.net', 'chat.openai.com'
]

# Productivity related domains (Broad)
broad_productivity_domains = [
    'github.com', 'stackoverflow.com', 'gitlab.com', 'bitbucket.org', 
    'sourceforge.net', 'dev.to', 'codepen.io', 'hackerrank.com', 
    'leetcode.com', 'freecodecamp.org'
]

# ... Other broad domain categories ...

# ==================================
# ||        NARROW DOMAINS        ||
# ==================================
# Narrow categories are more specific and targeted to particular subjects or interests.

narrow_coding_domains = [
    'github.com', 'stackoverflow.com', 'gitlab.com', 'bitbucket.org', 
    'sourceforge.net', 'dev.to', 'codepen.io', 'hackerrank.com', 
    'leetcode.com', 'freecodecamp.org'
]

narrow_streaming_domains = [
    'netflix.com', 'hulu.com', 'disneyplus.com', 'crunchyroll.com'
]

narrow_medical_domains = [
    'webmd.com', 'mayoclinic.org', 'healthline.com', 'medscape.com',
    'nih.gov', 'who.int', 'clevelandclinic.org', 'hopkinsmedicine.org'
]

narrow_financial_domains = [
    'bloomberg.com', 'investopedia.com', 'marketwatch.com', 'seekingalpha.com',
    'ft.com', 'wsj.com', 'cnbc.com', 'morningstar.com'
]

narrow_educational_domains = [
    'coursera.org', 'edx.org', 'khanacademy.org', 'udemy.com',
    'academia.edu', 'researchgate.net', 'brainly.com', 'lynda.com', 'chat.openai.com'
]

narrow_gaming_domains = [
    'ign.com', 'gamefaqs.com', 'pcgamer.com', 'gamespot.com',
    'polygon.com', 'twitch.tv', 'steampowered.com', 'giantbomb.com'
]

narrow_social_media_domains = [
    'facebook.com', 'twitter.com', 'instagram.com', 'linkedin.com',
    'pinterest.com', 'snapchat.com', 'tumblr.com', 'reddit.com'
]

narrow_news_media_domains = [
    'nytimes.com', 'theguardian.com', 'bbc.co.uk', 'cnn.com',
    'aljazeera.com', 'foxnews.com', 'nbcnews.com', 'reuters.com'
]




