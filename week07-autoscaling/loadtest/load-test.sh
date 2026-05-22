#!/bin/bash
echo "Starting load test..."
kubectl run load-generator \
  --image=busybox:latest \
  --restart=Never \
  -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://php-apache; done"

echo "Watching HPA scale up (press Ctrl+C to stop)..."
kubectl get hpa --watch
