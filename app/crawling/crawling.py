import requests
from bs4 import BeautifulSoup
from fastapi import APIRouter

lyrics_crawling = APIRouter()


@lyrics_crawling.get("/get_lyrics")
async def get_lyrics(song_title: str):
    song_id = search_song_id(song_title)
    print(song_id)

    if song_id:
        print(f"The song ID for '{song_title}' is: {song_id}")
    else:
        print("The song ID could not be found.")

    lyrics = get_lyrics_by_song_id(song_id)
    # if lyrics is None:
    #     lyrics = get_lyrics_by_song_id_19(song_id)
    if lyrics:
        print(lyrics)
    else:
        print("가사를 찾을 수 없습니다.")

    return lyrics


def get_lyrics_by_song_id(song_id):
    url = f"https://www.melon.com/song/detail.htm?songId={song_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    lyrics = soup.find("div", class_="lyric")

    if lyrics:
        for br in lyrics.find_all("br"):
            br.replace_with("<br>")
        return lyrics.get_text().strip()

    return None


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# load_dotenv(os.path.join(BASE_DIR, "../.env"))
# client_id = os.environ["CRAWLING_ID"]
# client_password = os.environ["CRAWLING_PASSWORD"]


# def get_lyrics_by_song_id_19(song_id):
#     base_url = f"https://member.melon.com/muid/web/login/login_informM.htm"
#     url = f"https://www.melon.com/song/detail.htm?songId={song_id}"
#
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.get(base_url)
#
#     driver.find_element(By.XPATH, '//*[@id="id"]').send_keys(client_id)
#     time.sleep(1)
#     driver.find_element(By.XPATH, '//*[@id="pwd"]').send_keys(client_password)
#     time.sleep(1)
#
#     driver.find_element(By.XPATH, '//*[@id="btnLogin"]').click()
#     time.sleep(1)
#
#     driver.get(url)
#     time.sleep(1)
#
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#
#     lyrics = soup.find("div", class_="lyric")
#
#     if lyrics:
#         for br in lyrics.find_all("br"):
#             br.replace_with("<br>")
#         print(lyrics.get_text().strip())
#         return lyrics.get_text().strip()
#
#     return None


def search_song_id(title):
    base_url = f"https://www.melon.com/search/song/index.htm?q={title}&section=&searchGnbYn=Y&kkoSpl=Y&kkoDpType=&ipath=srch_form"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    song_id_tag = soup.select_one('.btn_icon_detail')

    if song_id_tag is not None:
        song_id = song_id_tag.get('href').split('\'')[9]
        return song_id

    return None

# def search_songs():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
#     driver.maximize_window()
#
#     url = f'https://www.melon.com/chart/index.htm'
#     driver.get(url)
#
#     driver.find_element(By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/div/div/button/span').click()
#
#     year = 2022
#
#     for i in range(1, 4):
#         for j in range(1, 11):
#             result = []
#
#             if i == 1 and j > 3:
#                 continue
#
#             # 연간차트 클릭
#             driver.find_element(By.XPATH, '//*[@id="d_chart_search"]/div/h4[3]/a').click()
#             time.sleep(2)
#
#             # 연대선택 클릭
#             driver.find_element(By.XPATH,
#                                 '//*[@id="d_chart_search"]/div/div/div[1]/div[1]/ul/li[{}]/span/label'.format(
#                                     i)).click()
#             time.sleep(2)
#
#             # 연도선택 클릭
#             driver.find_element(By.XPATH, '//*[@id="d_chart_search"]/div/div/div[2]/div[1]/ul/li[{}]/span/label'.format(
#                 j)).click()
#             time.sleep(2)
#
#             # 장르선택 종합 클릭
#             driver.find_element(By.XPATH, '//*[@id="d_chart_search"]/div/div/div[5]/div[1]/ul/li[1]/span/label').click()
#             time.sleep(2)
#
#             # 검색버튼 클릭
#             driver.find_element(By.XPATH, '//*[@id="d_srch_form"]/div[2]/button/span/span').click()
#             time.sleep(3)
#
#             html = driver.page_source
#             soup = BeautifulSoup(html, 'html.parser')
#
#             songs = soup.select('.tb_list.type02 tr')
#             count = 1
#             for song in songs:
#                 title_elem = song.select_one('div.ellipsis.rank01 > span > strong > a')
#                 artist_elem = song.select_one('div.ellipsis.rank02 > a')
#                 song_id_elem = song.select_one('button.btn_icon.play')
#
#                 if title_elem and artist_elem and song_id_elem:
#                     title = title_elem.text
#                     artist = artist_elem.text
#                     song_id = song_id_elem['data-song-no']
#
#                     lyrics = get_lyrics_by_song_id_19(song_id)
#
#                     result.append([title, artist, lyrics])
#                 print(count)
#                 count += 1
#
#             result_df = pd.DataFrame(result, columns=['title', 'artist', 'lyrics'])
#
#             result_df.to_excel('result{}.xlsx'.format(year), index=False)
#             year -= 1


# def organization_result():
#     result = []
#     for i in range(2000, 2023):
#         df = pd.read_excel('result{}.xlsx'.format(i), sheet_name='Sheet1')
#         result.append(df)
#
#     result_df = pd.concat(result)
#
#     result_df.to_excel('result.xlsx', index=False)
#
#
# def drop_duplicate_result():
#     df = pd.read_excel('result.xlsx')
#
#     df_drop_duplicates = df.drop_duplicates(keep='first')
#
#     df_drop_duplicates.to_excel('result_drop_duplicates.xlsx', index=False)
