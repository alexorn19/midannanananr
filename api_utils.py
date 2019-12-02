import requests

api_url = "http://apis.is/petrol"
try:
    default = requests.get(api_url)
except Exception as e:
    default = {}


def raw_data(url=api_url):
    try:
        response = requests.get(url)
    except Exception as e:
        response = {}
    data = response.json()
    return data


def timestamps():
    ks = ['timestampApis', 'timestampPriceChanges', 'timestampPriceCheck']
    d = raw_data()
    return {k: d[k] for k in ks}


def results():
    d = raw_data()
    return d["results"]


def companieset():
    l = results()
    f = [g['company'] for g in l]
    return list(set(f))


def compinfo(comp):
    l = results()
    res = [d for d in l if d['company'] == comp]
    return res


def lowestprices():
    l = results()
    dres = [d['diesel'] for d in l]
    pres = [d['bensin95'] for d in l]
    pricks = {'min_diesel': min(dres), 'min_bensin95': min(pres)}
    lvendors = {'min_diesel_vendor': d['company']
                for d in l if d['diesel'] == pricks['min_diesel']}
    pvendors = {'min_bensin95_vendor': d['company']
                for d in l if d['diesel'] == pricks['min_bensin95']}
    out = {}
    out.update(pricks)
    out.update(lvendors)
    out.update(pvendors)
    return out


def stationinfo(stat):
    l = results()
    res = [d for d in l if d['key'] == stat]
    return res
