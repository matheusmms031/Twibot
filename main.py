import json
import requests
import os
from requests_oauthlib import OAuth1
# consumer_key = chave de acesso para a api
# consumer_ky_secret = chave secreta de acesso da api
# token_key = chave de acesso do usuario
# token_secret = chave secreta de acesso do usuario
consumer_key = ''
consumer_key_secret = ''
token_key = ''
token_secret = ''
auth = OAuth1(consumer_key, consumer_key_secret,token_key,token_secret,)
# URLS PARA ESPECIFICAR OQUE QUER FAZER
url_base = 'https://api.twitter.com/1.1/'

urls = {"1.1":{"user":{"followers_list":"followers/list.json","followers_ids":"followers/ids.json","friends_ids":"friends/ids.json","friends_list":"friends/list.json",'lookup':'users/lookup.json'},"direct":{'direct_mensages_list':'direct_messages/events/list.json'}}}


headers = {'authorization':'Bearer '}
parameters = {}

exit = 0
def get_response_user(url): #Retorna a mensagem do servidor com a autenticação de usuario
  return requests.get(url, auth=auth, params=parameters)
def get_response_bearer(url): #Retorna a mensagem do servidor com a autenticação de APP
  return requests.get(url, headers=headers, params=parameters)

def direct_mensages():
  count = int(input("Quantity of mensages: "))
  parameters['count'] = count
  url = url_base + urls['1.1']['direct']['direct_mensages_list']
  response = get_response_user(url)
  print(response.text)
  exit = input("APERTE ENTER PARA SAIR")
  direct_main()

def direct_banner():
  print("""
  ██████╗ ██╗██████╗ ███████╗ ██████╗████████╗███████╗    ███╗   ███╗███████╗███╗   ██╗███████╗ █████╗  ██████╗ ███████╗███████╗
  ██╔══██╗██║██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔════╝    ████╗ ████║██╔════╝████╗  ██║██╔════╝██╔══██╗██╔════╝ ██╔════╝██╔════╝
  ██║  ██║██║██████╔╝█████╗  ██║        ██║   ███████╗    ██╔████╔██║█████╗  ██╔██╗ ██║███████╗███████║██║  ███╗█████╗  ███████╗
  ██║  ██║██║██╔══██╗██╔══╝  ██║        ██║   ╚════██║    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║╚════██║██╔══██║██║   ██║██╔══╝  ╚════██║
  ██████╔╝██║██║  ██║███████╗╚██████╗   ██║   ███████║    ██║ ╚═╝ ██║███████╗██║ ╚████║███████║██║  ██║╚██████╔╝███████╗███████║
  ╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝   ╚═╝   ╚══════╝    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════
  """)
def direct_main():
  os.system("cls || clear")
  direct_banner()
  print("""
                  | 1 |          Back          | 1 | 
                  | 2 |  View Directs Mensages | 2 |
  """)
  command = int(input("[x]>"))
  if command == 1:
    principal()
  if command == 2:
    direct_mensages()



def query_banner():
  print("""
     ██████╗ ██████╗ ███╗   ██╗███████╗██╗   ██╗██╗  ████████╗███████╗
    ██╔════╝██╔═══██╗████╗  ██║██╔════╝██║   ██║██║  ╚══██╔══╝██╔════╝
    ██║     ██║   ██║██╔██╗ ██║███████╗██║   ██║██║     ██║   ███████╗
    ██║     ██║   ██║██║╚██╗██║╚════██║██║   ██║██║     ██║   ╚════██║
    ╚██████╗╚██████╔╝██║ ╚████║███████║╚██████╔╝███████╗██║   ███████║
    ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚══════╝╚═╝   ╚══════╝
 """)
def query_followers_id():
    screen_name = str(input("Input Username: "))
    quantity = str(input("How many followers(MAX 200): "))
    parameters['screen_name'] = screen_name
    parameters['count'] = quantity
    url = url_base + urls['1.1']['user']['followers_ids']
    response = get_response_bearer(url)
    response_dict = response.json()
    print(f"\n Firts {quantity} followers of {screen_name} \n")
    for c in range(1,len(response_dict['ids'])):
      print(f"| {c} | {response_dict['ids'][c]} ")
    exit = input("\n TECLE ENTER PARA SAIR")
    query_types()
def query_followers_list():
    screen_name = str(input("Input Username: "))
    quantity = str(input("How many followers(MAX 200): "))
    parameters['screen_name'] = screen_name
    parameters['count'] = quantity
    url = url_base + urls['1.1']['user']['followers_list']
    response = get_response_bearer(url)
    response_dict = response.json()
    print(f"\n Firts {quantity} followers of {screen_name} \n")
    for c in range(1,len(response_dict['users'])):
      print(f"| {c} | ID {response_dict['users'][c]['id']} | NAME {response_dict['users'][c]['name']} | USERNAME {response_dict['users'][c]['screen_name']} | FOLLOWERS {response_dict['users'][c]['followers_count']} | FOLLOWING {response_dict['users'][c]['friends_count']} ")
    exit = input("\n TECLE ENTER PARA SAIR")
    query_types()
def query_following_list():
    screen_name = str(input("Input Username: "))
    quantity = str(input("How many following(MAX 200): "))
    parameters['screen_name'] = screen_name
    parameters['count'] = quantity
    url = url_base + urls['1.1']['user']['friends_list']
    response = get_response_bearer(url)
    response_dict = response.json()
    print(f"\n Firts {quantity} following of {screen_name} \n")
    for c in range(1,len(response_dict['users'])):
      print(f"| {c} | ID {response_dict['users'][c]['id']} | NAME {response_dict['users'][c]['name']} | USERNAME {response_dict['users'][c]['screen_name']} | FOLLOWERS {response_dict['users'][c]['followers_count']} | FOLLOWING {response_dict['users'][c]['friends_count']} ")
    exit = input("\n TECLE ENTER PARA SAIR")
    query_types()
def query_following_id():
    screen_name = str(input("Input Username: "))
    quantity = str(input("How many following(MAX 200): "))
    parameters['screen_name'] = screen_name
    parameters['count'] = quantity
    url = url_base + urls['1.1']['user']['friends_ids']
    response = get_response_bearer(url)
    response_dict = response.json()
    print(f"\n Firts {quantity} following of {screen_name} \n")
    for c in range(1,len(response_dict['ids'])):
      print(f"| {c} | {response_dict['ids'][c]} ")
    exit = input("\n TECLE ENTER PARA SAIR")
    query_types()
def query_user_information():
    screen_name = str(input("Input Username: "))
    parameters['screen_name'] = screen_name
    url = url_base + urls['1.1']['user']['lookup']
    response = get_response_bearer(url)
    response_dict = response.json()
    print(f"\n Informations of {screen_name} \n")
    print(f"""
    NAME :      {response_dict[0]['name']}
    USERNAME:   {response_dict[0]['screen_name']}
    ID:         {response_dict[0]['id']}
    LOCATION:   {response_dict[0]['location']}
    FOLLOWERS:  {response_dict[0]['followers_count']}
    FOLLOWING:  {response_dict[0]['friends_count']}
    CREATED AT: {response_dict[0]['created_at']}
    TWEETS:     {response_dict[0]['statuses_count']}
    """)
    exit = input("\n TECLE ENTER PARA SAIR")
    query_types()
def query_types():# Função que é o menu dos tipos 
    while True:
        os.system("cls || clear")
        query_banner()
        print("""
                        | 1 |       Back        | 1 | 
                        | 2 |   Followers List  | 2 |
                        | 3 | Followers List Id | 3 |
                        | 4 |  User Information | 4 |
                        | 5 |   Following List  | 5 |
                        | 6 | Following List Id | 6 |         
        """)
        command = int(input("[x]>"))
        if command == 1:
          query_main()
        if command == 2:
          query_followers_list()
        if command == 3:
          query_followers_id()
        if command == 4:
          query_user_information()
        if command == 5:
          query_following_list()
        if command == 6:
          query_following_id()
        if command == 7:
          query_user_tweets()
def query_main(): # Função responsave pelo menu de consultas
  command = int()
  os.system("cls || clear")
  query_banner() 
  print("""
                  | 1 |       Back        | 1 | 
                  | 2 |   Types of query  | 2 |
  """)
  command = int(input("[x]>"))
  if command == 1: # Se digitar 1, voltar para o menu 
    principal()
  if command == 2: # Se digitar 2, abrir os tipos de buscas
    os.system("cls || clear")
    query_types() 
def principal(): # Função responsvel pelo menu
  while True:
    command = int()
    os.system('cls || clear')
    print("""
 ████████╗██╗    ██╗██╗██████╗  ██████╗ ████████╗
 ╚══██╔══╝██║    ██║██║██╔══██╗██╔═══██╗╚══██╔══╝
    ██║   ██║ █╗ ██║██║██████╔╝██║   ██║   ██║   
    ██║   ██║███╗██║██║██╔══██╗██║   ██║   ██║   
    ██║   ╚███╔███╔╝██║██████╔╝╚██████╔╝   ██║   
    ╚═╝    ╚══╝╚══╝ ╚═╝╚═════╝  ╚═════╝    ╚═╝  
    
    | 1 | Login                | 5 | Top #       
    | 2 | Direct Menssages    
    | 3 | Consults            
    | 4 | Tweets
    """)
    command = int(input("[x]>"))
    if command == 2:
      direct_main()
    if command == 3:
      query_main()


principal()
