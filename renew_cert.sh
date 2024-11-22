#!/bin/sh

# Run Certbot renewal
certbot renew --quiet --post-hook "nginx -s reload"