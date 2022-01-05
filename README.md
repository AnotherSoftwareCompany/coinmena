Simple Exchange rate tracker
------


To run
--

```
docker-compose up
```



To add data
------------

```
using docker
------------
docker-compose exec  app <command>


run these
---------
python manage.py add_coin  Dollar  USD

python manage.py add_coin  Bitcoin  BTC



python manage.py add_coin_pair BTC USD
```


To test
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


You will need authentication
--------

- create a user
```
docker-compose exec  app python manage.py createsuperuser
```

- create a token
```bash
docker-compose exec app python manage.py drf_create_token <username>
```

```bash
curl -H "Authorization: Token <token>" localhost:8000/api/v1/quotes/
```