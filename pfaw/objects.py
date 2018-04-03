class Player(object):
    def __init__(self, response):
        self.name = response['displayName']
        self.id = response['id']

    def __str__(self):
        return f'Name: {self.name}\nID: {self.id}'


class BattleRoyale(object):
    def __init__(self, status, response, mode, platform):
        self.status = status
        self.score = 0
        self.matches = 0
        self.time = 0
        self.kills = 0
        self.wins = 0
        self.top3 = 0
        self.top5 = 0
        self.top6 = 0
        self.top10 = 0
        self.top12 = 0
        self.top25 = 0

        if mode == 'solo':
            mode = '_p2'
        elif mode == 'duo':
            mode = '_p10'
        elif mode == 'squad':
            mode = '_p9'
        elif mode == 'all':
            mode = '_p'

        for i in response:
            if mode and platform in i['name']:
                if 'score' in i['name']:
                    self.score += i['value']
                elif 'matchesplayed' in i['name']:
                    self.matches += i['value']
                elif 'minutesplayed' in i['name']:
                    self.time += i['value']
                elif 'kills' in i['name']:
                    self.kills += i['value']
                elif 'placetop1' in i['name']:
                    self.wins += i['value']
                elif 'placetop3' in i['name']:
                    self.top3 += i['value']
                elif 'placetop5' in i['name']:
                    self.top5 += i['value']
                elif 'placetop6' in i['name']:
                    self.top6 += i['value']
                elif 'placetop10' in i['name']:
                    self.top10 += i['value']
                elif 'placetop12' in i['name']:
                    self.top12 += i['value']
                elif 'placetop25' in i['name']:
                    self.top25 += i['value']
    def __str__(self):
        return f'Score: {self.score}\nMatches played: {self.matches}\nMinutes played: {self.time}\nKills: {self.kills}\nWins: {self.wins}\nTop 3: {self.top3}\nTop 5: {self.top5}\nTop 6: {self.top6}\nTop 10: {self.top10}\nTop 12: {self.top12}\nTop 25: {self.top25}'

class Shop(object):
    def __init__(self, status, response):
        self.status = status
        storefronts = False
        self.storefronts = {}
        for name in response:
            value = response[name]
            if name == 'dailyPurchaseHrs':
                self.dailyPurchaseHours = value
            elif name == 'expiration':
                self.expiration = value
            elif name == 'refreshIntervalHrs':
                self.refreshIntervalHours = value
            elif name == 'storefronts':
                storefronts = True
        if storefronts:
            for front in response['storefronts']:
                storefront = object.Storefront(front)
                self.storefronts[storefront.name] = storefront

class Storefront(object):
    def __init__(self, storefront):
        entries = False
        self.entries = {}
        for name in storefront:
            value = storefront[name]
            if name == 'name':
                self.name = value
            elif name == 'catalogEntries':
                entries = True
        if entries:
            for entry in storefront['catalogEntries']:
                catalogEntry = object.CatalogEntry(entry)
                self.entries[catalogEntry.name] = catalogEntry
                
class CatalogEntry(object):
    def __init__(self, entry):
        prices = False
        self.prices = {}
        for name in entry:
            value = entry[name]
            if name == 'title':
                self.title = value
            elif name == 'devName':
                self.devName = value
            elif name == 'description':
                self.description = value
            elif name == 'dailyLimit':
                self.dailyLimit = value
            elif name == 'monthlyLimit':
                self.monthlyLimit = value
            elif name == 'offerId':
                self.offerId = value
            elif name == 'offerType':
                self.offerType = value
            elif name == 'refundable':
                self.refundable = value
            elif name == 'prices':
                prices = True
        if prices:
            for price in entry['prices']:
                cprice = object.Price(price)
                self.prices[cprice.currencyType] = cprice
                
class Price(object):
    def __init__(self, price):
        for name in price:
            value = price[name]
            if name == 'currencyType':
                self.currencyType = value
            elif name == 'basePrice':
                self.basePrice = value
            elif name == 'regularPrice':
                self.regularPrice = value
            elif name == 'finalPrice':
                self.finalPrice = value
            elif name == 'saleExpiration':
                self.expiration = value
                
