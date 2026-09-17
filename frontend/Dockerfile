#multistage build
#Install dependencies

FROM node:20-alpine AS deps

WORKDIR /frontend

COPY  package.json package-lock.json ./

RUN npm ci

# Build statge
FROM node:20-alpine AS builder

WORKDIR /frontend

COPY --from=deps /frontend/node_modules ./node_modules

COPY . .

RUN npm run build

#Production stage
FROM node:20-alpine AS runner

WORKDIR /frontend

ENV NODE_ENV=production

COPY --from=builder /frontend/public ./public
COPY --from=builder /frontend/.next/ ./.next
COPY --from=builder /frontend/node_modules ./node_modules
COPY --from=builder /frontend/package.json ./package.json


EXPOSE 3000

CMD [ "npm", "start" ]
