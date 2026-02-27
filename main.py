### This will be the main file that will do all the analysis###

#call the espn_data file to retrieve results

import espn_data

dashboarddata = espn_data.gather_stats()
print(dashboarddata)