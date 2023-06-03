import requests
import json
import streamlit as st

st.set_page_config(page_title='乃木坂46 BLOG', layout="wide")

member_list = [{'name': '乃木坂46', 'cate': '', 'code': '10001'},
               {'name': '岡本 姫奈', 'cate': '5期生', 'code': '55401'},
               {'name': '川﨑 桜', 'cate': '5期生', 'code': '55400'},
               {'name': '池田 瑛紗', 'cate': '5期生', 'code': '55397'},
               {'name': '五百城 茉央', 'cate': '5期生', 'code': '55396'},
               {'name': '中西 アルノ', 'cate': '5期生', 'code': '55395'},
               {'name': '奥田 いろは', 'cate': '5期生', 'code': '55394'},
               {'name': '冨里 奈央', 'cate': '5期生', 'code': '55393'},
               {'name': '小川 彩', 'cate': '5期生', 'code': '55392'},
               {'name': '菅原 咲月', 'cate': '5期生', 'code': '55391'},
               {'name': '井上 和', 'cate': '5期生', 'code': '55389'},
               {'name': '弓木 奈於', 'cate': '4期生', 'code': '55387'},
               {'name': '松尾 美佑', 'cate': '4期生', 'code': '55386'},
               {'name': '林 瑠奈', 'cate': '4期生', 'code': '55385'},
               {'name': '佐藤 璃果', 'cate': '4期生', 'code': '55384'},
               {'name': '黒見 明香', 'cate': '4期生', 'code': '55383'},
               {'name': '清宮 レイ', 'cate': '4期生', 'code': '48014'},
               {'name': '北川 悠理', 'cate': '4期生', 'code': '48012'},
               {'name': '金川 紗耶', 'cate': '4期生', 'code': '48010'},
               {'name': '矢久保 美緒', 'cate': '4期生', 'code': '48019'},
               {'name': '早川 聖来', 'cate': '4期生', 'code': '48018'},
               {'name': '掛橋 沙耶香', 'cate': '4期生', 'code': '48009'},
               {'name': '賀喜 遥香', 'cate': '4期生', 'code': '48008'},
               {'name': '筒井 あやめ', 'cate': '4期生', 'code': '48017'},
               {'name': '田村 真佑', 'cate': '4期生', 'code': '48015'},
               {'name': '柴田 柚菜', 'cate': '4期生', 'code': '48013'},
               {'name': '遠藤 さくら', 'cate': '4期生', 'code': '48006'},
               {'name': '与田 祐希', 'cate': '3期生', 'code': '36760'},
               {'name': '吉田 綾乃クリスティー', 'cate': '3期生', 'code': '36759'},
               {'name': '山下 美月', 'cate': '3期生', 'code': '36758'},
               {'name': '向井 葉月', 'cate': '3期生', 'code': '36757'},
               {'name': '中村 麗乃', 'cate': '3期生', 'code': '36756'},
               {'name': '佐藤 楓', 'cate': '3期生', 'code': '36755'},
               {'name': '阪口 珠美', 'cate': '3期生', 'code': '36754'},
               {'name': '久保 史緒里', 'cate': '3期生', 'code': '36753'}]

cookies = {
    'WAPID': '9ulLdh0k9EgQ2fqvv8frLAf9A6v8Qx9kvme',
    'wap_last_event': 'showWidgetPage',
    '__td_signed': 'true',
    '_ts_yjad': '1643978843049',
    '_fbp': 'fb.1.1643978843522.760024492',
    'wovn_selected_lang': 'ja',
    '_fbc': 'fb.1.1660921246855.IwAR3JBuS09qKl5C5hGlFnmSvXq4Zp1UBYNH_zuXsNk5yzQubh8zVPK7ULUnw',
    'wap_last_event': 'showWidgetPage',
    '_ga_R9MY5W6HJK': 'GS1.1.1673455267.2.1.1673455671.0.0.0',
    'wovn_uuid': 'xz0kgt10x',
    '_ga_FTL2JTLQ27': 'deleted',
    '_ga_FTL2JTLQ27': 'deleted',
    'WAPID': 'zbl5hvXIQwg48mEfUhnzZ36b55AyFHubOJy',
    '_gcl_au': '1.1.1700913064.1683221336',
    'auth_tkn_nogizaka46.com': 'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODY2NzM2OTAsImlhdCI6MTY4NDA4MTY5MCwibmJmIjowLCJzdWIiOiI3NjAwNTU0NzQxNDkxMzEzMTEiLCJpc3MiOiJmZW5zaS1pZC1ub2dpemFrYS1tb2JpbGUiLCJhdWQiOiJmZW5zaS1pZC1ub2dpemFrYS1tb2JpbGUifQ.yKCuEK_VaX_L8xZV0XDgPOPHr7jIsba_JHwK2LKzV-_LZOk1OwDSlsUa8faScViPpsu5qXmFfjFu4BRnOjsPsg',
    '_ga_MQH5407CPF': 'GS1.1.1684659932.4.0.1684659932.0.0.0',
    '__utmz': '174951741.1685186281.336.16.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '__utmc': '174951741',
    '_gid': 'GA1.2.303585636.1685585526',
    '_td': 'c9a818f0-f0bc-49c7-8ba3-fe709ff29867',
    '_ga': 'GA1.2.1489452597.1643978843',
    '_ga_FTL2JTLQ27': 'GS1.1.1685599011.151.0.1685599011.0.0.0',
    '_gat': '1',
    '__utma': '174951741.1489452597.1643978843.1685585525.1685599012.346',
    '__utmt': '1',
    '__utmb': '174951741.1.10.1685599012',
}

headers = {
    'authority': 'www.nogizaka46.com',
    'accept': '*/*',
    'accept-language': 'ja,zh;q=0.9,zh-CN;q=0.8,ko;q=0.7,en;q=0.6,tr;q=0.5',
    # 'cookie': 'WAPID=9ulLdh0k9EgQ2fqvv8frLAf9A6v8Qx9kvme; wap_last_event=showWidgetPage; __td_signed=true; _ts_yjad=1643978843049; _fbp=fb.1.1643978843522.760024492; wovn_selected_lang=ja; _fbc=fb.1.1660921246855.IwAR3JBuS09qKl5C5hGlFnmSvXq4Zp1UBYNH_zuXsNk5yzQubh8zVPK7ULUnw; wap_last_event=showWidgetPage; _ga_R9MY5W6HJK=GS1.1.1673455267.2.1.1673455671.0.0.0; wovn_uuid=xz0kgt10x; _ga_FTL2JTLQ27=deleted; _ga_FTL2JTLQ27=deleted; WAPID=zbl5hvXIQwg48mEfUhnzZ36b55AyFHubOJy; _gcl_au=1.1.1700913064.1683221336; auth_tkn_nogizaka46.com=Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODY2NzM2OTAsImlhdCI6MTY4NDA4MTY5MCwibmJmIjowLCJzdWIiOiI3NjAwNTU0NzQxNDkxMzEzMTEiLCJpc3MiOiJmZW5zaS1pZC1ub2dpemFrYS1tb2JpbGUiLCJhdWQiOiJmZW5zaS1pZC1ub2dpemFrYS1tb2JpbGUifQ.yKCuEK_VaX_L8xZV0XDgPOPHr7jIsba_JHwK2LKzV-_LZOk1OwDSlsUa8faScViPpsu5qXmFfjFu4BRnOjsPsg; _ga_MQH5407CPF=GS1.1.1684659932.4.0.1684659932.0.0.0; __utmz=174951741.1685186281.336.16.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=174951741; _gid=GA1.2.303585636.1685585526; _td=c9a818f0-f0bc-49c7-8ba3-fe709ff29867; _ga=GA1.2.1489452597.1643978843; _ga_FTL2JTLQ27=GS1.1.1685599011.151.0.1685599011.0.0.0; _gat=1; __utma=174951741.1489452597.1643978843.1685585525.1685599012.346; __utmt=1; __utmb=174951741.1.10.1685599012',
    'referer': 'https://www.nogizaka46.com/s/n46/diary/MEMBER?ima=1116',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}

select_name = st.selectbox('选择成员', (
    '乃木坂46', '与田 祐希', '吉田 綾乃クリスティー', '山下 美月', '向井 葉月', '中村 麗乃', '佐藤 楓', '阪口 珠美',
    '久保 史緒里', '弓木 奈於', '松尾 美佑', '林 瑠奈', '佐藤 璃果', '黒見 明香', '清宮 レイ', '北川 悠理', '金川 紗耶',
    '矢久保 美緒', '早川 聖来', '掛橋 沙耶香', '賀喜 遥香', '筒井 あやめ', '田村 真佑', '柴田 柚菜', '遠藤 さくら',
    '岡本 姫奈',
    '川﨑 桜', '池田 瑛紗', '五百城 茉央', '中西 アルノ', '奥田 いろは', '冨里 奈央', '小川 彩', '菅原 咲月', '井上 和'))

st_ = st.number_input('请输入页码：', value=1)

st_num = int((st_ - 1) * 32)


def member_select(select_name):
    for i in member_list:
        if select_name == i['name']:
            return i['code']


params = {
    'ima': '1116',
    'rw': '32',
    'st': f'{st_num}',
    'callback': 'res',
}

response = requests.get('https://www.nogizaka46.com/s/n46/api/list/blog', params=params, cookies=cookies,
                        headers=headers)

css = '''<style>
img {
    width: 100%;
    border-radius: 12px;
    height: 50%;
    aspect-ratio: 1/1;
    object-fit: cover;
}

#container {
  max-width: 50%;

  /* 在水平轴线上居中放置 container */
  margin: 0 auto;

  /* 在 container 上方添加空白区域（视窗高度的 20% 位置） */
  margin-top: 2vh;
}

.card {
  /* 修改背景色 */
  background-color: white;

  /* 增加边框 */
  border: 1px solid #bacdd8;

  /* 在边框和内容之间添加空白区域 */
  padding: 8px;

  border-radius: 12px;
}

/* 给具有 tag class 的 div 元素添加样式 */
.member_name {
    display:table;
    margin: 0 auto;
    font-size: 16px;
    color: #9e3eb2;
}

.blog_title {
    font-size: 20px;
    color: #9e3eb2;
}

.update_date {
  font-size: 12px;
  display:table;
  margin: 0 auto;
  color: #788697;
}

.css-b3z5c9{
    border: none;
    padding: 6px 24px;
    border-radius: 30px;
    
    font-weight: 600;
    color: #ffffff;
    background-color: #9e3eb2;
    
    /* Button 默认是行内元素，display 属性值为 block，margin 值为 0 auto; */
    margin: 0 auto;
    display: block;
    
    /* Button 是一个可点击的元素，因此需要有一个 pointer cursor */
    cursor: pointer;
}

.css-b3z5c9:focus,
.css-b3z5c9:hover {
  background-color: #C46ED6;
  color: #ffffff;
}

</style>'''

st.markdown(css, unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)


def member_blog(code):
    member_headers = {
        'authority': 'www.nogizaka46.com',
        'accept': '*/*',
        'accept-language': 'ja,zh;q=0.9,zh-CN;q=0.8,ko;q=0.7,en;q=0.6,tr;q=0.5',
        # 'cookie': 'WAPID=9ulLdh0k9EgQ2fqvv8frLAf9A6v8Qx9kvme; wap_last_event=showWidgetPage; __td_signed=true; _ts_yjad=1643978843049; _fbp=fb.1.1643978843522.760024492; wovn_selected_lang=ja; _fbc=fb.1.1660921246855.IwAR3JBuS09qKl5C5hGlFnmSvXq4Zp1UBYNH_zuXsNk5yzQubh8zVPK7ULUnw; wap_last_event=showWidgetPage; _ga_R9MY5W6HJK=GS1.1.1673455267.2.1.1673455671.0.0.0; wovn_uuid=xz0kgt10x; _ga_FTL2JTLQ27=deleted; _ga_FTL2JTLQ27=deleted; WAPID=zbl5hvXIQwg48mEfUhnzZ36b55AyFHubOJy; _gcl_au=1.1.1700913064.1683221336; auth_tkn_nogizaka46.com=Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODY2NzM2OTAsImlhdCI6MTY4NDA4MTY5MCwibmJmIjowLCJzdWIiOiI3NjAwNTU0NzQxNDkxMzEzMTEiLCJpc3MiOiJmZW5zaS1pZC1ub2dpemFrYS1tb2JpbGUiLCJhdWQiOiJmZW5zaS1pZC1ub2dpemFrYS1tb2JpbGUifQ.yKCuEK_VaX_L8xZV0XDgPOPHr7jIsba_JHwK2LKzV-_LZOk1OwDSlsUa8faScViPpsu5qXmFfjFu4BRnOjsPsg; _ga_MQH5407CPF=GS1.1.1684659932.4.0.1684659932.0.0.0; __utmz=174951741.1685186281.336.16.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=174951741; _gid=GA1.2.303585636.1685585526; _td=c9a818f0-f0bc-49c7-8ba3-fe709ff29867; _ga=GA1.2.1489452597.1643978843; _ga_FTL2JTLQ27=GS1.1.1685599011.151.0.1685599011.0.0.0; _gat=1; __utma=174951741.1489452597.1643978843.1685585525.1685599012.346; __utmt=1; __utmb=174951741.1.10.1685599012',
        'referer': f'https://www.nogizaka46.com/s/n46/artist/{code}?ima=3527',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    if st_ == 1:
        st_page = 0
    else:
        st_page = int((st_ - 1) * 16)

    member_params = {
        'ct': f'{code}',
        'rw': '16',
        'st': f'{st_page}',
        'callback': 'res',
    }

    resp = requests.get('https://www.nogizaka46.com/s/n46/api/list/blog', params=member_params, cookies=cookies,
                        headers=member_headers)

    json_data = resp.content.decode().replace("res(", "")[:-2]

    member_blog_js = json.loads(json_data)

    member_blog_data = member_blog_js['data']

    member_blog_count = member_blog_js['count']

    with col1:
        i = 0
        try:
            for name in range(len(member_blog_data)):
                blog_title = member_blog_data[i]['title']
                member_name = member_blog_data[i]['name']
                update_date = member_blog_data[i]['date'][:16]
                list_img = member_blog_data[i]['img']
                blog_text = member_blog_data[i]['text']
                sidebar = st.sidebar
                if list_img == '/files/46/assets/img/blog/none.png':
                    list_img = list_img.replace('/files/46/assets/img/blog/none.png',
                                                'https://www.nogizaka46.com/files/46/assets/img/blog/none.png')
                if '/files/' in blog_text:
                    blog_text = blog_text.replace('/files/', 'https://www.nogizaka46.com/files/').replace('.jpg"',
                                                                                                          '.jpg" style="width: 100%;height: 50%;"')
                if '/images/' in blog_text:
                    blog_text = blog_text.replace('/images/', 'https://www.nogizaka46.com/images/').replace('.jpg"',
                                                                                                            '.jpg" style="width: 100%;height: 50%;"')

                st.markdown(
                    f'<div id="container"><div class="card"><img src="{list_img}"></div><span class="member_name">{member_name}</span><span class="update_date">{update_date}</span></div></div>',
                    unsafe_allow_html=True)
                if st.button('查看BLOG', key=i):
                    sidebar.write(f'<div class="blog_title">{blog_title}</div><br>' + blog_text, unsafe_allow_html=True)
                    if sidebar.button('关闭'):
                        sidebar.empty()

                i += 4
        except IndexError:
            pass
    with col2:
        i = 1

        try:
            for name in range(len(member_blog_data)):
                blog_title = member_blog_data[i]['title']
                member_name = member_blog_data[i]['name']
                update_date = member_blog_data[i]['date'][:16]
                list_img = member_blog_data[i]['img']
                blog_text = member_blog_data[i]['text']
                sidebar = st.sidebar
                if list_img == '/files/46/assets/img/blog/none.png':
                    list_img = list_img.replace('/files/46/assets/img/blog/none.png',
                                                'https://www.nogizaka46.com/files/46/assets/img/blog/none.png')
                if '/files/' in blog_text:
                    blog_text = blog_text.replace('/files/', 'https://www.nogizaka46.com/files/').replace('.jpg"',
                                                                                                          '.jpg" style="width: 100%;height: 50%;"')
                if '/images/' in blog_text:
                    blog_text = blog_text.replace('/images/', 'https://www.nogizaka46.com/images/').replace('.jpg"',
                                                                                                            '.jpg" style="width: 100%;height: 50%;"')

                st.markdown(
                    f'<div id="container"><div class="card"><img src="{list_img}"></div><span class="member_name">{member_name}</span><span class="update_date">{update_date}</span></div></div>',
                    unsafe_allow_html=True)
                if st.button('查看BLOG', key=i):
                    sidebar.write(f'<div class="blog_title">{blog_title}</div><br>' + blog_text, unsafe_allow_html=True)
                    if sidebar.button('关闭'):
                        sidebar.empty()

                i += 4
        except IndexError:
            pass

    with col3:
        i = 2

        try:
            for name in range(len(member_blog_data)):
                blog_title = member_blog_data[i]['title']
                member_name = member_blog_data[i]['name']
                update_date = member_blog_data[i]['date'][:16]
                list_img = member_blog_data[i]['img']
                blog_text = member_blog_data[i]['text']
                sidebar = st.sidebar
                if list_img == '/files/46/assets/img/blog/none.png':
                    list_img = list_img.replace('/files/46/assets/img/blog/none.png',
                                                'https://www.nogizaka46.com/files/46/assets/img/blog/none.png')
                if '/files/' in blog_text:
                    blog_text = blog_text.replace('/files/', 'https://www.nogizaka46.com/files/').replace('.jpg"',
                                                                                                          '.jpg" style="width: 100%;height: 50%;"')
                if '/images/' in blog_text:
                    blog_text = blog_text.replace('/images/', 'https://www.nogizaka46.com/images/').replace('.jpg"',
                                                                                                            '.jpg" style="width: 100%;height: 50%;"')

                st.markdown(
                    f'<div id="container"><div class="card"><img src="{list_img}"></div><span class="member_name">{member_name}</span><span class="update_date">{update_date}</span></div></div>',
                    unsafe_allow_html=True)
                if st.button('查看BLOG', key=i):
                    sidebar.write(f'<div class="blog_title">{blog_title}</div><br>' + blog_text, unsafe_allow_html=True)
                    if sidebar.button('关闭'):
                        sidebar.empty()

                i += 4
        except IndexError:
            pass
    with col4:
        i = 3

        try:
            for name in range(len(member_blog_data)):
                blog_title = member_blog_data[i]['title']
                member_name = member_blog_data[i]['name']
                update_date = member_blog_data[i]['date'][:16]
                list_img = member_blog_data[i]['img']
                blog_text = member_blog_data[i]['text']
                sidebar = st.sidebar
                if list_img == '/files/46/assets/img/blog/none.png':
                    list_img = list_img.replace('/files/46/assets/img/blog/none.png',
                                                'https://www.nogizaka46.com/files/46/assets/img/blog/none.png')
                if '/files/' in blog_text:
                    blog_text = blog_text.replace('/files/', 'https://www.nogizaka46.com/files/').replace('.jpg"',
                                                                                                          '.jpg" style="width: 100%;height: 50%;"')
                if '/images/' in blog_text:
                    blog_text = blog_text.replace('/images/', 'https://www.nogizaka46.com/images/').replace('.jpg"',
                                                                                                            '.jpg" style="width: 100%;height: 50%;"')

                st.markdown(
                    f'<div id="container"><div class="card"><img src="{list_img}"></div><span class="member_name">{member_name}</span><span class="update_date">{update_date}</span></div></div>',
                    unsafe_allow_html=True)
                if st.button('查看BLOG', key=i):
                    sidebar.write(f'<div class="blog_title">{blog_title}</div><br>' + blog_text, unsafe_allow_html=True)
                    if sidebar.button('关闭'):
                        sidebar.empty()

                i += 4
        except IndexError:
            pass


def all_blog():
    if response.status_code == 200:

        json_data = response.content.decode().replace("res(", "")[:-2]

        data_js = json.loads(json_data)

        data = data_js['data']

        with col1:
            # blog列表
            i = 0

            try:
                for name in range(8):
                    blog_title = data[i]['title']
                    member_name = data[i]['name']
                    update_date = data[i]['date'][:16]
                    list_img = data[i]['img']
                    blog_text = data[i]['text']
                    if list_img == '/files/46/assets/img/blog/none.png':
                        list_img = list_img.replace('/files/46/assets/img/blog/none.png',
                                                    'https://www.nogizaka46.com/files/46/assets/img/blog/none.png')
                    sidebar = st.sidebar
                    if '/files/' in blog_text:
                        blog_text = blog_text.replace('/files/', 'https://www.nogizaka46.com/files/').replace('.jpg"',
                                                                                                              '.jpg" style="width: 100%;height: 50%;"')
                    if '/images/' in blog_text:
                        blog_text = blog_text.replace('/images/', 'https://www.nogizaka46.com/images/').replace('.jpg"',
                                                                                                                '.jpg" style="width: 100%;height: 50%;"')

                    st.markdown(
                        f'<div id="container"><div class="card"><img src="{list_img}"></div><span class="member_name">{member_name}</span><span class="update_date">{update_date}</span></div></div>',
                        unsafe_allow_html=True)
                    if st.button('查看BLOG', key=i):
                        sidebar.write(f'<div class="blog_title">{blog_title}</div><br>' + blog_text, unsafe_allow_html=True)
                        if sidebar.button('关闭'):
                            sidebar.empty()

                    i += 4
            except IndexError:
                pass
        with col2:
            i = 1

            try:
                for name in range(8):
                    blog_title = data[i]['title']
                    member_name = data[i]['name']
                    update_date = data[i]['date'][:16]
                    list_img = data[i]['img']
                    blog_text = data[i]['text']
                    if list_img == '/files/46/assets/img/blog/none.png':
                        list_img = list_img.replace('/files/46/assets/img/blog/none.png',
                                                    'https://www.nogizaka46.com/files/46/assets/img/blog/none.png')
                    sidebar = st.sidebar
                    if '/files/' in blog_text:
                        blog_text = blog_text.replace('/files/', 'https://www.nogizaka46.com/files/').replace('.jpg"',
                                                                                                              '.jpg" style="width: 100%;height: 50%;"')
                    if '/images/' in blog_text:
                        blog_text = blog_text.replace('/images/', 'https://www.nogizaka46.com/images/').replace('.jpg"',
                                                                                                                '.jpg" style="width: 100%;height: 50%;"')

                    st.markdown(
                        f'<div id="container"><div class="card"><img src="{list_img}"></div><span class="member_name">{member_name}</span><span class="update_date">{update_date}</span></div></div>',
                        unsafe_allow_html=True)
                    if st.button('查看BLOG', key=i):
                        sidebar.write(f'<div class="blog_title">{blog_title}</div><br>' + blog_text,
                                      unsafe_allow_html=True)
                        if sidebar.button('关闭'):
                            sidebar.empty()

                    i += 4
            except IndexError:
                pass

        with col3:
            i = 2

            try:
                for name in range(8):
                    blog_title = data[i]['title']
                    member_name = data[i]['name']
                    update_date = data[i]['date'][:16]
                    list_img = data[i]['img']
                    blog_text = data[i]['text']
                    if list_img == '/files/46/assets/img/blog/none.png':
                        list_img = list_img.replace('/files/46/assets/img/blog/none.png',
                                                    'https://www.nogizaka46.com/files/46/assets/img/blog/none.png')
                    sidebar = st.sidebar
                    if '/files/' in blog_text:
                        blog_text = blog_text.replace('/files/', 'https://www.nogizaka46.com/files/').replace('.jpg"',
                                                                                                              '.jpg" style="width: 100%;height: 50%;"')
                    if '/images/' in blog_text:
                        blog_text = blog_text.replace('/images/', 'https://www.nogizaka46.com/images/').replace('.jpg"',
                                                                                                                '.jpg" style="width: 100%;height: 50%;"')

                    st.markdown(
                        f'<div id="container"><div class="card"><img src="{list_img}"></div><span class="member_name">{member_name}</span><span class="update_date">{update_date}</span></div></div>',
                        unsafe_allow_html=True)
                    if st.button('查看BLOG', key=i):
                        sidebar.write(f'<div class="blog_title">{blog_title}</div><br>' + blog_text,
                                      unsafe_allow_html=True)
                        if sidebar.button('关闭'):
                            sidebar.empty()

                    i += 4
            except IndexError:
                pass
        with col4:
            i = 3

            try:
                for name in range(8):
                    blog_title = data[i]['title']
                    member_name = data[i]['name']
                    update_date = data[i]['date'][:16]
                    list_img = data[i]['img']
                    blog_text = data[i]['text']
                    if list_img == '/files/46/assets/img/blog/none.png':
                        list_img = list_img.replace('/files/46/assets/img/blog/none.png',
                                                    'https://www.nogizaka46.com/files/46/assets/img/blog/none.png')
                    sidebar = st.sidebar
                    if '/files/' in blog_text:
                        blog_text = blog_text.replace('/files/', 'https://www.nogizaka46.com/files/').replace('.jpg"',
                                                                                                              '.jpg" style="width: 100%;height: 50%;"')
                    if '/images/' in blog_text:
                        blog_text = blog_text.replace('/images/', 'https://www.nogizaka46.com/images/').replace('.jpg"',
                                                                                                                '.jpg" style="width: 100%;height: 50%;"')

                    st.markdown(
                        f'<div id="container"><div class="card"><img src="{list_img}"></div><span class="member_name">{member_name}</span><span class="update_date">{update_date}</span></div></div>',
                        unsafe_allow_html=True)
                    if st.button('查看BLOG', key=i):
                        sidebar.write(f'<div class="blog_title">{blog_title}</div><br>' + blog_text,
                                      unsafe_allow_html=True)
                        if sidebar.button('关闭'):
                            sidebar.empty()

                    i += 4
            except IndexError:
                pass


if select_name == '乃木坂46':
    all_blog()
if member_select(select_name):
    member_blog(member_select(select_name))
