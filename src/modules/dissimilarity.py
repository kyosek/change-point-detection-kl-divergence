from datetime import date, timedelta
from scipy.stats import entropy


start_date = date(2019,2,1)
end_date = date(2020,3,28)
delta = timedelta(days=1)

kl = []
date = []

while start_date <= end_date:

    kld = entropy(np.array(df[df['date']<'2019-01-01'].close.tail(30)), np.array(df[df['date']<=start_date].close.tail(30)))
    
    kl += [kld]
    date += [start_date]

    start_date+=delta

kl = pd.DataFrame(list(zip(date,kl)),columns=['date','kl'])

kl['ma5'] = kl.kl.rolling(5).mean()
kl['ma7'] = kl.kl.rolling(7).mean()
kl['ma21'] = kl.kl.rolling(21).mean()
kl['mstd2'] = kl.kl.rolling(2).std()
kl['bolinger_high'] = kl.ma7+(kl.mstd2*2)
kl['bolinger_low'] = kl.ma7-(kl.mstd2*2)