import requests

def options(website):
    r = requests.options("https://"+website)
    try:
        if r.status_code == requests.codes.ok:
            print(f"Staus code: {r.status_code}")
            print(f"Allowed Headers: {r.headers['Allow']}")
        else:
            print(f"Status code not 200 OK: {r.status_code}")
    except KeyError:
        print("No 'Allow' headers.")

    try:
        print(f"Allowed Headers: {r.headers['allow']}")
    except:
        print("No 'allow' headers.")


if __name__ == "__main__":
    starturl = input("Enter URL: ")
    print("-"*(len(starturl) + 11))
    options(starturl)