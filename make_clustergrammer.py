'''
Python 2.7
The clustergrammer python module can be installed using pip:
pip install clustergrammer

or by getting the code from the repo:
https://github.com/MaayanLab/clustergrammer-py
'''

from clustergrammer import Network
net = Network()

# load matrix tsv file
net.load_file('txt/big_data_cd1.txt')

# optional filtering and normalization
##########################################
# net.filter_sum('row', threshold=20)
net.normalize(axis='row', norm_type='zscore', keep_orig=True)
# net.filter_N_top('row', 250, rank_type='sum')
# net.filter_threshold('row', threshold=3.0, num_occur=4)
# net.swap_nan_for_zero()
# net.set_cat_color('col', 1, 'Category: one', 'blue')

  # net.make_clust()
  # net.dendro_cats('row', 5)

net.cluster(dist_type='cos',views=[] , dendro=True,
               sim_mat=True, filter_sim=0.1, calc_cat_pval=False, enrichrgram=False)

# write jsons for front-end visualizations
net.write_json_to_file('viz', 'json/big_data_cd1.json', 'indent')
# net.write_json_to_file('sim_row', 'json/mult_view_sim_row.json', 'no-indent')
# net.write_json_to_file('sim_col', 'json/mult_view_sim_col.json', 'no-indent')
