class Base:
    def __init__(self, response):
        self.response = response


class Player(Base):
    def __init__(self, response):
        super().__init__(response)
        self.name = self.response.get('displayName')
        self.id = self.response.get('id')


class BattleRoyale:
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


class Store(Base):
    def __init__(self, response, status):
        super().__init__(response)
        self.refresh_interval_hrs = self.response.get('refreshIntervalHrs')
        self.daily_purchase_hrs = self.response.get('dailyPurchaseHrs')
        self.expiration = self.response.get('expiration')
        self.storefronts = self.storefront_list()

    def storefront_list(self):
        return [StoreFront(response) for response in self.response.get('storefronts')]


class StoreFront(Base):
    def __init__(self, response):
        super().__init__(response)
        self.name = self.response.get('name')
        self.catalog_entries = self.catalog_entry_list()

    def catalog_entry_list(self):
        return [CatalogEntry(response) for response in self.response.get('catalogEntries')]


class CatalogEntry(Base):
    def __init__(self, response):
        super().__init__(response)
        self.offer_id = self.response.get('offerId')
        self.dev_name = self.response.get('devName')
        self.offer_type = self.response.get('offerType')
        self.prices = self.price_list()
        self.title = self.response.get('title')
        self.description = self.response.get('description')
        self.refundable = self.response.get('refundable')

    def price_list(self):
        return [Price(response) for response in self.response.get('prices')]


class Price(Base):
    def __init__(self, response):
        super().__init__(response)
        self.currency_type = self.response.get('currencyType')
        self.regular_price = self.response.get('regularPrice')
        self.final_price = self.response.get('finalPrice')
        self.sale_expiration = self.response.get('saleExpiration')
        self.base_price = self.response.get('basePrice')


class News:
    def __init__(self, status, response):
        self.status = status

        common = response.get('athenamessage').get('overrideablemessage')
        if common.get('message') is not None:
            self.common = [common.get('message')]
        elif common.get('messages') is not None:
            self.common = common.get('messages')
        else:
            self.common = None

        br = response.get('battleroyalenews').get('news')
        if br.get('message') is not None:
            self.br = [br.get('message')]
        elif br.get('messages') is not None:
            self.br = br.get('messages')
        else:
            self.br = None

        login = response.get('loginmessage').get('loginmessage')
        if login.get('message') is not None:
            self.login = [login.get('message')]
        elif login.get('messages') is not None:
            self.login = login.get('messages')
        else:
            self.login = None


class Profile:
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


class PastSeason:
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
