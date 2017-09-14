## calculate_scores.R 

## calculate_scores.R ensures all files are properly configured and calculates OHI scores.
  ## - configure_toolbox.r ensures your files are properly configured. It is a script in your repository.
  ## - CalculateAll() calculates OHI scores. It is a function in the `ohicore` R package 
  ##   (this can be written in R as `ohicore::CalculateAll()`).  

## When you begin, configure_toolbox.r and CalculateAll() will calculate scores using
## the 'templated' data and goal models provided. We suggest you work
## goal-by-goal as you prepare data in the prep folder and develop goal models
## in functions.r. Running configure_toolbox.r and a specific goal model line-by-line 
## in functions.R is a good workflow.

## run the configure_toolbox.r script to check configuration

setwd('ore2017')
source('configure_toolbox.r')

## calculate scenario scores
scores = ohicore::CalculateAll(conf, layers)

## save scores as scores.csv
write.csv(scores, 'scores.csv', na='', row.names=F)


## visualize scores ----

## source from here until added to ohicore
source('https://raw.githubusercontent.com/OHI-Science/ohibc/master/src/R/common.R')
source('plot_flower_local.R')

library(tidyverse)

## regions info
regions <- bind_rows(
  data_frame(                # order regions to start with whole study_area
    region_id   = 0,
    region_name = 'Global'),
  read_csv('spatial/regions_list.csv') %>%
    select(region_id   = rgn_id,
           region_name = rgn_name))

## set figure name
regions <- regions %>%
  mutate(flower_png = sprintf('reports/figures/flower_%s.png',
                              str_replace_all(region_name, ' ', '_')))
readr::write_csv(regions, 'reports/figures/regions_figs.csv')

## save flower plot for each region
for (i in regions$region_id) { # i = 0
  
  ## fig_name to save
  fig_name <- regions$flower_png[regions$region_id == i]
  
  ## scores info
  score_df <- scores %>%
    filter(dimension == 'score') %>%
    filter(region_id == i)
  
  ## Casey's modified flower plot
  plot_obj <- plot_flower(score_df,
                          filename    = fig_name,
                          goals_csv   = 'conf/goals.csv',
                          incl_legend = TRUE)
  
}




