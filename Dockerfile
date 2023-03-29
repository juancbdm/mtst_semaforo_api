FROM node:19-alpine3.16
WORKDIR /usr/src/app
COPY . .
RUN npm install
EXPOSE 80
CMD ["npm","start"]
