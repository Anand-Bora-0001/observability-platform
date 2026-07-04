FROM golang:1.23-alpine AS builder

WORKDIR /app
# We will copy the go.mod and go.sum when they exist
# COPY go.mod go.sum ./
# RUN go mod download

COPY . .
# RUN CGO_ENABLED=0 GOOS=linux go build -o identity-service ./cmd/server

FROM alpine:latest
WORKDIR /app
# COPY --from=builder /app/identity-service .
EXPOSE 50051
# CMD ["./identity-service"]
