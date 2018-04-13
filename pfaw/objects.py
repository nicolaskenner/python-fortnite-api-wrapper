class Base:
    def __init__(self, response):
        self.response = response


class Player(Base):
    def __init__(self, response):
        super().__init__(response)
        self.name = self.response.get('displayName')
        self.id = self.response.get('id')


class BattleRoyale:
    def __init__(self, response, mode, platform):
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
    def __init__(self, response):
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
