# ui-web-app-reactjs
UI app to access microservices through API Gateway.
Developed in React.js

## Build Instruction
```
npm install
npm start
```

## Dockerize and Run
```
docker build -t image:tag .
docker run -d -p 8080:8080 --name ui image:tag 
```
*App runs on port **8080***
Open http://localhost:8080 in browser

