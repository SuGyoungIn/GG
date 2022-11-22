import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error

mpl.rc('font',family='NanumGothic')
mpl.rc('axes',unicode_minus=False)

sns.set(font='NanumGothic', rc={'axes.unicode_minus':False}, style='darkgrid')
plt.rc('figure',figsize=(10,8))

warnings.filterwarnings('ignore')
movies=pd.read_csv('c:/Users/multicampus/Desktop/ssafy8/03.학생용/fp/server/ml-latest-small/movies.csv')
ratings=pd.read_csv('c:/Users/multicampus/Desktop/ssafy8/03.학생용/fp/server/ml-latest-small/ratings.csv')

print(type(movies),movies)


ratings_matrix=ratings.pivot_table("rating","userId","movieId")

rating_movies=pd.merge(ratings,movies,on="movieId")
ratings_matrix=rating_movies.pivot_table("rating","userId","title")
ratings_matrix.fillna(0,inplace=True)
ratings_matrix_T=ratings_matrix.T

item_sim = cosine_similarity(ratings_matrix_T,ratings_matrix_T)
item_sim_df = pd.DataFrame(item_sim,index=ratings_matrix_T.index,columns=ratings_matrix_T.index)

def predict_rating(ratings_arr,item_sim_arr):
    sum_sr = ratings_arr @ item_sim_arr
    sum_s_abs = np.array([np.abs(item_sim_arr).sum(axis=1)])
    ratings_pred=sum_sr/sum_s_abs
    return ratings_pred


ratings_pred = predict_rating(ratings_matrix.values,item_sim_df.values)
ratings_pred_matrix = pd.DataFrame(data=ratings_pred,index=ratings_matrix.index,columns = ratings_matrix.columns)

def get_mse(pred,actual):
    pred=pred[actual.nonzero()].flatten()
    actual=actual[actual.nonzero()].flatten()
    return mean_squared_error(pred,actual)

MSE1 = get_mse(ratings_pred,ratings_matrix.values)

def predict_rating_topsim(ratings_arr,item_sim_arr,N=20):
    pred = np.zeros(ratings_arr.shape)

    # for col in range(ratings.arr.)


# print(item_sim_df["Godfather, The (1972)"].sort_values(ascending=False)[1:6])

