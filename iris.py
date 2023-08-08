import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config('선호도테스트')
# 질문지 체크
tab1, tab2 = st.tabs(["고객 선호도 테스트", "선호도 기반 추천 공연"])
with tab1:
    _, col, _ = st.columns([3,6,2])
    col.header('고객 선호도 테스트')
   
    user_genre = st.multiselect(
        '선호하는 공연 장르를 선택하세요.',
        ['오페라','뮤지컬','연극']
    )
    if not user_genre:
        st.write(':red[*장르를 선택해주세요!*]')

    user_list = []
    st.write('#### 마음에 드는 대사를 골라보세요. (중복가능)')
    checkbox = st.checkbox('"카르페 디엠, 오늘을 즐겨라. 당신의 삶을 특별하게 만드세요."')
    if checkbox:
        user_list.extend(['Youth', 'Philosophical', 'Comedy'])

    checkbox = st.checkbox('"죽느냐 사느냐 그것이 문제로다!"')
    if checkbox:
        user_list.extend(['Tragedy', 'Mystery', 'Dark'])
        
    checkbox = st.checkbox('"우리 모두가 주인노릇을 할 수는 없다."')
    if checkbox:
        user_list.extend(['Tragedy', 'Deep', 'Dark'])
        
    checkbox = st.checkbox('"바닥에 떨어지면 뭐가 좋은 줄 알아? 위로 올라갈 일만 있다는거지!"')
    if checkbox:
        user_list.extend(['Exciting', 'Happiness', 'Family'])
    
    checkbox = st.checkbox('"사랑에 빠지면 비도 눈부신 햇볕으로 보이나보다"')
    if checkbox:
        user_list.extend(['Drama', 'Happiness', 'Romance'])
        
    checkbox = st.checkbox('"집만한 곳은 없다!"')
    if checkbox:
        user_list.extend(['Fantasy', 'Adventure', 'Bright']) 
    
    checkbox = st.checkbox('"아득한 북소리가 들리는가? 저노래는 그들이 이뤄나갈 미래의 소리!"')
    if checkbox:
        user_list.extend(['Serious', 'History', 'Philosophical']) 
        
    checkbox = st.checkbox('"네가 누구인지 기억해"')
    if checkbox:
        user_list.extend(['Family', 'Adventure', 'Majestic']) 

    checkbox = st.checkbox('"우리가 꿈꾸는 세상이 지금 우리가 살고 있는 세상이 되기를"')
    if checkbox:
        user_list.extend(['Drama', 'Fantasy', 'Fairy Tail']) 

    checkbox = st.checkbox('"제 이름은 셜록 홈즈, 주소는 베이커 가 221B번지입니다"')
    if checkbox:
        user_list.extend(['Mystery', 'Humorous', 'Crime']) 
        
    checkbox = st.checkbox('"4월의 날씨가 맑은 쌀쌀한 날이었다. 그리고 시계는 13시를 가리키고 있었다."')
    if checkbox:
        user_list.extend(['Dystopia', 'War', 'Dark']) 

    checkbox = st.checkbox('"포스가 함께하길"')
    if checkbox:
        user_list.extend(['Adventure', 'Science Fiction', 'Drama']) 

    checkbox = st.checkbox('"친구는 가까이 두되 적은 더 가까이 둬라"')
    if checkbox:
        user_list.extend(['Drama', 'Crime', 'Revenge']) 

    checkbox = st.checkbox('"신사 숙녀 여러분 기다리던 시간이 왔습니다."')
    if checkbox:
        user_list.extend(['Performance', 'Exciting', 'Humorous']) 

    checkbox = st.checkbox('"우린 모든 것을 잃은 후에야 무슨 일이든 자유롭게 할 수 있다	"')
    if checkbox:
        user_list.extend(['Thriller', 'Dark','Drama']) 

    checkbox = st.checkbox('"주님은 한 쪽 문을 닫으실 때 다른 한 쪽 문을 열어 놓으신다"')
    if checkbox:
        user_list.extend(['Happiness', 'Peaceful','Religious']) 

    checkbox = st.checkbox('4월의 날씨가 맑은 쌀쌀한 날이었다. 그리고 시계는 13시를 가리키고 있었다.')
    if checkbox:
        user_list.extend(['War', 'Dark', 'Blue']) 

    checkbox = st.checkbox('"지구엔 크고 검은 구명이 뚫려있지 그리고 또 다시 더러운 기생충들이 살아가지"')
    if checkbox:
        user_list.extend(['Thriller', 'Realism', 'Horror']) 

    # checkbox = st.checkbox('대사가 없는 공연을 보고싶다. (꼭)')
    # if checkbox:
    #     user_list.extend(['Nonverbal']) 

with tab2:
    uploaded_file = st.file_uploader(
        "Choose your database", accept_multiple_files=False)
    if uploaded_file is not None:
        file_name = uploaded_file
    else:
        file_name = "공연_카테고리_라벨링.xlsx"
    df = pd.read_excel(file_name)
    df = df[['Genre', 'Name', 'Category']]
    # 전처리
    df = df[df['Category'].notnull()].reset_index(drop=True)
    df['Category'] = [a.split(',') for a in df['Category']]
    df['Category'] = [sorted(a) for a in df['Category']]
    # 수정할 것 수정하기
    edit_dict = {'':None, 'Homorous':'Humorous','Circus':'Performance','kids':None,'Kids':None,'Tragidy':'Tragedy'}
    for idx in df.index:
        edit_list = []
        for cat in df.at[idx,'Category']:
            if cat in edit_dict.keys():
                cat = edit_dict[cat]
                edit_list.append(cat)
            else:
                edit_list.append(cat)
        df.at[idx,'Category'] = edit_list
    for idx in df.index:
        if None in df.at[idx,'Category']:
            df.at[idx,'Category'].remove(None)
            
    # 원본유지
    shows_df = df.copy()
    
    user_name = 'User01'
    user_record = [(user_genre, user_name, list(set(user_list)))]
    user_df = pd.DataFrame(user_record, columns=df.columns.values)

    # 유저가 선택한 장르에 해당하는 공연만, 그리고 유저 데이터를 추가하기
    user_shows_df = shows_df[shows_df['Genre'].isin(user_genre)]
    user_shows_df = user_shows_df.append(user_df).reset_index(drop = True)
    
    from sklearn.feature_extraction.text import CountVectorizer
    user_shows_df['categories_literal'] = user_shows_df['Category'].apply(lambda x: (' ').join(x))
    count_vect = CountVectorizer(min_df=0.00, ngram_range=(1,2))
    category_mat = count_vect.fit_transform(user_shows_df['categories_literal'])
    
    from sklearn.metrics.pairwise import cosine_similarity
    category_sim = cosine_similarity(category_mat,category_mat)
    category_sim_sorted_ind = category_sim.argsort()[:,::-1]
    
    def find_sim_show(df,sorted_ind,title_name = user_name,top_n = 3):
        # 기준이 되는 유저의 data와 index를 가져온다
        title_show = df[df['Name'] == title_name]
        title_index = title_show.index.values
        
        # (top_n)+1에 해당하는 장르 유서성이 높은 index 추출(유저 index를 삭제할 것이기 때문)
        similar_indexes = sorted_ind[title_index,:(top_n)+1]
        similar_indexes = similar_indexes.reshape(-1)
        
        # 유저 index는 제외
        similar_indexes = similar_indexes[similar_indexes != title_index]
        
        return df.iloc[similar_indexes]
    
    similar_shows = find_sim_show(user_shows_df, category_sim_sorted_ind, user_name, 5)
    st.dataframe(similar_shows)
real_cats = [
    'Fantasy', 'Performance', 'History', 'Exciting', 'Nonverbal', 
    'Comedy', 'Crime', 'Serious', 'Mystery', 'Dark', 'Thriller', 
    'Family', 'Peaceful', 'Fairy Tail', 'Bright', 'Humorous', 'Drama', 
    'Realism', 'Romance', 'Blue', 'Youth', 'Philosophical', 'Dialog', 'War', 
    'Majestic', 'Deep', 'Religious', 'Tragedy', 'Revenge', 'Omnibus', 'Happiness', 
    'Adventure', 'Horror', 'Science Fiction']

st.code(set(user_list))
# st.code(len(set(user_list)))
st.code(set(real_cats) - set(user_list))
st.code(set(user_list) - set(real_cats))
