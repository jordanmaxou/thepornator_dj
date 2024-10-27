# The pornator :eggplant:
The best porn website ever in django. :underage: :woman: :heart: :massage: :kiss: :sweat_drops:

## Init project
1. Install mkcert and create self-signed certificate according to have TLS in local :key:
```bash
mkcert -install # just once
mkcert -cert-file devops/reverse-proxy/development/certs/local-cert.pem -key-file devops/reverse-proxy/development/certs/local-key.pem "docker.localhost" "*.docker.localhost"
```
2. Start the project :rocket:
```bash
./compose up -d
```

3. Create media bucket on minio server if not exists

## TODO
- [ ] statics and medias subdomaines to path
- [ ] ruff config
- [ ] mypy config
- [ ] lint command
