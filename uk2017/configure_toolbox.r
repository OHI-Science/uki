## configure_toolbox.r

## configure_toolbox.r ensures all files in your repo are properly configured. 
## It must be sourced before calculating OHI scores with ohicore::CalculateAll(); 
## it can be sourced here or is also sourced from calculate_scores.r.

## You are encouraged to use this script when developing individual goal models. A good workflow is: 
  ## 1. prepare data layers in the /prep folders (script as much as possible in R)
  ## 2. register data layers in layers.csv and save them in /layers folder
  ## 3. source configure_repo.r to ensure proper configuration
  ## 4. develop goal models in functions.r, running individual goal models line by line

## load required packages after checking whether they are already installed
pkgs_required <- c('ohicore', 'tidyverse', 'stringr', 'zoo')
pkgs_check <- pkgs_required[!pkgs_required %in% (.packages())]
pkgs_installed <- sapply(pkgs_check, FUN = function(x) library(x, character.only = TRUE))

## load scenario configuration
conf = ohicore::Conf(file.path(wd, 'conf'))

## check that scenario layers files in the \layers folder match layers.csv registration. Layers files are not modified.
ohicore::CheckLayers(file.path(wd, 'layers.csv'), 'layers', flds_id=conf$config$layers_id_fields)

## load scenario layers for ohicore to access. Layers files are not modified.
layers = ohicore::Layers(file.path(wd, 'layers.csv'), 'layers')

