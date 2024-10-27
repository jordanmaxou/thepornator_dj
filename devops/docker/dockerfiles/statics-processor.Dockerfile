FROM node:alpine

RUN npm install -g webpack webpack-cli

WORKDIR /home/node

ENTRYPOINT [ "npx", "webpack" ]
CMD ["--mode", "development", "--watch" ]
