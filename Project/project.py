#our data is from https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2010000301

import pandas as pd

url = 'https://raw.githubusercontent.com/darrenpierre90/NLP-STATDEV/master/Testfile/processed_input_2010000301.csv'
df = pd.read_csv(url,error_bad_lines=False,sep='""',engine='python')
print(df)






