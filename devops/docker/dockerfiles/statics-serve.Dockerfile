FROM node:alpine AS builder

RUN npm install -g webpack webpack-cli

WORKDIR /home/node

COPY . .

RUN npx webpack --mode production

#############################################################################
FROM nginx:alpine AS serve

WORKDIR /usr/share/nginx/html

COPY --from=builder /home/node/dist .
