import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import sqlite3

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error

# mpl.rc('font',family='NanumGothic')
# mpl.rc('axes',unicode_minus=False)
# sns.set(font='NanumGothic', rc={'axes.unicode_minus':False}, style='darkgrid')
# plt.rc('figure',figsize=(10,8))
# warnings.filterwarnings('ignore')



# con = sqlite3.connect('server\db.sqlite3')
# cur = con.cursor()
# query = cur.execute("SELECT * From movies_movie")

# cols = [column[0] for column in query.description]

# movies = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

# print(race_result)
movies=pd.read_csv('c:/Users/multicampus/Desktop/ssafy8/03.학생용/fp/server/ml-latest-small/movies.csv')

# print(movies)

ratings=pd.read_csv('c:/Users/multicampus/Desktop/ssafy8/03.학생용/fp/server/ml-latest-small/ratings.csv')

# print('데이터 다 읽음')

ratings_matrix=ratings.pivot_table("rating","userId","movieId")
rating_movies=pd.merge(ratings,movies,on="movieId")
ratings_matrix=rating_movies.pivot_table("rating","userId","title")
ratings_matrix.fillna(0,inplace=True)
ratings_matrix_T=ratings_matrix.T

item_sim = cosine_similarity(ratings_matrix_T, ratings_matrix_T)
item_sim_df = pd.DataFrame(
    item_sim, index=ratings_matrix_T.index, columns=ratings_matrix_T.index)


print('진행중1')


def predict_rating(ratings_arr,item_sim_arr):
    sum_sr = ratings_arr @ item_sim_arr
    sum_s_abs = np.array([np.abs(item_sim_arr).sum(axis=1)])
    ratings_pred = sum_sr/sum_s_abs
    return ratings_pred


ratings_pred = predict_rating(ratings_matrix.values, item_sim_df.values)
ratings_pred_matrix = pd.DataFrame(
    data=ratings_pred, index=ratings_matrix.index, columns=ratings_matrix.columns)


print('진행중2')


def get_mse(pred,actual):
    pred=pred[actual.nonzero()].flatten()
    actual=actual[actual.nonzero()].flatten()
    return mean_squared_error(pred,actual)

def get_mse(pred, actual):
    pred = pred[actual.nonzero()].flatten()
    actual = actual[actual.nonzero()].flatten()
    return mean_squared_error(pred, actual)


MSE1 = get_mse(ratings_pred, ratings_matrix.values)


def predict_rating_topsim(ratings_arr, item_sim_arr, N=20):
    # 사용자-아이템 평점 행렬 크기만큼 0으로 채운 예측 행렬 초기화
    pred = np.zeros(ratings_arr.shape)

    # for col in range(ratings.arr.)

    # 사용자-아이템 평점 행렬의 열 크기(아이템 수)만큼 반복 (row: 사용자, col: 아이템)
    for col in range(ratings_arr.shape[1]):

        # 특정 아이템의 유사도 행렬 오름차순 정렬시 index .. (1)
        temp = np.argsort(item_sim_arr[:, col])

        # (1)의 index를 역순으로 나열시 상위 N개의 index = 특정 아이템의 유사도 상위 N개 아이템 index .. (2)
        top_n_items = [temp[:-1-N:-1]]

        # 개인화된 예측 평점을 계산: 반복당 특정 아이템의 예측 평점(사용자 전체)
        for row in range(ratings_arr.shape[0]):

            # (2)의 유사도 행렬
            item_sim_arr_topN = item_sim_arr[col, :][top_n_items].T  # N x 1

            # (2)의 실제 평점 행렬
            ratings_arr_topN = ratings_arr[row, :][top_n_items]     # 1 x N

            # 예측 평점
            pred[row, col] = ratings_arr_topN @ item_sim_arr_topN
            pred[row, col] /= np.sum(np.abs(item_sim_arr_topN))

    return pred


ratings_pred = predict_rating_topsim(
    ratings_matrix.values, item_sim_df.values, N=20)


MSE2 = get_mse(ratings_pred, ratings_matrix.values)

ratings_pred_matrix = pd.DataFrame(
    data=ratings_pred, index=ratings_matrix.index, columns=ratings_matrix.columns)

user_rating_id = ratings_matrix.loc[9, :]
user_rating_id[user_rating_id > 0].sort_values(ascending=False)[:10]


def get_unseen_movies(ratings_matrix, userId):

    # user_rating: userId의 아이템 평점 정보 (시리즈 형태: title을 index로 가진다.)
    user_rating = ratings_matrix.loc[userId, :]

    # user_rating=0인 아직 안본 영화
    unseen_movie_list = user_rating[user_rating == 0].index.tolist()

    # 모든 영화명을 list 객체로 만듬.
    movies_list = ratings_matrix.columns.tolist()

    # 한줄 for + if문으로 안본 영화 리스트 생성
    unseen_list = [
        movie for movie in movies_list if movie in unseen_movie_list]

    return unseen_list


# 보지 않은 영화 중 예측 높은 순서로 시리즈 반환
def recomm_movie_by_userid(pred_df, userId, unseen_list, top_n=10):
    recomm_movies = pred_df.loc[userId, unseen_list].sort_values(ascending=False)[
        :top_n]

    return recomm_movies


# 아직 보지 않은 영화 리스트
unseen_list = get_unseen_movies(ratings_matrix, 9)

# 아이템 기반의 최근접 이웃 협업 필터링으로 영화 추천
recomm_movies = recomm_movie_by_userid(
    ratings_pred_matrix, 9, unseen_list, top_n=10)

# 데이터 프레임 생성
recomm_movies = pd.DataFrame(
    data=recomm_movies.values, index=recomm_movies.index, columns=['pred_score'])
print(recomm_movies)

# print(item_sim_df["Godfather, The (1972)"].sort_values(ascending=False)[1:6])
