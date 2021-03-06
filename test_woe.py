import pandas as pd
import numpy as np
###import information_value

data = pd.read_csv('./simple_features_test.csv')

top_vars = [
'SK_ID_CURR',
'EXT_SOURCE_3',
'NEW_EXT_SOURCES_MEAN',
'INSTAL_AMT_PAYMENT_SUM',
'INSTAL_DPD_MIN',
'INSTAL_DPD_MAX',
'PREV_CNT_PAYMENT_MEAN',
'NEW_CREDIT_TO_ANNUITY_RATIO',
'AMT_GOODS_PRICE',
'CODE_GENDER',
'CC_CNT_DRAWINGS_ATM_CURRENT_MEAN',
'AMT_CREDIT',
'INSTAL_DAYS_ENTRY_PAYMENT_SUM',
'NEW_CREDIT_TO_GOODS_RATIO',
'EXT_SOURCE_2',
'PREV_APP_CREDIT_PERC_MEAN',
'BURO_CREDIT_ACTIVE_Closed_MEAN',
'NEW_SOURCES_PROD',
'EXT_SOURCE_1',
'BURO_CREDIT_TYPE_Microloan_MEAN',
'REGION_RATING_CLIENT_W_CITY',
'NEW_CAR_TO_EMPLOY_RATIO',
'NAME_FAMILY_STATUS_Married',
'BURO_CREDIT_TYPE_Mortgage_MEAN',
'PREV_NAME_SELLER_INDUSTRY_Connectivity_MEAN',
'ACTIVE_AMT_CREDIT_SUM_DEBT_SUM',
'INSTAL_AMT_INSTALMENT_MIN',
'BURO_AMT_CREDIT_SUM_DEBT_SUM',
'BURO_AMT_CREDIT_SUM_LIMIT_SUM',
'POS_NAME_CONTRACT_STATUS_Canceled_MEAN']

top_df = data[top_vars]

export = top_df.to_csv('./top_features_test.csv')


