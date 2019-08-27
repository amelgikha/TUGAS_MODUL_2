use world;
select * from city;
-- NO 1
select * from city where CountryCode = 'IDN' order by Population desc limit 10;

-- NO 2
describe country;
select ID, city.Name as nama_kota, district, country.Name as negara, city.population from
city inner join country
on city.CountryCode = country.Code order by population desc limit 10;

-- NO 3
select * from country limit 5;
select code, Name, Continent, Region, IndepYear as tahun_merdeka from country where IndepYear is not null order by IndepYear limit 10;

-- NO 4
select Continent as Benua, count(Continent) as Jumlah_Negara, sum(Population) as Populasi, AVG(LifeExpectancy) as Rata_AngkaHrpnHdp from country group by Continent having count(Continent) > 10 order by Populasi desc;
select SUM(Continent) as Benua from country where Continent = 'Asia';

-- NO 5
select Name as Nama, Continent as Benua, LifeExpectancy as AngkaHarapanHidup, GNP from country where Continent = 'Asia' order by AngkaHarapanHidup desc limit 9;

-- NO 6
select * from countrylanguage limit 5;
select countrylanguage.CountryCode as countrycode, country.Name as name, Language, IsOfficial, Percentage from
countrylanguage inner join country
on countrylanguage.CountryCode = country.Code order by Percentage desc limit 10;

-- NO 7
select * from country;
select country.Name as Negara_ASEAN, country.Population as Populasi_Negara, GNP, city.Name as IbuKota, city.Population as Populasi_Ibukota from
country inner join city
on country.Capital = city.ID where country.Name = 'Brunei' or country.Name ='Cambodia' or country.Name ='East Timor' or country.Name ='Indonesia' or country.Name ='Laos' or country.Name ='Malaysia' or country.Name ='Myanmar' or country.Name ='Philippines'or country.Name ='Singapore' or country.Name ='Thailand' or country.Name ='Vietnam' order by country.Name asc;

-- NO 8
select country.Name as Negara_G20, country.Population as Populasi_Negara, GNP, city.Name as IbuKota, city.Population as Populasi_Ibukota from
country inner join city
on country.Capital = city.ID
where country.Name='Argentina' or country.Name='Australia' or country.Name='Brazil' or country.Name='Canada' or country.Name='China' or country.Name='France' or country.Name='Germany' or country.Name='India' or country.Name='Indonesia' or country.Name='Japan' or country.Name='Mexico' or country.Name='Russian Federation' or country.Name='Saudi Arabia' or country.Name='South Africa' or country.Name='South Korea' or country.Name='Turkey' or country.Name='United Kingdom' or country.Name='United States' or 