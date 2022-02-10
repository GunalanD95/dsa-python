import requests

def main():


    url = 'https://api.github.com/events'
    get = requests.get(url)
    print(get.status_code)
    json_content = get.json()
    print(json_content[0] ['id']) #print the first element of the list and filter the id


    data = {
        'FirstName': 'Gunalan',
        'LastName': 'Deivaganapathy',
    }
    url2 = 'https://httpbin.org/post'
    post = requests.post(url2, data=data)
    print(post.status_code)
    json_data = post.json()
    print(json_data['form']['FirstName'])




if __name__ == '__main__':
    main()