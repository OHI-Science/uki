*** TEXT PROCESSING FOR OFFSHORE RENEWABLE ENERGY AS 11TH GOAL OHI ***

DATA: SST, WIND SPEED, WAVE HEIGHT, WAVE PERIOD
/uki/python scripts/data originates from http://sail.msk.ru/wow/ 
directory http://sail.msk.ru/wow/data/CENTENNIAL/OBS/ 2010/01 to 2015/12
information taken in consideration (units) : Latitude(degrees), Longitude(degrees), Air temperature(Celsius degrees), SST (sea surface temperature) (Celsius degrees), Wind speed (m/s), Significant wave height (m), Dominant wave period (s)

** changed all wind speeds of weird values (example 27.01138.2) to 6
** noticed after processing all data that it is a matter of combining 2 columns in CENTENNIAL/OBS/ data 


-concatanating all .txt files found in /data + sorting > total.txt
-python script used total.py in order to calculate the average of the variables across all similar Latitudes and Longitudes

IMPORTANT PYTHON SCRIPT - can be much improved - oncountries.py
-associating countries to latitudes and longitudes
oncountries.py > file.txt

-averaging on countries : countryaverage.py > fileout.txt

-sorting awk 'NR==1; NR>1 {print $0 | "sort -n"}' < fileout.txt > wavewinddata.txt


DATA: AIR DENSITY

created matrix - matrix.py
found elevation points with GPS visualizer http://www.gpsvisualizer.com/
> elevations.txt
https://www.grc.nasa.gov/www/k-12/airplane/atmos.html
calculated density - density.py

DATA: SALINITY

data from https://www.nodc.noaa.gov/General/salinity.html
averaged for 0-60 m depth for all data points > salinity.txt
salinity per country - attributing data point to countries with saloncountry.py >salinitycountry.txt
averging for each country - with salinity.py > salinityfinal.txt

sorted, deleted extra columns that are not used in this case
>airdensity.txt
>data.txt
>salinitydata.txt

FLUID DENSITY 

According to the state equation from https://www.google.co.uk/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0ahUKEwim08P2z-3VAhWnJ8AKHXiqABQQFggpMAA&url=https%3A%2F%2Fwww.niot.res.in%2FCOAT%2Fcoat_pdf%2FCHAP%2520III%2520-%2520Equation%2520of%2520State.pdf&usg=AFQjCNHXfwWKYLbkZAg2QjWiatmO26AzPg

using SST and Salinity  > fluiddensity.py > fluiddensity.txt

**REMOVED total.txt and compressed as too large for GitHub Desktop application