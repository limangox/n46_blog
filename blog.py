import requests
import json
import streamlit as st
st.set_page_config(layout="wide")

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

st_ = st.number_input('请输入页码：', value=1)
if st_ == 1:
    st_num = 0
else:
    st_num = int((st_ - 1) * 32)

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
    object-fit: cover;
}

#container {
  max-width: 300px;

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
  padding: 4px 8px;
  border: 1px solid #e5eaed;

  border-radius: 50px;
  font-size: 12px;
  font-weight: 600;
  color: #788697;
}

.update_date {
  padding: 4px 8px;
  border: 1px solid #e5eaed;

  border-radius: 50px;
  font-size: 12px;
  font-weight: 600;
  color: #788697;
}

/* 给具有 name class 的 div 元素添加样式 */
.title {
  font-size: 15px;
  font-weight: 600;

  margin-top: 16px;
  margin-bottom: 16px;
}
.card__details {
  /* 在细节内容周围添加空白区域 */
  padding: 16px 8px 8px 8px;
}

.css-1x8cf1d {
    margin-top: 10px !important;
    margin-left: 35% !important;
}
</style>'''

col1, col2, col3, col4 = st.columns(4, gap='large')

st.markdown(css, unsafe_allow_html=True)

if response.status_code == 200:
    json_data = response.content.decode().replace("res(", "")[:-2]

    data_js = json.loads(json_data)

    data = data_js['data']

    with col1:
        # blog列表
        i = 0

        for name in range(8):
            blog_title = data[i]['title']
            member_name = data[i]['name']
            update_date = data[i]['date']
            list_img = data[i]['img']
            blog_text = data[i]['text']
            st.write(
                f'<div id="container"><div class="card"><img src="{list_img}"><div class="card__details"><span class="member_name">{member_name}</span>&nbsp<span class="update_date">{update_date}</span><div class="title">{blog_title}</div></div></div></div>',
                unsafe_allow_html=True)
            if st.button('查看BLOG', key=i):
                sidebar = st.sidebar
                if '/files/' in blog_text:
                    blog_text = blog_text.replace('/files/', 'https://www.nogizaka46.com/files/').replace('.jpg"',
                                                                                                          '.jpg" style="width: 100%;height: 50%;"')
                    sidebar.write(blog_text, unsafe_allow_html=True)
                if '/images/' in blog_text:
                    blog_text = blog_text.replace('/images/', 'https://www.nogizaka46.com/images/').replace('.jpg"',
                                                                                                            '.jpg" style="width: 100%;height: 50%;"')
                    sidebar.write(blog_text, unsafe_allow_html=True)
                if sidebar.button('关闭'):
                    sidebar.empty()

            i += 4
        # blog正文

    with col2:
        # blog列表
        i = 1

        for name in range(8):
            blog_title = data[i]['title']
            member_name = data[i]['name']
            update_date = data[i]['date']
            list_img = data[i]['img']
            blog_text = data[i]['text']
            st.write(
                f'<div id="container"><div class="card"><img src="{list_img}"><div class="card__details"><span class="member_name">{member_name}</span>&nbsp<span class="update_date">{update_date}</span><div class="title">{blog_title}</div></div></div></div>',
                unsafe_allow_html=True)
            if st.button('查看BLOG', key=i):
                sidebar = st.sidebar
                if '/files/' in blog_text:
                    blog_text = blog_text.replace('/files/', 'https://www.nogizaka46.com/files/').replace('.jpg"',
                                                                                                          '.jpg" style="width: 100%;height: 50%;"')
                    sidebar.write(blog_text, unsafe_allow_html=True)
                if '/images/' in blog_text:
                    blog_text = blog_text.replace('/images/', 'https://www.nogizaka46.com/images/').replace('.jpg"',
                                                                                                            '.jpg" style="width: 100%;height: 50%;"')
                    sidebar.write(blog_text, unsafe_allow_html=True)
                if sidebar.button('关闭'):
                    sidebar.empty()

            i += 4

    with col3:
        # blog列表
        i = 2

        for name in range(8):
            blog_title = data[i]['title']
            member_name = data[i]['name']
            update_date = data[i]['date']
            list_img = data[i]['img']
            blog_text = data[i]['text']
            st.write(
                f'<div id="container"><div class="card"><img src="{list_img}"><div class="card__details"><span class="member_name">{member_name}</span>&nbsp<span class="update_date">{update_date}</span><div class="title">{blog_title}</div></div></div></div>',
                unsafe_allow_html=True)
            if st.button('查看BLOG', key=i):
                sidebar = st.sidebar
                if '/files/' in blog_text:
                    blog_text = blog_text.replace('/files/', 'https://www.nogizaka46.com/files/').replace('.jpg"',
                                                                                                          '.jpg" style="width: 100%;height: 50%;"')
                    sidebar.write(blog_text, unsafe_allow_html=True)
                if '/images/' in blog_text:
                    blog_text = blog_text.replace('/images/', 'https://www.nogizaka46.com/images/').replace('.jpg"',
                                                                                                            '.jpg" style="width: 100%;height: 50%;"')
                    sidebar.write(blog_text, unsafe_allow_html=True)
                if sidebar.button('关闭'):
                    sidebar.empty()

            i += 4

    with col4:
        # blog列表
        i = 3

        for name in range(8):
            blog_title = data[i]['title']
            member_name = data[i]['name']
            update_date = data[i]['date']
            list_img = data[i]['img']
            blog_text = data[i]['text']
            st.write(
                f'<div id="container"><div class="card"><img src="{list_img}"><div class="card__details"><span class="member_name">{member_name}</span>&nbsp<span class="update_date">{update_date}</span><div class="title">{blog_title}</div></div></div></div>',
                unsafe_allow_html=True)
            if st.button('查看BLOG', key=i):
                sidebar = st.sidebar
                if '/files/' in blog_text:
                    blog_text = blog_text.replace('/files/', 'https://www.nogizaka46.com/files/').replace('.jpg"',
                                                                                                          '.jpg" style="width: 100%;height: 50%;"')
                    sidebar.write(blog_text, unsafe_allow_html=True)
                if '/images/' in blog_text:
                    blog_text = blog_text.replace('/images/', 'https://www.nogizaka46.com/images/').replace('.jpg"',
                                                                                                            '.jpg" style="width: 100%;height: 50%;"')
                    sidebar.write(blog_text, unsafe_allow_html=True)
                if sidebar.button('关闭'):
                    sidebar.empty()

            i += 4
