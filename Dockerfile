# Variable ENV used to decide if test packages need to be installed for local testing
ARG ENV

# Pull base image
FROM python:3.7

# Set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Create non-root user to run app
RUN groupadd admin -g 1000
RUN useradd -ms /bin/bash admin -u 1000 -g 1000

# Setup working directory
WORKDIR /code

RUN chown -R admin:admin /code
RUN chmod 755 /code

# Copy project
COPY . /code/

# Install dependancies
RUN if [ "$ENV" = "production" ]; then pip install pipenv && pipenv install --system; \
else pip install pipenv && pipenv install --dev --system ; fi

# Change to admin user
USER admin
