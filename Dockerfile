# Pull python base image
FROM python:3.10-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y install libpq-dev gcc && apt-get install git -y --no-install-recommends
    
# Installing requirements
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt && pip install pylint-django==2.3.0

# Copy Project to the container
RUN mkdir -p /fyle-partner-dashboard-api
COPY . /fyle-partner-dashboard-api/
WORKDIR /fyle-partner-dashboard-api

# Do linting checks
RUN pylint --load-plugins pylint_django --rcfile=.pylintrc **/**.py

#================================================================
# Set default GID if not provided during build
#================================================================
ARG SERVICE_GID=1001

#================================================================
# Setup non-root user and permissions
#================================================================
RUN groupadd -r -g ${SERVICE_GID} partner_dashboard_api_service && \
    useradd -r -g partner_dashboard_api_service partner_dashboard_api_user && \
    chown -R partner_dashboard_api_user:partner_dashboard_api_service /fyle-partner-dashboard-api

# Switch to non-root user
USER partner_dashboard_api_user

# Expose development port
EXPOSE 8000

# Run development server
CMD /bin/bash run.sh
