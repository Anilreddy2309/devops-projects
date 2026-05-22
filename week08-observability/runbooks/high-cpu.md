# Runbook: High CPU Usage

## Alert
HighCPUUsage — CPU above 80% for 2+ minutes

## Impact
- Slow response times
- Potential pod evictions
- User-facing degradation

## Diagnosis steps
1. Check which pods are consuming CPU:
   kubectl top pods -A --sort-by=cpu | head -10

2. Check node CPU:
   kubectl top nodes

3. Check if HPA is scaling:
   kubectl get hpa -A

4. Check recent deployments (did anything change?):
   kubectl rollout history deployment -A

## Resolution
- If a specific pod is spiking → check its logs: kubectl logs POD_NAME
- If all pods are high → scale up nodes or trigger HPA
- If recent deployment caused it → rollback: kubectl rollout undo deployment/NAME

## Escalation
If not resolved in 15 minutes → page on-call engineer
