token = 'https://account-public-service-prod03.ol.epicgames.com/account/api/oauth/token'
exchange = 'https://account-public-service-prod03.ol.epicgames.com/account/api/oauth/exchange'
player = 'https://persona-public-service-prod06.ol.epicgames.com/persona/api/public/account/lookup?q={}'
battle_royale = 'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/stats/accountId/{}/bulk/window/alltime'
status = 'https://lightswitch-public-service-prod06.ol.epicgames.com/lightswitch/api/service/bulk/status?serviceId=Fortnite'
friends = 'https://friends-public-service-prod06.ol.epicgames.com/friends/api/public/friends/{}'
store = 'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/storefront/v2/catalog?rvn={}'
news = 'https://fortnitecontent-website-prod07.ol.epicgames.com/content/api/pages/fortnite-game'
patch_notes = 'https://www.epicgames.com/fortnite/api/blog/getPosts'
blog = 'https://www.epicgames.com/fortnite/{}/news/{}'
leaderboard = 'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/leaderboards/type/global/stat/br_placetop1_{}_m0{}/window/weekly'
account = 'https://account-public-service-prod03.ol.epicgames.com/account/api/public/account?accountId={}'


class Platform:
    pc = 'pc'
    ps4 = 'ps4'
    xb1 = 'xb1'


class Mode:
    solo = '_p2'
    duo = '_p10'
    squad = '_p9'
