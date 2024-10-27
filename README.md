# thepornator_dj
rebuild thepornator in django


## Generate a certificate to *.docker.localhost subdomains
```bash
# If it's the firt install of mkcert, run
mkcert -install

# Generate certificate for domain "docker.localhost", "domain.local" and their sub-domains
mkcert -cert-file devops/reverse-proxy/development/certs/local-cert.pem -key-file devops/reverse-proxy/development/certs/local-key.pem "docker.localhost" "*.docker.localhost"
```

## Poetry, the package manager
We use [poetry](https://python-poetry.org) as package manager.

Install dependencies
```bash
poetry install
```

Add a dependency
```bash
poetry add <package-name>
```
