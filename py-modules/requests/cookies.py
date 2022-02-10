import requests

def main():


    url = 'https://httpbin.org/cookies'
    cookies = {'profile': 'software engineer'}
    r = requests.get(url, cookies=cookies)
    print(r.text)

if __name__ == '__main__':
    main()