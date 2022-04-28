.mode box
.import area.json area

create table country(id string, name string, areas object[], path text, fullkey text);
create table area(id string, name string, areas object[], path text, fullkey text);
create table city(id string,parent_id string, name string, path text, fullkey text);


insert into country (id, name, areas, path, fullkey)
select
json_extract(value, "$.id") as id,
json_extract(value, "$.name") as name,
json_extract(value, "$.areas") as areas,
path,
fullkey
from json_each(readfile("area.json"));

insert into area (id, name, areas, path, fullkey)
select
json_extract(value, "$.id") as id,
json_extract(value, "$.name") as name,
json_extract(value, "$.areas") as areas,
replace(path, '.areas', '') as path,
fullkey
from json_tree(readfile("area.json"))
where path like '%.areas';

update area
set country_id = (select id from country where area.country_id = country.id);

insert into city (id, parent_id, name, path, fullkey)
select
json_extract(value, "$.id") as id,
json_extract(value, "$.parent_id") as parent_id,
json_extract(value, "$.name") as name,
replace(path, '%.areas%.areas', '') as path,
fullkey
from json_tree(readfile("area.json"))
where path like '%.areas';


update city
set areas_id = (select id from area where city.parent_id = area.id);


/*select city, (select(53.1950306 * 2 - 2 * (53.1950306 * geo_lon + geo_lon * 2)  + (50.1069518 * 2 - 2 * 50.1069518 * geo_lon + geo_lon * 2))) as distance
from city
order by 2 DESC
limit 3;*/


