"""USOS2google configuration. If in trouble, see README"""

# USOS necessary configuration - you need to fill it
usosapi_base_url = 'http://usosapps.uw.edu.pl/' # url to usos api, default UW
consumer_key = ''
consumer_secret = ''

# USOS optional configuration
access_token_key = ''
access_token_secret = ''

# Timezone configuration
import pytz
mytz = pytz.timezone('Europe/Warsaw')

# You may use this dict to provide nicer names for courses, for -s option.
names_dict = {
# "1000-111bAM1b" : "Analiza I.1 (p II)",
# "1000-211bPM" : "Podst. Mat",
# "1000-211bWPF" : "WPF",
}

# These courses won't be copied.
ignore_list = [
# "1000-214bWWW",
]
