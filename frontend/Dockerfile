ARG NODE_VERSION=20.18.0
ARG NODE_ENV
ARG VITE_API_URL

# Create build stage
FROM node:${NODE_VERSION}-slim AS build-stage

# Enable pnpm
ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable

RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and pnpm-lock.yaml files to the working directory
COPY ./package.json /app/
COPY ./pnpm-lock.yaml /app/

## Install dependencies
RUN pnpm install --shamefully-hoist
RUN pnpm add axios

# Copy the rest of the application files to the working directory
#COPY . ./

# Build the application

EXPOSE 3000

CMD ["pnpm","dev","-o","--debug"]
# Start the application