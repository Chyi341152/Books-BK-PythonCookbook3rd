# mymodule.py

def urlprint(protocol, host, domain):
    url = '{}://{}.{}'.format(protocol, host, domain)
    # built-in print function, by defualt,sends output to sys.stdout
    print(url)
