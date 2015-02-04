This project explores how US economic data affects the SP&P 500.  
The relationships between the files in this repo are provided below:

1. EDA.Rmd - explores how economic data impacts the S&P 500.  It uses data from 
my_data.csv and us_population.csv

2. EDA.html - knitr output of EDA.Rmd

3. my_data.csv - US economic data from 1967 to 2014. It is data input to EDA.Rmd and the
output from get_data.Rmd.

4. us_population.csv - total US population by year.  It is data input to EDA.Rmd and 
output from sum_population.py.  Data in this file is checked for accuracy against 
US Census Bureau data online.

5. get_data.Rmd - downloads data from Quandl.com.  The site provides US economic data.  
Economic data is combined with columns in us_government.csv.  "us_government.csv" provides 
data on which political party controls the House, Senate and Presidency.

6. get_data.html - knitr output of get_data.Rmd

7. sum_population.py - sums population data in us_pop.txt by zip code by year.  It 
produces us_population.csv.

8. us_government.csv - data from http://www.infoplease.com/ipa/A0774721.html and entered 
manually into a CSV file through Excel.  Values in the categorical variables were
entered manually by observing which party had the majority.

9. us_pop.txt - downloaded .gz file from 
http://seer.cancer.gov/popdata.thru.2012/download.html. "us_pop.text" is the unzipped file
of the downloaded file.   
See http://seer.cancer.gov/popdata.thru.2012/popdic.html for the data dictionary.

References:
http://www1.nyse.com/pdfs/nyse_chap_04.pdf

http://www.infoplease.com/ipa/A0774721.html

http://seer.cancer.gov/popdata/

https://www.quandl.com

http://www.cookbook-r.com/Graphs/Plotting_distributions_(ggplot2)/

http://docs.ggplot2.org/0.9.3.1/theme.html

http://flowingdata.com/2008/02/15/how-to-read-and-use-a-box-and-whisker-plot/

http://docs.ggplot2.org/current/

http://www.cookbook-r.com/Graphs/Legends_(ggplot2)/

http://docs.ggplot2.org/current/scale_brewer.html

http://seananderson.ca/2013/10/19/reshape.html

