module github.com/observability-platform/identity-go

go 1.23

require (
	github.com/golang-jwt/jwt/v5 v5.2.1
	google.golang.org/grpc v1.64.0
	google.golang.org/protobuf v1.34.1
	go.opentelemetry.io/otel v1.27.0
	go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc v1.27.0
	go.opentelemetry.io/otel/sdk v1.27.0
	go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc v0.52.0
)
