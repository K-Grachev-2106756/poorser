"""@package get_prices docstring
    Функция get_prices() вызывается второй. Вызов асинхронный.
    Используется для получения актуальных цен на товары, их стоимости по
    скидке и информации о бонусных рублях. В параметры формируемого
    запроса передаём ID товаров, которые получили после отработки функции
    get_ids. Затем полученный список укладывается в файл Prices.json в
    кодировке UTF-8.
"""
import requests
import json

def get_prices():

    with open("ProductsIds.json","r", encoding="utf-8") as read:
        ProductsIds = json.load(read)
    ProductsIds_str = ','.join(ProductsIds)

    cookies = {
        '__hash_': 'a8ff386d587ff7fa23339969e47a5235',
        '__lhash_': '42ba09bd19bb7d4ad3767c0876d9fe36',
        'MVID_AB_PDP_CHAR': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_ACTOR_API_AVAILABILITY': 'true',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityR_67',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLC': 'true',
        'MVID_GLP': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_IMG_RESIZE': 'true',
        'MVID_INIT_DATA_OFF': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '2100000100000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_HANDOVER': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_MOBILE_FILTERS': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '67',
        'MVID_REGION_SHOP': 'S968',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_WEBP_ENABLED': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        '_gid': 'GA1.2.860601023.1672430297',
        '_ym_uid': '1672430297123553613',
        '_ym_d': '1672430297',
        '_sp_ses.d61c': '*',
        '_ym_isad': '2',
        'partnerSrc': 'yandex',
        '_ga': 'GA1.2.786643857.1672430297',
        'admitad_uid': '%D0%BC%20%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE',
        'utm_term': '%D0%BC%20%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE',
        '__SourceTracker': 'yandex__cpc',
        'admitad_deduplication_cookie': 'yandex__cpc',
        '__cpatrack': 'yandex_cpc',
        '__sourceid': 'yandex',
        '__allsource': 'yandex',
        'SMSError': '',
        'authError': '',
        'tmr_lvid': '29eb085df73e723d6b102c006728d294',
        'tmr_lvidTS': '1672430301888',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': 'cecc4f53-bd40-454e-83a8-3ca8b342f1c9',
        'advcake_track_id': '980c3b21-775b-3ce0-a096-c380ca8afba0',
        'advcake_session_id': '8ebe6cbc-b2d2-6c30-f270-ec0d1e2944f8',
        'advcake_track_url': 'https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dcpc%26utm_campaign%3Dcn%3Amg_image_name_p_pfo%7Ccid%3A81880973%26utm_content%3Dph%3A42727671487%7Cre%3A42727671487%7Ccid%3A81880973%7Cgid%3A5107957801%7Caid%3A13283670009%7Cadp%3Ano%7Cpos%3Apremium1%7Csrc%3Asearch_none%7Cdvc%3Adesktop%7Ccoef_goal%3A0%7Cregion%3A45%7C%25D0%25A7%25D0%25B5%25D0%25B1%25D0%25BE%25D0%25BA%25D1%2581%25D0%25B0%25D1%2580%25D1%258B%26utm_term%3D%25D0%25BC%2520%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%26_openstat%3DZGlyZWN0LnlhbmRleC5ydTs4MTg4MDk3MzsxMzI4MzY3MDAwOTt5YW5kZXgucnU6cHJlbWl1bQ%26yclid%3D711931062986473471',
        'advcake_utm_partner': 'cn%3Amg_image_name_p_pfo%7Ccid%3A81880973',
        'advcake_utm_webmaster': 'ph%3A42727671487%7Cre%3A42727671487%7Ccid%3A81880973%7Cgid%3A5107957801%7Caid%3A13283670009%7Cadp%3Ano%7Cpos%3Apremium1%7Csrc%3Asearch_none%7Cdvc%3Adesktop%7Ccoef_goal%3A0%7Cregion%3A45%7C%25D0%25A7%25D0%25B5%25D0%25B1%25D0%25BE%25D0%25BA%25D1%2581%25D0%25B0%25D1%2580%25D1%258B',
        'advcake_click_id': '',
        'uxs_uid': '50e23e40-887c-11ed-98d4-230064e01a5d',
        'flocktory-uuid': '358489a3-20dc-489c-a829-08014628d238-2',
        'afUserId': '55ca9e07-820c-4e6f-ac2c-4600dcc9ead7-p',
        'AF_SYNC': '1672430304613',
        'tmr_detect': '0%7C1672430305942',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80': '2449792010.20480.0000',
        'bIPs': '-1707567431',
        '_sp_id.d61c': '274922a0-b7c9-4b6d-8ba8-ee4f8e749e10.1672430298.1.1672430334..d0e61805-32c8-4ac3-b675-8259cd1dcef8..f5356fe9-8902-4eaf-ad69-4f7a04f010c6.1672430298760.23',
        '_ga_CFMZTSS5FM': 'GS1.1.1672430297.1.1.1672430433.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1672430299.1.1.1672430433.60.0.0',
        'MVID_ENVCLOUD': 'prod2',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': '__hash_=a8ff386d587ff7fa23339969e47a5235; __lhash_=42ba09bd19bb7d4ad3767c0876d9fe36; MVID_AB_PDP_CHAR=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_ACTOR_API_AVAILABILITY=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CART_AVAILABILITY=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityR_67; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GTM_ENABLED=011; MVID_IMG_RESIZE=true; MVID_INIT_DATA_OFF=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=2100000100000; MVID_LAYOUT_TYPE=1; MVID_LP_HANDOVER=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=67; MVID_REGION_SHOP=S968; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; _gid=GA1.2.860601023.1672430297; _ym_uid=1672430297123553613; _ym_d=1672430297; _sp_ses.d61c=*; _ym_isad=2; partnerSrc=yandex; _ga=GA1.2.786643857.1672430297; admitad_uid=%D0%BC%20%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE; utm_term=%D0%BC%20%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE; __SourceTracker=yandex__cpc; admitad_deduplication_cookie=yandex__cpc; __cpatrack=yandex_cpc; __sourceid=yandex; __allsource=yandex; SMSError=; authError=; tmr_lvid=29eb085df73e723d6b102c006728d294; tmr_lvidTS=1672430301888; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=cecc4f53-bd40-454e-83a8-3ca8b342f1c9; advcake_track_id=980c3b21-775b-3ce0-a096-c380ca8afba0; advcake_session_id=8ebe6cbc-b2d2-6c30-f270-ec0d1e2944f8; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dcpc%26utm_campaign%3Dcn%3Amg_image_name_p_pfo%7Ccid%3A81880973%26utm_content%3Dph%3A42727671487%7Cre%3A42727671487%7Ccid%3A81880973%7Cgid%3A5107957801%7Caid%3A13283670009%7Cadp%3Ano%7Cpos%3Apremium1%7Csrc%3Asearch_none%7Cdvc%3Adesktop%7Ccoef_goal%3A0%7Cregion%3A45%7C%25D0%25A7%25D0%25B5%25D0%25B1%25D0%25BE%25D0%25BA%25D1%2581%25D0%25B0%25D1%2580%25D1%258B%26utm_term%3D%25D0%25BC%2520%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%26_openstat%3DZGlyZWN0LnlhbmRleC5ydTs4MTg4MDk3MzsxMzI4MzY3MDAwOTt5YW5kZXgucnU6cHJlbWl1bQ%26yclid%3D711931062986473471; advcake_utm_partner=cn%3Amg_image_name_p_pfo%7Ccid%3A81880973; advcake_utm_webmaster=ph%3A42727671487%7Cre%3A42727671487%7Ccid%3A81880973%7Cgid%3A5107957801%7Caid%3A13283670009%7Cadp%3Ano%7Cpos%3Apremium1%7Csrc%3Asearch_none%7Cdvc%3Adesktop%7Ccoef_goal%3A0%7Cregion%3A45%7C%25D0%25A7%25D0%25B5%25D0%25B1%25D0%25BE%25D0%25BA%25D1%2581%25D0%25B0%25D1%2580%25D1%258B; advcake_click_id=; uxs_uid=50e23e40-887c-11ed-98d4-230064e01a5d; flocktory-uuid=358489a3-20dc-489c-a829-08014628d238-2; afUserId=55ca9e07-820c-4e6f-ac2c-4600dcc9ead7-p; AF_SYNC=1672430304613; tmr_detect=0%7C1672430305942; flacktory=no; BIGipServeratg-ps-prod_tcp80=2449792010.20480.0000; bIPs=-1707567431; _sp_id.d61c=274922a0-b7c9-4b6d-8ba8-ee4f8e749e10.1672430298.1.1672430334..d0e61805-32c8-4ac3-b675-8259cd1dcef8..f5356fe9-8902-4eaf-ad69-4f7a04f010c6.1672430298760.23; _ga_CFMZTSS5FM=GS1.1.1672430297.1.1.1672430433.0.0.0; _ga_BNX5WPP3YK=GS1.1.1672430299.1.1.1672430433.60.0.0; MVID_ENVCLOUD=prod2',
        'pragma': 'no-cache',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36',
        'x-kl-ajax-request': 'Ajax_Request',
        'x-set-application-id': 'da35ba4f-9b62-4531-b914-a9313c95e7e5',
    }

    params = {
        'productIds': ProductsIds_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()

    prices_list = response.get('body').get('materialPrices')

    all_prices = []
    for pr in prices_list:
        all_prices.append([pr["price"]["productId"], pr["price"]["basePrice"], pr["price"]["salePrice"], pr["bonusRubles"]["total"] ])

    with open('Prices.json','w', encoding="utf-8") as file:
        json.dump(all_prices, file, indent = 4, ensure_ascii = False)


def main():
    get_prices()

if __name__ == '__main__':
    main()  