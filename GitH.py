def Get_Info_GitHub(n):
    def Find_Files(urls):
        links = urls
        import requests
        from bs4 import BeautifulSoup
        HEADERS = {
            'user-agent': '', # Set here ur own 'user-agent'
            'accept': '' # Set here ur 'accept' from network
        }
        # Tags = []; Pk = []
        Tagz = []; Pz = []
        for url in links:
            print('---------------------------------------\nRepository: ' + url)
            Tags = []; Pk = []
            html = requests.get(url, headers=HEADERS).text
            soup = BeautifulSoup(html, 'html.parser')
            f = soup.find_all(class_='js-navigation-open Link--primary')
            for i in f:
                if '.' in i.text:
                    Pk.append(' '.join((i.text).split()))
                    if (i.text)[((i.text).index('.') + 1)::] not in Tags:
                        Tags.append((i.text)[((i.text).index('.') + 1)::])
                    Pz.append(' '.join((i.text).split()))
                    if ((i.text)[((i.text).index('.') + 1)::]) not in Tagz:
                        Tagz.append((i.text)[((i.text).index('.') + 1)::])
                else:
                    links.append('https://github.com' + i.get('href'))
            for x in Tags:
                print(x + ':')
                for x1 in Pk:
                    if x in x1[-4::]:
                        print(x1)
                print('')
        print('=====================================================\nCounter_of_Each/Percentage\n')
        for z in Tagz:
            c = 0
            for z1 in Pz:
                if z in z1[-4::]:
                    c += 1
            print('---    ----      ----\n' + z + ':    ', c, '      ' + str(int(round(c/len(Pz), 2)*100)) + '%')
    import requests
    from bs4 import BeautifulSoup
    HEADERS = {
        'user-agent': '', # Set here ur own 'user-agent'
        'accept': '' # Set here ur 'accept' from network
    }
    URL = 'https://github.com/' + str(n) + '/'
    html = requests.get(URL + '?tab=repositories', headers=HEADERS).text
    if str((requests.get(URL, headers=HEADERS).status_code)) != '200':
        print('Invalid Profile name')
    elif requests.get(URL, headers=HEADERS).status_code > 500:
        print('Web Service is down')
    else:
        soup = BeautifulSoup(html, 'html.parser')
        Repos_n = soup.find_all(class_='wb-break-all'); urlz = []
        for i in Repos_n:
            urlz.append(URL + '\n'.join((i.text).split()))
        Find_Files(urlz)
Get_Info_GitHub('') #write any nickname of the github user here
