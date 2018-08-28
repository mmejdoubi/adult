# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:01:19 2018

@author: MEJDOUBI MOHAMED
"""

""" a placer dans un module utils.py """
def load_data(input_file, tbl_type):
    """
    fonction generique qui charge le csv, drop colonnes inutiles, format les dates..
    :param input_file: emplacement du fichier csv
    :param tbl_type: REF / LOG
    
    :return: dataframe
    """
    return true

def make_labels(
        entity_id,
        df,
        time_col,
        prediction_window,
        label_filter
        ):
    """
    genere le df idClient | cutoff_time | label (variable target)
    
    :param entity_id = entite pour laquelle on calcul les aggregats : idclient
    :param df = le df en entrée => table de log de transactions/Events
    :param time_col = la colonne avec date event à partir de la quelle commence
    calcul de la target
    :param prediction_window => exprimée en nbre de jours APRES time_col
    :param : seuil / condition pour label = True : 
        label true si count(events)  > X transactions pendant prediction_window
        label true si Sum(amount) > 100 dh
        label true si sum(amount) > 50dh where product_category = 'jean'
    :return: df avec idClient | cutoff_time | label
    """
    return 0

def computeFeatures(
     entity_id,
     log_df,
     time_col,
     cutoff_df,
     cutoff_time_col,
     n_periods,
     period_window,
     bin_cols,
     n_bins,
     time_features,
     group_by_cols
     ):
     """
         :param: entity_id => id_client
         :param: log_df => le df des events pour lequel on crée les agg
         :param: time_col => col date evenement au format timestamp
         :param: cutoff_df => le df avec variable qui 'censure' les events
         à prendre en consideration :
             exemple : signup_date de l'utilisateur'
             exemple 2 : df calculé par fonction make_labels sur données de logs
        :param: cutoff_time_col colonne date, les agg sont calcule avec 
        event_date < cutoff_time_col
        
        :param: n_periods => intervalles egales pour lesquelles on calcule les agg
        pour derniers six mois avant cutoff_time_col, n_periods=6
        
        :param: period_window = longueur en jours de chaque fenetre temporelle
        exemple : historique trx clients mensuels sur derniers 6mois :
                n_periods = 6 + period_window = 30
                
        :param: bin_cols = ['price', 'Quantity'], les colonnes numeriques a 
        discretiser en intervalles et utiliser comme vars de group_by 
        exemple : nb_trx_price_500MAD
                  nb_trx_quantity_plus_10_articles
                 
        :param: n_bins :> nbre intervalles pour decouper les bin_cols = 5
        
        :param: time_features = True/False, si time_col doit etre derivée 
        les colonnes : time_of_day, day_of_week, month, is_weekend...
        
        :param: group_by_cols= ['canal', 'is_retour', 'is_mobile'] 
                                + time_features
                                + bin_cols
        
        SEQUENCE DE CONSTRUCTION DES FEATURES
        =========================================
        1/ generation des agg globaux (sans filtres group_by, ni fenetre temps):
        total_sum_amount
        total_count_distinct_product
        total_count_trx
        
        2/ generation des agg pour chaque fenetre temporelle : 
            sum_amount_p1/p..k
            
        3/ generation des agg par split des group_by_vars:
            sum_amount_canal_ONLINE
            count_trx_TOD_AFTERNOON
        4/ generation des agg split par combinaison periode x group_by
        
        5/ meta operateurs : genre diff entre 
        trend lineaire sur count_trx par periode => capter croissance / 
        reduction de l'usage
     """
     return true
