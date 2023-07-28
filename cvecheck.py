import pandas as pd
import requests

API_KEY = "eyJraWQiOiJUV3lfd0piZUhMUjJrb1NZQWZpTnZPeGptWExPM3NKNTdBTUk0UGEySzRRIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULkp1RktKN2lFaGp3dHB6UnJXbkpkQ0gzMW1VWl9Fa1BIUGRrYVJYbmtoclUiLCJpc3MiOiJodHRwczovL2lkLmNpc2NvLmNvbS9vYXV0aDIvZGVmYXVsdCIsImF1ZCI6ImFwaTovL2RlZmF1bHQiLCJpYXQiOjE2OTA1ODM1NDIsImV4cCI6MTY5MDU4NzE0MiwiY2lkIjoiNTNwanBmYWFnYTh5cThzOHJkM2NtOHh2Iiwic2NwIjpbImN1c3RvbXNjb3BlIl0sImFjY2Vzc19sZXZlbCI6MSwic3ViIjoiNTNwanBmYWFnYTh5cThzOHJkM2NtOHh2IiwiZnVsbF9uYW1lIjoibnVsbCBudWxsIiwiYXpwIjoiNTNwanBmYWFnYTh5cThzOHJkM2NtOHh2In0.nG5FAADe7tl2Xxrc5ulYDdQ2RSyEj1YiN10A4UCx7jrxMLBMHdbRoUOQ1FH0-ktr85BOOsWGm58OKKzYAvJPxWig-Z2ezhOIdcAtwYoEsZTou8jwyBz_SxnoHpsb1Uvl0C3kn9sPBbkwC_uxIea383wzerNAS2OOVm4QREDnHFudoyBRotJ-NxxMkNM8nL-X23ILmkZTnDMI-rtx8VDi1vjigTW69aQ51DQzlgcWLEhlGH4DIU0CZVBEuDMJJdur5gNMsuhb5iAFNS2yN1d5_yFwu8UaOhZVoRoWUdatp8k1ULuSwWGv1gf2koHz5wUSUSozW-vvMXGws0xrR3n7bQ"
EXCEL_FILE = "vuln.xlsx"

# Load the Excel file
df = pd.read_excel(EXCEL_FILE)

# Create a new column for the solution
df['Solution'] = ""

# Iterate over the DataFrame
for index, row in df.iterrows():
    # Extract the CVE
    cve_id = row['CVE_ID']  # replace 'CVE_ID' with your actual column name
    
    # Make the API request
    response = requests.get(
        f'https://apix.cisco.com/security/advisories/cve/{cve_id}',
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
    )

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Extract the solution from the API response
        solution = data['advisory']['solution']
        
        # Write the solution to the 'Solution' column
        df.at[index, 'Solution'] = solution

# Write the DataFrame to a new Excel file
df.to_excel("output.xlsx", index=False)

