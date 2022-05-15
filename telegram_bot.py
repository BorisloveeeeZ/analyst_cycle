import pandas as pd
import telegram
import matplotlib.pyplot as plt
import seaborn as sns
import pandahouse as db
import io
import os
import asyncio


sns.set(font_scale=2,
        style="darkgrid",
        rc={'figure.figsize': (44,20)})

def get_plot(data):

    plot_dict = {(0,0) : {'y':'users', 'title':'Уникальные пользователи'},
              (0,1) : {'y':'likes', 'title':'Количество лайков'},
              (1,0) : {'y':'views', 'title':'Количество просмотров'},
              (1,1) : {'y':'ctr', 'title':'CTR'}
    }

    fig, axes = plt.subplots(2, 2) 
    fig.suptitle('Статистика по ленте за предыдущие 7 дней')  
    for i in range(2):
        for j in range(2):
            sns.lineplot(ax = axes[i,j], data = data, x = 'date', y = plot_dict[(i, j)]['y'])
            axes[i,j].set_title(plot_dict[(i,j)]['title'])
            axes[i,j].set(xlabel = None)
            axes[i,j].set(ylabel = None)
            for ind, label in enumerate(axes[i,j].get_xticklabels()):
                if ind % 3 == 0 :
                    label.set_visible(True)
                else:
                    label.set_visible(False)    

    plot_object = io.BytesIO()
    plt.savefig(plot_object)
    plot_object.name = 'test_plot.png'
    plot_object.seek(0)
    plt.close()


    return plot_object

async def feed_report(chat_id = None):
    chat_id = chat_id or 1728100829
    bot = telegram.Bot(token = '5201797154:AAH-bDxdih6M5n8qU4YM1c8bv78MU0hqwBA')
    message = ''' Отчет за {date} по основным метрикам:
DAU: {users} ({to_users_day_ago:+.2%} к дню назад, {to_users_week_ago:+.2%} к прошлой неделе)
Likes: {likes} ({to_likes_day_ago:+.2%} к дню назад, {to_likes_week_ago:+.2%} к прошлой неделе)
Views: {views} ({to_views_day_ago:+.2%} к дню назад, {to_views_week_ago:+.2%} к прошлой неделе)
CTR: {ctr:+.2%} ({to_ctr_day_ago:+.2%} к дню назад, {to_ctr_week_ago:+.2%} к прошлой неделе)
Posts: {posts} ({to_posts_day_ago:+.2%} к дню назад, {to_posts_week_ago:+.2%} к прошлой неделе)
'''
    connection = {'host': 'https://clickhouse.lab.karpov.courses',
              'password': 'dpo_python_2020',
              'user': 'student',
              'database': 'simulator'
             }

    data = '''
       SELECT
         toDate(time) AS date,
         COUNT(DISTINCT(user_id)) AS users,
         CountIf(user_id, action = 'view') AS views,
         CountIf(user_id, action = 'like') AS likes,
         100 * likes / views AS ctr,
         (views + likes) AS posts
       FROM simulator_20220320.feed_actions
       WHERE toDate(time) between today()- 8 and today() - 1
       GROUP BY date
       ORDER BY date
    '''
   
    df = db.read_clickhouse(data, connection=connection)
    df['date'] = pd.to_datetime(df['date']).dt.date
    df = df.astype({'users': int, 'views': int, 'likes' : int, 'posts' : int})
    today = pd.Timestamp('now') - pd.DateOffset(days = 1)
    day_ago = today - pd.DateOffset(days = 1)
    week_ago = today - pd.DateOffset(days = 7)
    report = message.format(
        date = today.date(),
        users = df[df['date'] == today.date()]['users'].iloc[0],
        to_users_day_ago =(df[df['date'] == today.date()]['users'].iloc[0]
                           - df[df['date'] == day_ago.date()]['users'].iloc[0])    
                           / df[df['date'] == day_ago.date()]['users'].iloc[0],  #Считаем процент в датафрейме по колонкам
        to_users_week_ago =(df[df['date'] == today.date()]['users'].iloc[0]
                            - df[df['date'] == week_ago.date()]['users'].iloc[0])    
                            / df[df['date'] == week_ago.date()]['users'].iloc[0],

        views = df[df['date'] == today.date()]['views'].iloc[0],
        to_views_day_ago =(df[df['date'] == day_ago.date()]['views'].iloc[0])    
                            / df[df['date'] == day_ago.date()]['views'].iloc[0],

        to_views_week_ago =(df[df['date'] == today.date()]['views'].iloc[0]
                            - df[df['date'] == week_ago.date()]['views'].iloc[0])
                            / df[df['date'] == week_ago.date()]['views'].iloc[0],

        likes = df[df['date'] == today.date()]['likes'].iloc[0], 
        to_likes_day_ago =(df[df['date'] == today.date()]['likes'].iloc[0]
                            - df[df['date'] == day_ago.date()]['likes'].iloc[0])    
                            / df[df['date'] == day_ago.date()]['likes'].iloc[0], 

        to_likes_week_ago =(df[df['date'] == today.date()]['likes'].iloc[0]
                            - df[df['date'] == week_ago.date()]['likes'].iloc[0])    
                            / df[df['date'] == week_ago.date()]['likes'].iloc[0], 

        posts = df[df['date'] == today.date()]['posts'].iloc[0],
        to_posts_day_ago =(df[df['date'] == today.date()]['posts'].iloc[0]
                            - df[df['date'] == day_ago.date()]['posts'].iloc[0])    
                            / df[df['date'] == day_ago.date()]['posts'].iloc[0],

        to_posts_week_ago = (df[df['date'] == today.date()]['posts'].iloc[0]
                            - df[df['date'] == week_ago.date()]['posts'].iloc[0])    
                            / df[df['date'] == week_ago.date()]['posts'].iloc[0], 

        ctr = df[df['date'] == today.date()]['ctr'].iloc[0],
        to_ctr_day_ago =(df[df['date'] == today.date()]['ctr'].iloc[0]
                            - df[df['date'] == day_ago.date()]['ctr'].iloc[0])    
                            / df[df['date'] == day_ago.date()]['ctr'].iloc[0],

        to_ctr_week_ago = (df[df['date'] == today.date()]['ctr'].iloc[0]
                            - df[df['date'] == week_ago.date()]['ctr'].iloc[0])    
                            / df[df['date'] == week_ago.date()]['ctr'].iloc[0]
                    )

    plot_object = get_plot(df)
    await bot.sendMessage(chat_id = chat_id, text = report)
    await bot.sendPhoto(chat_id = chat_id, photo = plot_object)


try:
    asyncio.run(feed_report())
except Exception as e:
    print(e)


            
