ARG NODE_VERSION=22.13.1
ARG NODE_ENV
ARG VITE_API_URL

# Create build stage
FROM node:${NODE_VERSION}-slim AS build-stage

# Remove yarn-specific cache configuration
RUN apt-get clean
RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

 
# Copy package.json and package-lock.json files to the working directory
COPY ./package.json /app/
COPY ./package-lock.json /app/

## Install dependencies
#RUN npm install

# Copy the rest of the application files to the working directory
#COPY . ./

# Copy the script to the container
COPY ./scripts/generate-env.sh /app/generate-env.sh

# Make the script executable
RUN chmod +x /app/generate-env.sh

# Run the script to generate the .env file
RUN /app/generate-env.sh

# Build the application

EXPOSE 3000

#CMD ["pnpm","dev","-o","--debug"]
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "3000"]
# Start the application