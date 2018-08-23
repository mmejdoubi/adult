

import pandas as pd
import numpy as np
import featuretools as ft

# import data
application_train_df = pd.read_csv('../inputs/application_train.csv')
application_test_df = pd.read_csv('../inputs/application_test.csv')

bureau_df = pd.read_csv('../inputs/bureau.csv')
bureau_balance_df = pd.read_csv('../inputs/bureau_balance.csv')

prev_application_df = pd.read_csv('../inputs/previous_application.csv')
installments_payments_df = pd.read_csv('../inputs/installments_payments.csv')
pos_balance_df = pd.read_csv('../inputs/POS_CASH_balance.csv')
cc_balance_df = pd.read_csv('../inputs/credit_card_balance.csv')

print("="*40)
print('CSV read success...')
print("="*40)


# Create new entityset
es = ft.EntitySet(id = 'clients')

es = es.entity_from_dataframe(entity_id = 'clients', dataframe = clients, 
index = 'client_id', time_index = 'joined')

# if no unique index => ask FT to create it 
es = es.entity_from_dataframe(entity_id = 'payments', 
                              dataframe = payments,
                              variable_types = {'missed': ft.variable_types.Categorical},
                              make_index = True,
                              index = 'payment_id',
time_index = 'payment_date')

