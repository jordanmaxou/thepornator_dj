FROM node:alpine

RUN npm install -g webpack@ webpack-cli

WORKDIR /home/node

COPY . .

RUN npm ci

ENTRYPOINT [ "tail", "-f", "/dev/null" ]
# ENTRYPOINT [ "webpack" ]
# CMD ["--mode", "development", "--watch" ]
