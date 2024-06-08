FROM golang:1.22-alpine AS build
LABEL authors="avugar"

WORKDIR /app
COPY . .

RUN go mod download
RUN go build -o /app/cmd/app.exe /app/cmd/main.go

FROM alpine:latest

WORKDIR /app
COPY .env .
COPY --from=build /app/cmd/app.exe .

CMD ["./app.exe"]