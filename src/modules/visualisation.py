# Plot the data
sns.lineplot(y='close',x='date',data=df)
sns.lineplot(y='volume',x='date',data=df)
sns.lineplot(y='marketCap',x='date',data=df)
plt.show()

sns.lineplot(y='close',x='date',data=df[df['date']>= '2018-12-01'],color='red',label='train')
sns.lineplot(y='close',x='date',data=df[df['date']>= '2019-01-01'],label='unseen')
plt.title('Bitcoin Daily Close Price')
plt.show()

sns.lineplot(y='close',x='date',data=df)
sns.lineplot(y='fft',x='date',data=df)
plt.title('Bitcoin Daily Close Price (2019 ~)')
plt.show()


# Plot KL divergence
sns.lineplot(y='kl',x='date',data=kl)
sns.lineplot(y='ma5',x='date',data=kl)
sns.lineplot(y='ma21',x='date',data=kl)
sns.lineplot(y='bolinger_high',x='date',data=kl,color='yellow')
sns.lineplot(y='bolinger_low',x='date',data=kl,color='yellow')
plt.title('KL Divergence')
plt.show()
