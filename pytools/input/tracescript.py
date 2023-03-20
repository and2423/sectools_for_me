import requests

# TRACE check with the script input
# Have to test in burp to see if I'm getting
# the right thing back. Work in progress.

def trace_input(URL, schema):
    page = "/<script>alert('TRACE')</script>"
    r = requests.request("TRACE", schema+URL+page)
    print(f"Method: {r.request.method}")
    print(f"Headers: {r.request.headers}")
    print()
    print(len(schema+URL+page))
    print()
    print(f"Status: {r.status_code}")
    print(f"Headers: {r.headers}")
    print(f"Body: {r.content}")



if __name__ == "__main__":
    URL = input("Enter start URL: ")
    schema = input("Please pick 1: 'https://' -or- 2: 'https://': ")
    while(schema != (1 or 2)):
        if schema == '1':
            schema = 'http://'
            break
        elif schema == '2':
            schema = 'https://'
            break
        else:
            print("Please pick again.")
        schema = input("Please pick 1: 'https://' -or- 2: 'https://': ")

    trace_input(URL, schema)