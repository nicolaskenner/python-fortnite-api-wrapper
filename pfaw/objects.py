from . import constants, utils


class Base:
    def __init__(self, response):
        self.response = response


class Player(Base):
    def __init__(self, response):
        super().__init__(response)
        self.name = self.response.get('displayName')
        self.id = self.response.get('id')


class BattleRoyale(Base):
    def __init__(self, response, platform):
        super().__init__(response)
        self.solo = BattleRoyaleStats(response=self.response, platform=platform, mode='_p2')
        self.duo = BattleRoyaleStats(response=self.response, platform=platform, mode='_p10')
        self.squad = BattleRoyaleStats(response=self.response, platform=platform, mode='_p9')
        self.all = BattleRoyaleStats(response=self.response, platform=platform, mode='_p')


class BattleRoyaleStats(Base):
    def __init__(self, response, platform, mode):
        super().__init__(response)
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
        for stat in self.response:
            if platform in stat.get('name') and mode in stat.get('name'):
                if 'score_' in stat.get('name'):
                    self.score += stat.get('value')
                elif 'matchesplayed_' in stat.get('name'):
                    self.matches += stat.get('value')
                elif 'minutesplayed_' in stat.get('name'):
                    self.time += stat.get('value')
                elif 'kills_' in stat.get('name'):
                    self.kills += stat.get('value')
                elif 'placetop1_' in stat.get('name'):
                    self.wins += stat.get('value')
                elif 'placetop3_' in stat.get('name'):
                    self.top3 += stat.get('value')
                elif 'placetop5_' in stat.get('name'):
                    self.top5 += stat.get('value')
                elif 'placetop6_' in stat.get('name'):
                    self.top6 += stat.get('value')
                elif 'placetop10_' in stat.get('name'):
                    self.top10 += stat.get('value')
                elif 'placetop12_' in stat.get('name'):
                    self.top12 += stat.get('value')
                elif 'placetop25_' in stat.get('name'):
                    self.top25 += stat.get('value')


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


class News(Base):
    def __init__(self, response):
        super().__init__(response)

        common = response.get('athenamessage').get('overrideablemessage')
        if common.get('message') is not None:
            self.common = [NewsMessage(common.get('message'))]
        elif common.get('messages') is not None:
            self.common = self.message_list(common)
        else:
            self.common = None

        br = response.get('battleroyalenews').get('news')
        if br.get('message') is not None:
            self.br = [NewsMessage(br.get('message'))]
        elif br.get('messages') is not None:
            self.br = self.message_list(br)
        else:
            self.br = None

        login = response.get('loginmessage').get('loginmessage')
        if login.get('message') is not None:
            self.login = [NewsMessage(login.get('message'))]
        elif login.get('messages') is not None:
            self.login = self.message_list(login)
        else:
            self.login = None

    def message_list(self, messages):
        return [NewsMessage(response) for response in messages.get('messages')]


class NewsMessage(Base):
    def __init__(self, response):
        super().__init__(response)
        self.image = self.response.get('image')
        self.title = self.response.get('title')
        self.body = self.response.get('body')


class PatchNotes(Base):
    def __init__(self, status, response):
        super().__init__(response)
        self.status = status

        self.post_count = response.get('postCount')
        self.increment_count = response.get('incrementCount')
        self.total_blogs = response.get('blogTotal')
        self.totals = CategoryTotals(response.get('categoryTotals'))
        self.blogs = self.blog_list()

    def blog_list(self):
        return [Blog(response) for response in self.response.get('blogList')]


class CategoryTotals:
    def __init__(self, data):
        self.community = data.get('community')
        self.events = data.get('events')
        self.patch_notes = data.get('patch_notes')
        self.announcements = data.get('announcements')
        self.all = data.get('all')


class Blog:
    def __init__(self, data):
        self.trending = data.get('trending')
        self.no_top_image = data.get('noTopImage')
        self.image = data.get('image')
        self.author = data.get('author')
        self.share_image = data.get('shareImage')
        self.title = data.get('title')
        self.html_content = data.get('content')
        self.trending_image = data.get('trendingImage')
        self.category = data.get('cat')
        self.html_short = data.get('short')
        self.featured = data.get('featured')
        self.date = data.get('date')
        if self.date is not None:
            self.date = utils.convert_iso_time(self.date)
        self.id = data.get('_id')
        self.slug = data.get('slug')
        self.locale = data.get('locale')
        self.categories = data.get('category')
        self.tags = data.get('tags')
        if self.slug is not None and self.locale is not None:
            self.url = constants.blog.format(self.locale, self.slug)
        else:
            self.url = None


class Leaderboard(Base):
    def __init__(self, response):
        super().__init__(response)
        self.id = response.get('id')
        self.name = response.get('name')
        self.rank = response.get('rank')
        self.value = response.get('value')
