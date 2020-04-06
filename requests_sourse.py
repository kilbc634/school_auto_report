# this file save the Curl requests
get_token = """
curl --request POST \
  --url https://epidemicapi.ncut.edu.tw/api/login \
  --header 'content-type: application/json;charset=UTF-8' \
  --header 'origin: https://epidemic.ncut.edu.tw' \
  --header 'referer: https://epidemic.ncut.edu.tw/login' \
  --data '{
	"userId": "3A123456",
	"password": "abc123",
	"remember": false
}'
"""

get_departments = """
curl --request GET \
  --url https://epidemicapi.ncut.edu.tw/api/departments \
  --header 'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoi546L7pGG5a6HIiwidXNlcklkIjoiM0E1MTMxMDMiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiM0E1MTMxMDMiLCJyb2xlSWQiOiIyIiwiZW1haWwiOiJUVVlONzY4MDFAR01BSUwuQ09NIiwiaG9tZVBhZ2VJZCI6IjAxMDEiLCJkZXBhcnRtZW50TmFtZSI6Iumbu-WtkOezuyIsImRlcGFydG1lbnRJZCI6IjE0IiwidHlwZSI6IjEiLCJjbGFzc05hbWUiOiLlm5vlrZDlm5vkuZkiLCJleHAiOjE1ODc1MTg3MDcsImlzcyI6ImFwaXRlbXBsYXRlLm5jdXQuZWR1LnR3IiwiYXVkIjoiYXBpdGVtcGxhdGUifQ.CX7dh-WthsyKwMJUKEZ1HduBB7aAoAxvV3kfa_nVoJM' \
  --header 'origin: https://epidemic.ncut.edu.tw' \
  --header 'referer: https://epidemic.ncut.edu.tw/bodyTemp'
"""

get_config = """
curl --request GET \
  --url https://epidemicapi.ncut.edu.tw/api/config \
  --header 'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoi546L7pGG5a6HIiwidXNlcklkIjoiM0E1MTMxMDMiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiM0E1MTMxMDMiLCJyb2xlSWQiOiIyIiwiZW1haWwiOiJUVVlONzY4MDFAR01BSUwuQ09NIiwiaG9tZVBhZ2VJZCI6IjAxMDEiLCJkZXBhcnRtZW50TmFtZSI6Iumbu-WtkOezuyIsImRlcGFydG1lbnRJZCI6IjE0IiwidHlwZSI6IjEiLCJjbGFzc05hbWUiOiLlm5vlrZDlm5vkuZkiLCJleHAiOjE1ODc1MTg3MDcsImlzcyI6ImFwaXRlbXBsYXRlLm5jdXQuZWR1LnR3IiwiYXVkIjoiYXBpdGVtcGxhdGUifQ.CX7dh-WthsyKwMJUKEZ1HduBB7aAoAxvV3kfa_nVoJM' \
  --header 'origin: https://epidemic.ncut.edu.tw' \
  --header 'referer: https://epidemic.ncut.edu.tw/bodyTemp'
"""

get_activityData = """
curl --request GET \
  --url https://epidemicapi.ncut.edu.tw/api/activityData \
  --header 'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoi546L7pGG5a6HIiwidXNlcklkIjoiM0E1MTMxMDMiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiM0E1MTMxMDMiLCJyb2xlSWQiOiIyIiwiZW1haWwiOiJUVVlONzY4MDFAR01BSUwuQ09NIiwiaG9tZVBhZ2VJZCI6IjAxMDEiLCJkZXBhcnRtZW50TmFtZSI6Iumbu-WtkOezuyIsImRlcGFydG1lbnRJZCI6IjE0IiwidHlwZSI6IjEiLCJjbGFzc05hbWUiOiLlm5vlrZDlm5vkuZkiLCJleHAiOjE1ODc1MTg3MDcsImlzcyI6ImFwaXRlbXBsYXRlLm5jdXQuZWR1LnR3IiwiYXVkIjoiYXBpdGVtcGxhdGUifQ.CX7dh-WthsyKwMJUKEZ1HduBB7aAoAxvV3kfa_nVoJM' \
  --header 'origin: https://epidemic.ncut.edu.tw' \
  --header 'referer: https://epidemic.ncut.edu.tw/bodyTemp'
"""

get_temperatureSurveys = """
curl --request GET \
  --url https://epidemicapi.ncut.edu.tw/api/temperatureSurveys/3A513103-2020-03-01 \
  --header 'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoi546L7pGG5a6HIiwidXNlcklkIjoiM0E1MTMxMDMiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiM0E1MTMxMDMiLCJyb2xlSWQiOiIyIiwiZW1haWwiOiJUVVlONzY4MDFAR01BSUwuQ09NIiwiaG9tZVBhZ2VJZCI6IjAxMDEiLCJkZXBhcnRtZW50TmFtZSI6Iumbu-WtkOezuyIsImRlcGFydG1lbnRJZCI6IjE0IiwidHlwZSI6IjEiLCJjbGFzc05hbWUiOiLlm5vlrZDlm5vkuZkiLCJleHAiOjE1ODc1MTg3MDcsImlzcyI6ImFwaXRlbXBsYXRlLm5jdXQuZWR1LnR3IiwiYXVkIjoiYXBpdGVtcGxhdGUifQ.CX7dh-WthsyKwMJUKEZ1HduBB7aAoAxvV3kfa_nVoJM' \
  --header 'origin: https://epidemic.ncut.edu.tw' \
  --header 'referer: https://epidemic.ncut.edu.tw/bodyTemp'
"""

post_data = """
curl --request POST \
  --url https://epidemicapi.ncut.edu.tw/api/temperatureSurveys \
  --header 'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoi546L7pGG5a6HIiwidXNlcklkIjoiM0E1MTMxMDMiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiM0E1MTMxMDMiLCJyb2xlSWQiOiIyIiwiZW1haWwiOiJUVVlONzY4MDFAR01BSUwuQ09NIiwiaG9tZVBhZ2VJZCI6IjAxMDEiLCJkZXBhcnRtZW50TmFtZSI6Iumbu-WtkOezuyIsImRlcGFydG1lbnRJZCI6IjE0IiwidHlwZSI6IjEiLCJjbGFzc05hbWUiOiLlm5vlrZDlm5vkuZkiLCJleHAiOjE1ODc1MTg3MDcsImlzcyI6ImFwaXRlbXBsYXRlLm5jdXQuZWR1LnR3IiwiYXVkIjoiYXBpdGVtcGxhdGUifQ.CX7dh-WthsyKwMJUKEZ1HduBB7aAoAxvV3kfa_nVoJM' \
  --header 'content-type: application/json;charset=UTF-8' \
  --header 'origin: https://epidemic.ncut.edu.tw' \
  --header 'referer: https://epidemic.ncut.edu.tw/bodyTemp' \
  --data '{
	"id": "3A123456-undefined",
	"saveDate": "2020-03-01",
	"morningTemp": 34,
	"noonTemp": 37.5,
	"nightTemp": 34,
	"isValid": false,
	"morningManner": 0,
	"noonManner": 0,
	"nightManner": 0,
	"isMorningFever": null,
	"isNoonFever": false,
	"isNightFever": null,
	"morningActivity": "工作(At work)",
	"noonActivity": "工作(At work)",
	"nightActivity": "家中(Home)",
	"measureTime": "01:11",
	"userId": "3A123456",
	"departmentId": "14",
	"className": "四X四X",
	"departmentName": "OO系",
	"type": "1"
}'
"""
