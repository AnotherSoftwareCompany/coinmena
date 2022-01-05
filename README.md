Simple Exchange rate tracker
------


to run
--

```
docker-compose up
```



to add data
--

```
using docker
------------
docker exec -it app <command>


run these
---------
python manage.py add_coin  Dollar  USD

python manage.py add_coin  Bitcoin  BTC



python manage.py add_coin_pair BTC USD
```


to test
---------

- Fetch last five prices 

```bash
curl localhost:8000/api/v1/quotes/ | json_pp
```

```json
[
   {
      "created_at" : "2022-01-05T15:29:32.643575",
      "pair" : "BTC/USD",
      "price" : "46752.41"
   },
   {
      "created_at" : "2022-01-05T15:29:22.788692",
      "pair" : "BTC/USD",
      "price" : "46752.41"
   },
   {
      "created_at" : "2022-01-05T15:29:13.022370",
      "price" : "46752.41",
      "pair" : "BTC/USD"
   },
   {
      "created_at" : "2022-01-05T15:29:02.682029",
      "pair" : "BTC/USD",
      "price" : "46752.41"
   },
   {
      "created_at" : "2022-01-05T15:28:05.192983",
      "price" : "46710.76",
      "pair" : "BTC/USD"
   }
]

```



- Force request API data

```bash
curl -X POST localhost:8000/api/v1/quotes/ | json_pp
```


```json
{
   "success" : true
}

```