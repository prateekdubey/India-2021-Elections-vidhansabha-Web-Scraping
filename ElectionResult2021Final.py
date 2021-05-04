from bs4 import BeautifulSoup
import requests
import re
import time
import csv


print("Welcome to general election to vidhan sabha 2021 \n")
print("  Assam \n  Kerala \n  Puducherry \n  Tamil Nadu \n  West Bengal")
state=input("Enter the Name of state correctly for which you want result")
print("\n 1. Partywise result 2. Constituency wise result \n")
result_mode=input("Enter 1 or 2 ")

if (result_mode == '1'):
    start_url='https://results.eci.gov.in/Result2021/partywiseresult-S03.htm'
    source=requests.get(start_url)
    html =source.text
    soup=BeautifulSoup(html,'html.parser')

    state_code={}
    state_option = soup.findAll('table',width="100%")[3].findAll('tbody')[1].findAll('tr')[1].find('select').findAll('option')

    for x in state_option:
        state_code[x.text]=(x['value'])
        
    for x in state_code:
        if(x == state):
            state_codechar=state_code[state]
    partywise_url = 'https://results.eci.gov.in/Result2021/partywiseresult-'+state_codechar+'.htm?st='+state_codechar
    partywise_webscrap=requests.get(partywise_url)
    html = partywise_webscrap.text
    partywise_soup=BeautifulSoup(html,'html.parser')
    party_name=[]
    party_win=[]
    state_option = partywise_soup.findAll('table',width="100%")[3].findAll('div',id="div1")[0].findAll('tbody')[0].findAll('td')[0].text
    print(state_option.strip().replace(" ",""))
    state_option = partywise_soup.findAll('table',width="100%")[3].findAll('div',id="div1")[0].findAll('tbody')[0].findAll('tr')
    usable_data = state_option[3:(len(state_option)-1)]
    for i in usable_data:
        partywise_seats=[]
        partywise_info=i.findAll('td')
        for x in partywise_info:
            partywise_seats.append(x.string)
        party_name.append(str(partywise_seats[0]))
        party_win.append(int(partywise_seats[1]))

    for i in range(len(party_name)):
        print(party_name[i],party_win[i])

    print("\n Want a csv document of it?")
    choose=input("type yes or no")
    if(choose.lower()=="yes"):
        with open(state+''+str(time.time()), 'w', newline='') as general_file:
            writer=csv.writer(general_file)
            writer.writerow(['party','Seats_Won'])
            for i in range(len(party_name)):
                 writer.writerow([party_name[i], party_win[i]])
    else :
        print("\n Thank you")

else:
    constiuency_number=[]
    constiuency_name =[]
    Leading_candidate =[]
    Trailing_candidate =[]
    Margins =[]
    leading_party =[]
    trailing_party =[]
    start_url='https://results.eci.gov.in/Result2021/partywiseresult-S03.htm'
    source=requests.get(start_url)
    html =source.text
    soup1=BeautifulSoup(html,'html.parser')

    state_code={}
    state_option = soup1.findAll('table',width="100%")[3].findAll('tbody')[1].findAll('tr')[1].find('select').findAll('option')

    for x in state_option:
        state_code[x.text]=(x['value'])
        
    for x in state_code:
        if(x == state):
            state_codechar=state_code[state]
    time.sleep(1)
    start_url='https://results.eci.gov.in/Result2021/statewise'+state_codechar+'1.htm'
    source=requests.get(start_url)
    html =source.text
    soup2=BeautifulSoup(html,'html.parser')
    page_number_list=[]
    pageno=soup2.findAll('table',width="100%")[4].findAll('tr')[4].findAll('a')[1:-1]
    for i in pageno:
        page_number_list.append(i.text)
    
    for i in range(0,(len(page_number_list))):
        statewise_url = 'https://results.eci.gov.in/Result2021/statewise'+state_codechar+page_number_list[i]+'.htm'
        #print(statewise_url)
        #statewise_url = 'https://results.eci.gov.in/Result2021/statewiseU073.htm'
        source=requests.get(statewise_url)
        html =source.text
        soup3=BeautifulSoup(html,'html.parser')
        #print(soup3)
        seat=soup3.findAll('table',width="100%")[4].findAll('tr')
        cal=seat[5:(len(seat)-1)]
        j=0
        for x in cal:
            
            if(j==0 or j==9 or j==18 or j==27 or j==36 or j==45 or j==54 or j==63 or j==72 or j==81):
                a=x.findAll('td')
                margin=[]
                for k in a:
                    margin.append(k.text)
                constiuency_name.append(margin[0])
                constiuency_number.append(margin[1])
                Leading_candidate.append(margin[2])
                leading_party.append(margin[4])
                Trailing_candidate.append(margin[15])
                trailing_party.append(margin[17])
                Margins.append(margin[28])
                j=j+1
            else:
                j=j+1
        time.sleep(1)
        #print("value of i = ",i)
    #print(constiuency_name,constiuency_number,Leading_candidate,leading_party,Trailing_candidate,trailing_party,Margins)
       
    print("\n Want a csv document of it?")
    choose=input("type yes or no")
    if(choose.lower()=="yes"):
        with open(state+'ConstituencyWiseResult'+str(time.time()), 'w', newline='') as general_file:
            writer=csv.writer(general_file)
            writer.writerow(['Constituency_Name','Constituency_Number','Leading_Candidate_Name','Leading_Party','Trailing_Candidate_Name','Trailing_Party','Margin'])
            for i in range(len(constiuency_name)):
                 writer.writerow([constiuency_name[i],constiuency_number[i],Leading_candidate[i],leading_party[i],Trailing_candidate[i],trailing_party[i],Margins[i]])
    else :
        print("\n Thank you")
   
