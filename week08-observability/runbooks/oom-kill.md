# Runbook: OOMKilled Pod

## Alert
Pod status shows OOMKilled

## What is OOMKilled?
Linux kernel killed the container because it exceeded its memory limit.
The pod will restart automatically.

## Diagnosis steps
1. Confirm OOMKill:
   kubectl describe pod POD_NAME | grep -i oom

2. Check memory usage trend:
   kubectl top pod POD_NAME

3. Check memory limits:
   kubectl get pod POD_NAME -o jsonpath='{.spec.containers[*].resources}'

## Resolution
1. Increase memory limit:
   kubectl set resources deployment NAME --limits=memory=512Mi

2. Or update values.yaml in Helm chart and redeploy

3. Investigate memory leak in application code

## Prevention
- Always set memory requests AND limits
- Monitor memory trends in Grafana
- Set up HighMemoryUsage alert (already done!)
