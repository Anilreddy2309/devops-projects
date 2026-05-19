# ---- STAGE 1: Builder ----
# Full Node image with npm and build tools
# We use this ONLY to install dependencies
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

# ---- STAGE 2: Final image ----
# Slim clean image — no build tools, smaller and safer
FROM node:20-alpine
WORKDIR /app

# Copy ONLY the installed packages from builder stage
# Not the build tools — just the result
COPY --from=builder /app/node_modules ./node_modules
COPY app.js .

# Create a non-root user — never run apps as root
# If a hacker gets in, they get limited access
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

EXPOSE 3000

# Health check — Docker marks container unhealthy if this fails
HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget -qO- http://localhost:3000/health || exit 1

CMD ["node", "app.js"]
