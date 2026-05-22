# Runbook: Pod CrashLooping

## Alert
PodCrashLooping — pod restarting repeatedly

## Impact
- Service degraded or unavailable
- Users seeing errors

## Diagnosis steps
1. Find the crashing pod:
   kubectl get pods -A | grep -v Running

2. Check why it crashed:
   kubectl describe pod POD_NAME -n NAMESPACE
   kubectl logs POD_NAME -n NAMESPACE --previous

3. Common causes:
   - OOMKilled → not enough memory, increase limits
   - Error in app code → check logs for exception
   - Missing config/secret → check env vars
   - Failed health check → check liveness probe

## Resolution
- OOMKilled: kubectl set resources deployment NAME --limits=memory=256Mi
- Bad deploy: kubectl rollout undo deployment/NAME
- Missing secret: kubectl create secret generic NAME --from-literal=key=value

## Escalation
If not resolved in 10 minutes → page on-call + notify dev team
