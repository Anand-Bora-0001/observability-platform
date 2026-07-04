package auth

import (
	"context"
	"errors"
	"fmt"
	"time"

	"github.com/golang-jwt/jwt/v5"
	"github.com/observability-platform/identity-go/pb"
)

var jwtSecret = []byte("super-secret-enterprise-key") // In production, load from Vault/Env

type AuthService struct {
	pb.UnimplementedAuthServiceServer
}

func NewAuthService() *AuthService {
	return &AuthService{}
}

func (s *AuthService) ValidateToken(ctx context.Context, req *pb.ValidateTokenRequest) (*pb.ValidateTokenResponse, error) {
	tokenString := req.GetToken()
	if tokenString == "" {
		return &pb.ValidateTokenResponse{
			IsValid:      false,
			ErrorMessage: "token is empty",
		}, nil
	}

	token, err := jwt.Parse(tokenString, func(token *jwt.Token) (interface{}, error) {
		if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
			return nil, fmt.Errorf("unexpected signing method: %v", token.Header["alg"])
		}
		return jwtSecret, nil
	})

	if err != nil || !token.Valid {
		return &pb.ValidateTokenResponse{
			IsValid:      false,
			ErrorMessage: "invalid token",
		}, nil
	}

	claims, ok := token.Claims.(jwt.MapClaims)
	if !ok {
		return &pb.ValidateTokenResponse{
			IsValid:      false,
			ErrorMessage: "invalid claims",
		}, nil
	}

	// Extract standard claims
	userId, _ := claims["sub"].(string)
	email, _ := claims["email"].(string)
	orgId, _ := claims["org_id"].(string)

	// Extract roles (assuming string slice in JWT)
	var roles []string
	if rawRoles, ok := claims["roles"].([]interface{}); ok {
		for _, r := range rawRoles {
			if strRole, isStr := r.(string); isStr {
				roles = append(roles, strRole)
			}
		}
	}

	return &pb.ValidateTokenResponse{
		IsValid:        true,
		UserId:         userId,
		Email:          email,
		Roles:          roles,
		OrganizationId: orgId,
	}, nil
}

func (s *AuthService) CheckPermission(ctx context.Context, req *pb.CheckPermissionRequest) (*pb.CheckPermissionResponse, error) {
	// Simple mock RBAC/ABAC logic
	// In reality, this would check a Casbin enforcer, OPA policy, or DB.
	
	if req.GetUserId() == "" {
		return nil, errors.New("user_id required")
	}

	// For MVP: if the user asks for "admin" action on "system", allow it.
	// We assume validation is done upstream and token is good.
	if req.GetAction() == "admin" {
		return &pb.CheckPermissionResponse{
			Allowed: true,
			Reason:  "mock allow for admin",
		}, nil
	}

	return &pb.CheckPermissionResponse{
		Allowed: true,
		Reason:  "default allow",
	}, nil
}

// GenerateToken is a helper func for creating a valid JWT (e.g. on login)
func GenerateToken(userID, email, orgID string, roles []string) (string, error) {
	claims := jwt.MapClaims{
		"sub":    userID,
		"email":  email,
		"org_id": orgID,
		"roles":  roles,
		"exp":    time.Now().Add(time.Hour * 24).Unix(),
		"iat":    time.Now().Unix(),
	}

	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
	return token.SignedString(jwtSecret)
}
