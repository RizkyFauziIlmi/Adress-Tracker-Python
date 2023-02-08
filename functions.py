from requests import get
from os import name, system
from tabulate import tabulate

def clear(): 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def print_menu():
    clear()
    print(f'-----ADDRESS TRACKER-----\n[1] - Your Address\n[2] - Exit')

def ask():
    print("Enter your Command: ")
    command = input()
    return command

def print_location(ip, network, version, city, region, region_code, country, country_name, country_code, country_code_iso3, country_capital, country_tld, continent_code, in_eu, postal, latitude, longitude, currency_name, languages, country_area, country_population, asn, org):
    data = [
    ['IP', ip],
    ['Network', network],
    ['Version', version],
    ['City', city],
    ['region', region],
    ['Region Code', region_code],
    ['Country', country],
    ['Country Name', country_name],
    ['Country Code', country_code],
    ['Country Code Iso3', country_code_iso3],
    ['Country Capital', country_capital],
    ['Country TLD', country_tld],
    ['Continent Code', continent_code],
    ['IN_EU', in_eu],
    ['Postal', postal],
    ['Latitude', latitude],
    ['Longitude', longitude],
    ['Currency Name', currency_name],
    ['Languages', languages],
    ['Country Area', country_area],
    ['Country Population', country_population],
    ['ASN', asn],
    ['ORG', org],
    ]
    clear()
    print (tabulate(data, headers=["Title", "Value"]))

def get_ip():
    print("Get current IP Address...")
    response = get("https://api64.ipify.org?format=json").json()
    print('Successful Get IP Address')
    return response['ip']

def get_location():
    ip_address = get_ip()
    print(f"Get {ip_address} Location...")
    response = get(f'https://ipapi.co/{ip_address}/json/').json()
    print_location(ip=response['ip'], network=response['network'], version=response['version'], city=response['city'], region=response['region'], asn=response['asn'], continent_code=response['continent_code'], country=response['country'], country_area=response['country_area'], country_capital=response['country_capital'], country_code=response['country_code'], country_code_iso3=response['country_code_iso3'], country_name=response['country_name'], country_population=response['country_population'], country_tld=response['country_tld'], currency_name=response['currency_name'], in_eu=response['in_eu'], languages=response['languages'], latitude=response['latitude'], longitude=response['longitude'], org=response['org'], postal=response['postal'], region_code=response['region_code'])

def askClosed():
    close = False 
    print("Do you want to exit [y/n]?")
    answer = input()

    while (answer.lower() != 'y' or answer.lower() != 'n'):
        if answer.lower() == 'y':
            clear()
            close = True
            return close
        elif answer.lower() == 'n':
            return close
        else:
            clear()
            print("Invalid Input!")
            print("Do you want to exit [y/n]?")
            answer = input()