import pandas as pd

query_list = ['Malattia psichiatrica', 'Ansia', 'Fatica', 'Disordine dell\'sonno', 'Disturbi dell\'umore',
              'Perdita di memoria', 'Mal di testa', 'Disturbo', 'attenzione', 'Perdita di capelli', 'Dispnea',
              'Disfunzione cognitiva', 'Stanchezza dopo sforzo', 'sintomi', 'sonno', 'cognitiva', 'Disfunzione',
              'umore']


def main():
    for i in range(0, len(data)):
        print(i)

        all_text = data['tweet'][i]
        # keyword_list = ['motorcycle', 'bike', 'cycle', 'dirtbike', "long","sintomi"]

        # all_text = 'some rather long string'
        if set(query_list).intersection(all_text.split()):
            print("Found One")
            data.at[i, 'related'] = 1
        else:
            data.at[i, 'related'] = 0
if __name__ == "__main__":
    data = pd.read_csv('omdena_class/LongCovidItaliaPage_account_Scraped_LongCovid.csv')
    data['related'] = ''
    main()
    data.to_csv('e:/related/related_07_2022_Scraped_LongCovid.csv')
