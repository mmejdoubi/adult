
import numpy as np
import pandas as pd

### import des sources de donnees

installments = pd.read_csv('../inputs/installments_payments.csv')
installments.head(5)

### creation de vars 

installments_ = installments.sample(10000)
installments_['instalment_paid_late_in_days'] = installments_['DAYS_ENTRY_PAYMENT'] - installments_['DAYS_INSTALMENT'] 
installments_['instalment_paid_late'] = (installments_['instalment_paid_late_in_days'] > 0).astype(int)
installments_['instalment_paid_over_amount'] = installments_['AMT_PAYMENT'] - installments_['AMT_INSTALMENT']
installments_['instalment_paid_over'] = (installments_['instalment_paid_over_amount'] > 0).astype(int)

### defintion des fonctions de creation des agregats

def add_features(feature_name, aggs, features, feature_names, groupby):
    feature_names.extend(['{}_{}'.format(feature_name, agg) for agg in aggs])
    for agg in aggs:
        if agg == 'kurt':
            agg_func = kurtosis
        elif agg == 'iqr':
            agg_func = iqr
        else:
            agg_func = agg
        g = groupby[feature_name].agg(agg_func).reset_index().rename(index=str, columns={feature_name: '{}_{}'.format(feature_name, agg)})
        features = features.merge(g, on='SK_ID_CURR', how='left')
    return features, feature_names

### generation des agregats

### constitution de la liste contenant les id uniques
    
features = pd.DataFrame({'SK_ID_CURR':installments_['SK_ID_CURR'].unique()})
groupby = installments_.groupby(['SK_ID_CURR'])    
feature_names = []

features, feature_names = add_features('NUM_INSTALMENT_VERSION', 
                                       ['count','sum','mean','max','min','std'],
                                     features, feature_names, groupby)

features, feature_names = add_features('instalment_paid_late_in_days', 
                                       ['sum','mean','max','min','std'],
                                     features, feature_names, groupby)

features, feature_names = add_features('instalment_paid_late', ['sum','mean'],
                                     features, feature_names, groupby)

features, feature_names = add_features('instalment_paid_over_amount', 
                                       ['sum','mean','max','min','std'],
                                     features, feature_names, groupby)

features, feature_names = add_features('instalment_paid_over', ['sum','mean'],
                                     features, feature_names, groupby)

final_install_features = features.fillna(0)

test_filter = installments_[installments_['SK_ID_CURR']==376689]

