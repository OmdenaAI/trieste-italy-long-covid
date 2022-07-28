import pandas as pd
query_list = ['Malattia psichiatrica','Ansia','Fatica','Disordine dell\'sonno','Disturbi dell\'umore','Perdita di memoria', 'Mal di testa', 'Disturbo','attenzione', 'Perdita di capelli', 'Dispnea','Disfunzione cognitiva' , 'Stanchezza dopo sforzo' ]
#query_list = ['Ansia']
#related = []
#data = pd.read_csv('01_2022_Scraped_LongCovid.csv')
def searching(i,s):
        for q in query_list:


            if q in s :
                 data.at[i,'relate'] = 1
            else:
                 data.at[i,'relate'] = 0

def main():

    df_dict = data.to_dict(orient='records')
    i = 0

    for row in df_dict:
        print(i)
        i = i + 1
        s = row['tweet']
        s = str(s)
        print(type(s))
        try:
            s = row['tweet']
            # print(id)
            searching(i,s)
        except:
            print('error')
if __name__ == "__main__":
    related = []
    data = pd.read_csv('omdena_class/01_2022_Scraped_LongCovid.csv')
    data['relate']=''
    main()
    print(data)
    data.to_csv('e:/test33.csv')


s = "That I ever did see Anisa Dusty as the handle on the door"
s = s.split()
print(s)

for q in query_list:
    print(q)
    #q = str(q)

    for x in s :
        print(x)
        if x == q:
            print('found')



s = "That I ever did see Anisa Dusty as the handle on the door"
q = query_list[1]
print(q)

index = s.find('Anisa')
print(index)

import pandas as pd

query_list = ['Malattia psichiatrica', 'Ansia', 'Fatica', 'Disordine dell\'sonno', 'Disturbi dell\'umore',
              'Perdita di memoria', 'Mal di testa', 'Disturbo', 'attenzione', 'Perdita di capelli', 'Dispnea',
              'Disfunzione cognitiva', 'Stanchezza dopo sforzo', 'sintomi', 'sonno', 'cognitiva', 'Disfunzione',
              'umore']

data = pd.read_csv('omdena_class/01_2022_Scraped_LongCovid.csv')
data['related'] = ''
for i in range(0,len(data)):

    all_text = data['tweet'][i]
    #keyword_list = ['motorcycle', 'bike', 'cycle', 'dirtbike', "long","sintomi"]

    #all_text = 'some rather long string'
    if set(query_list).intersection(all_text.split()):
           print ("Found One")
           data.at[i,'related'] = 1
    else:
        data.at[i,'related'] = 0