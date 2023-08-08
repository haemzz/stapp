import streamlit as st
import pandas as pd
import numpy as np

# 질문지 체크
_, col, _ = st.columns([2,6,2])
col.header('고객 선호도 테스트')
col.write('마음에 드는 대사를 골라보세요. (중복가능)')

user_list = []

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

checkbox = st.checkbox('대사가 없는 공연을 보고싶다.')
if checkbox:
    user_list.extend(['Nonverbal']) 

real_cats = [
    'Fantasy', 'Performance', 'History', 'Exciting', 'Nonverbal', 
    'Comedy', 'Crime', 'Serious', 'Mystery', 'Dark', 'Thriller', 
    'Family', 'Peaceful', 'Fairy Tail', 'Bright', 'Humorous', 'Drama', 
    'Realism', 'Romance', 'Blue', 'Youth', 'Philosophical', 'Dialog', 'War', 
    'Majestic', 'Deep', 'Religious', 'Tragedy', 'Revenge', 'Omnibus', 'Happiness', 
    'Adventure', 'Horror', 'Science Fiction']

st.code(set(user_list))
st.code(len(set(user_list)))
st.code(set(real_cats) - set(user_list))
st.code(set(user_list) - set(real_cats))
