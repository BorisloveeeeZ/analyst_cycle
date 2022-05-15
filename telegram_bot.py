import pandas as pd
import telegram
import matplotlib.pyplot as plt
import seaborn as sns
import pandahouse as db
import io
import os


sns.set()

def feed_report(id = None):
    chat_id = 1728100829
    bot = telegram.Bot('5201797154:AAH-bDxdih6M5n8qU4YM1c8bv78MU0hqwBA')
    message = ''' Отчет за {date} по основным метрикам:
DAU: {users} ({to_users_day_ago: +.2%} к дню назад, ({to_users_week_ago: +.2%} к прошлой неделе)
Likes: {likes} ({to_likes_day_ago: +.2%} к дню назад, ({to_likes_week_ago: +.2%} к прошлой неделе)
Views: {views} ({to_views_day_ago: +.2%} к дню назад, ({to_views_week_ago: +.2%} к прошлой неделе)
CTR: {ctr} ({to_ctr_day_ago: +.2%} к дню назад, ({to_ctr_week_ago: +.2%} к прошлой неделе)
Posts: {posts} ({to_posts_day_ago: +.2%} к дню назад, ({to_posts_week_ago: +.2%} к прошлой неделе)

    '''
    
