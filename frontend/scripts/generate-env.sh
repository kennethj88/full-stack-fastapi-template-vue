# generate-env.sh
#!/bin/sh

# Create a .env file from environment variables
echo "VITE_API_URL=${VITE_API_URL}" > /app/.env
echo "NODE_ENV=${NODE_ENV}" >> /app/.env
echo "GOOGLE_CLIENT_ID=${GOOGLE_CLIENT_ID}" >> /app/.env
echo "UMAMI_WEBSITE_ID=${UMAMI_WEBSITE_ID}" >> /app/.env
echo "KLAVIYO_COMPANY_ID=${KLAVIYO_COMPANY_ID}" >> /app/.env
echo "SENTRY_DSN=${SENTRY_DSN}" >> /app/.env
echo "SENTRY_AUTH_TOKEN=${SENTRY_AUTH_TOKEN}" >> /app/.env