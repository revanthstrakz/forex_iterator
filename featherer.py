import feather
import os
import glob
import pandas as pd

extension = 'csv'
pairs=['EURUSD','EURCHF','EURGBP','EURJPY','EURAUD','USDCAD','USDCHF','USDJPY','USDMXN','GBPCHF','GBPJPY','GBPUSD','AUDJPY','AUDUSD','CHFJPY','NZDJPY','NZDUSD','XAUUSD','EURCAD','AUDCAD','CADJPY','EURNZD','GRXEUR','NZDCAD','SGDJPY','USDHKD','USDNOK','USDTRY','XAUAUD','AUDCHF','AUXAUD','EURHUF','EURPLN','FRXEUR','HKXHKD','NZDCHF','SPXUSD','USDHUF','USDPLN','USDZAR','XAUCHF','ZARJPY','BCOUSD','ETXEUR','EURCZK','EURSEK','GBPAUD','GBPNZD','JPXJPY','UDXUSD','USDCZK','USDSEK','WTIUSD','XAUEUR','AUDNZD','CADCHF','EURDKK','EURNOK','EURTRY','GBPCAD','NSXUSD','UKXGBP','USDDKK','USDSGD','XAGUSD','XAUGBP']


def fetch(names,pair):
    df = pd.concat([pd.read_csv(f) for f in names ])
    path = 'feathers/'+pair+'.feather'
    feather.write_dataframe(df, path)  


years=[2000, 2002, 2002, 2002, 2002, 2000, 2000, 2000, 2010, 2002, 2002, 2000, 2002, 2000, 2002, 2006, 2005, 2009, 2007, 2007, 2007, 2008, 2010, 2008, 2008, 2008, 2008, 2010, 2009, 2008, 2010, 2010, 2010, 2010, 2010, 2008, 2010, 2010, 2010, 2010, 2009, 2010, 2010, 2010, 2010, 2008, 2007, 2008, 2010, 2010, 2010, 2008, 2010, 2009, 2007, 2008, 2008, 2008, 2010, 2007, 2010, 2010, 2008, 2008, 2009, 2009]


for i,pair in enumerate(pairs):
    names=[]
    for y in range(years[i],2021):
        
        names.append('data/DAT_ASCII_'+pair+'_M1_'+str(y)+'.csv')
    for m in range(1,6):
        names.append('data/DAT_ASCII_'+pair+'_M1_20210'+str(m)+'.csv')
    fetch(names,pair)
