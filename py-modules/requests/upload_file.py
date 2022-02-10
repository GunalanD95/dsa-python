import requests


def main():
    '''
    Upload a file using requests.post()
    '''

    url = 'https://httpbin.org/post'
    file = {'file': open(r'C:\Users\admin\Desktop\DSA-PYTHON\py-modules\requests\product.xlsx', 'rb')}
    r = requests.post(url, files=file)
    print(r.status_code)
    print(r.text)




if __name__ == '__main__':
    main()