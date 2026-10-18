mkdir pronto
cd pronto
touch README.txt 
echo "Hello, this is a submission for HW0." >> README.txt
cat README.txt 
cd pronto 
mkdir data 
cd data
curl https://s3.amazonaws.com/pronto-data/open_data_year_one.zip -O 
ls
unzip open_data_year_one.zip 
head *.csv 
history > ~/download_pronto.bash
