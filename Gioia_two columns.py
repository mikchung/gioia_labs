import pandas as pd

def gioia_(folder_dir,delimiter_):

    print('Analysing file '+folder_dir)

    data = pd.read_csv(''+''+folder_dir+''+'',''+delimiter_+'')

    #creating primary key, replace the headers where necessary
    data['pk_']=data['url_domain']+','+data['app']

    #creating list of headers
    header_columns = []

    for i in data.columns:
        header_columns.append(i)

    #printing list of headers
    print(header_columns)

    #insert state of the art AI
    header_column = input('\n'+
    'Mr Gioia, it is me, Sooyoung, but you can call me Soogioia, which of the columns do you want to analyse: ')

    #create dataframe from pandaseries unique_occurences
    unique_occurences = data[header_column].value_counts()[:20].rename_axis('unique count').reset_index(name='pk')

    #split the primary key to tidy up the columns
    unique_occurences[['url_domain','app']] = unique_occurences['unique count'].str.split(',',expand = True)

    #print only the necessary columns.
    print(unique_occurences[['url_domain','app','pk']].to_string())

gioia_('c:/Users/mchung/Documents/Gioia/20211920 - Past7days_URLsforGoogle.txt',',')
