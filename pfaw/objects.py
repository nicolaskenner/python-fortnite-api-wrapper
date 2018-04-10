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


class News(object):
    def __init__(self, status, response):
        self.status = status

        common = response.get('athenamessage').get('overrideablemessage')
        if common.get('message') is not None:
            self.common = common.get('message')
        elif common.get('messages') is not None:
            self.common = common.get('messages')
        else:
            self.common = None

        br = response.get('battleroyalenews').get('news')
        if br.get('message') is not None:
            self.br = br.get('message')
        elif br.get('messages') is not None:
            self.br = br.get('messages')
        else:
            self.br = None

        login = response.get('loginmessage').get('loginmessage')
        if login.get('message') is not None:
            self.login = login.get('message')
        elif login.get('messages') is not None:
            self.login = login.get('messages')
        else:
            self.login = None


class Profile(object):
    def __init__(self, status, response):
        self.status = status
        if 'profile_changes' in response:
            for i in range(0, len(response['profile_changes'])):
                if response['profile_changes'][i]['changeType'] == 'fullProfileUpdate' and 'profile' in \
                        response['profile_changes'][i]:
                    stats = False
                    for addr in response['profile_changes'][i]['profile']:
                        value = response['profile_changes'][i][addr]
                        if addr == 'accountId':
                            self.accountId = value
                        elif addr == 'created':
                            self.created = value
                        elif addr == 'updated':
                            self.updated = value
                        elif addr == 'stats':
                            stats = True
                    if stats == True:
                        if response['profile_changes'][i]['profile']['stats']['templateId'] == 'profile_athena':
                            for addr in response['profile_changes'][i]['profile']['stats']['attributes']:
                                value = response['profile_changes'][i]['profile']['stats']['attributes'][addr]
                                if addr == 'level':
                                    self.level = value
                                elif addr == 'accountLevel':
                                    self.accountLevel = value
                                elif addr == 'xp':
                                    self.xp = value
                                elif addr == 'season_friend_match_boost':
                                    self.friendXpBoost = value
                                elif addr == 'lifetime_wins':
                                    self.lifetimeWins = value
                                elif addr == 'book_purchased':
                                    self.battlepass = value
                                elif addr == 'season_match_boost':
                                    self.xpBoost = value
                                elif addr == 'banner_icon':
                                    self.bannerType = value
                                elif addr == 'banner_color':
                                    self.bannerColor = value
                                elif addr == 'book_level':
                                    self.battlepassLevel = value
                                elif addr == 'season_num':
                                    self.season = value
                                elif addr == 'book_xp':
                                    self.battlepassStars = value
                                elif addr == 'favorite_character':
                                    self.character = value
                                elif addr == 'favorite_backpack':
                                    self.backbling = value
                                elif addr == 'favorite_skydivecontrail':
                                    self.trail = value
                                elif addr == 'favorite_pickaxe':
                                    self.pickaxe = value
                                elif addr == 'favorite_glider':
                                    self.glider = value
                                elif addr == 'favorite_loadingscreen':
                                    self.loadingscreen = value
                                elif addr == 'favorite_dance':
                                    self.dances = value
                                elif addr == 'season':
                                    self.seasonWins = value['numWins']
                                elif addr == 'past_seasons':
                                    self.pastSeasons = []
                                    for i in range(0, len(value)):
                                        self.pastSeasons.append(PastSeason(value[i]))
                                elif addr == 'quest_manager':
                                    self.abandonDailyAmount = value['dailyQuestRerolls']


class PastSeason(object):
    def __init__(self, season):
        for addr in season:
            value = season[addr]
            if addr == 'seasonNumber':
                self.number = value
            elif addr == 'numWins':
                self.wins = value
            elif addr == 'seasonXp':
                self.xp = value
            elif addr == 'seasonLevel':
                self.level = value
            elif addr == 'bookXp':
                self.battlepassStars = value
            elif addr == 'bookLevel':
                self.battlepassLevel = value
            elif addr == 'purchasedVip':
                self.battepass = value
