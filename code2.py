import pandas as pd

df=pd.read_csv('rail_pspoints2_comparison.csv')

rail_pspoints2=df[df.ID.isin([3111,2770,2607,2534,2438,2372,2277,2220,2180,2045,2003,1994,1951,1838,1650])]																																																																			

rail_pspoints2.to_csv('rail_pspoints2')

print(rail_pspoints2)




