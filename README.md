
1)	Register you api at Cisco’s developer portal using the below link

https://apiconsole.cisco.com/apps/myapps

 

2)	Now click on register an new app and select the following options and PSRIT in the API section

 



3)	You will now be able to see the API key under your My Apps & Keys

 



4)	Now we will use curl command below to get the access token that will be required to query our records against the csa’s that we have
curl -s -k -H "Content-Type: application/x-www-form-urlencoded" -X POST -d "client_id=53pjpfaaga8yq8s8rd3cm8xv" -d "client_secret=aHDXDF2UYd9TutVtpMjctuww" -d "grant_type=client_credentials" https://id.cisco.com/oauth2/default/v1/token

         




5)	This will give you the token required for quering to get the solutions from cisco

 



6)	Now the token that we obtained should be used in the python code in the github link 	
https://github.com/thanujyennaytelus/ciscovulnchecker

Note: you need to enable the legacy calls of the OpenSSL to get the queries back from cisco the advisoriy tested below is giving us the solution present is cisco website for “CVE-2018-0124”
 

7)	The script in git hub contains the code for giving the routes, firmware installed and to get the vulnerabilities that may be published by cisco.

Issues and improvements to be made:

1)	The number of calls allowed by cisco is limited

2)	For the router and firmware vuln checker the excel sheet needs to be in this format and it should be updated to query with cisco to email that there is a vulnerability in the infrastructure that we have

 
