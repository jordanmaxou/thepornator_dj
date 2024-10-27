FROM node:alpine

RUN npm install -g webpack webpack-cli

WORKDIR /home/node

COPY . .

ENTRYPOINT [ "npx", "webpack" ]
CMD ["--mode", "development", "--watch" ]
