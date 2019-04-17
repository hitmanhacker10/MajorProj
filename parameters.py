import final


# search query to be executed
user= final.query
user = user + " AND "
loc=final.loca
print(user)
print(loc)
url="site:linkedin.com/in/ " 
search_query = url + user + loc

# file were scraped profile information will be stored
file_name = 'linkedin/results_file.csv'

# login credentials
linkedin_username = 'hitmanhacker01@gmail.com'
linkedin_password = 'hit10ha01'
