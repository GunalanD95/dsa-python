import requests

def main():


    headers = {'content-type': 'multipart/form-data'}
    url = 'https://httpbin.org/post'
    pos = requests.post(url, headers=headers) # customizing the headers using headers args
    print(pos.status_code)
    print(pos.text)


if __name__ == '__main__':
    main()