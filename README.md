# The pornator :eggplant:

The best porn website ever in django. :underage: :woman: :heart: :massage: :kiss: :sweat_drops:

## Init project

1. Install formatter/linter globaly for pre-commit

```bash
pip install pre-commit
pip install ruff==1.7.0
pre-commit install # will trigger format/lint each time project is commit
```

2. Install mkcert and create self-signed certificate according to have TLS in local :key:

```bash
mkcert -install # just once
mkcert -cert-file devops/reverse-proxy/development/certs/local-cert.pem -key-file devops/reverse-proxy/development/certs/local-key.pem "docker.localhost" "*.docker.localhost"
```

3. Start the project :rocket:

```bash
./compose up -d
```

4. Create media bucket on minio server if not exists

Use [minio admin panel](https://minio-admin.pornator.localhost) to create 'pornator' bucket set permissions to public.

> [!CAUTION]
> In production, it will be important to restrict permission to readonly because public means everybody can put/set/delete.

# DB object

[https://github.com/jordanmaxou/thepornator/blob/master/php/\_object.php](https://github.com/jordanmaxou/thepornator/blob/master/php/_object.php)

# TODO

- vote system on ai pic detail page
- Edit categories on ai pic detail page
- create ads feature to administrate them
- pastille
- sitemap
- search engine
- ia pictures import
- fix tags mess (understand nothing about that)
- vote up/vote down
