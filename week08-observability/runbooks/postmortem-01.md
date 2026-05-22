# Postmortem: ArgoCD ApplicationSet Controller CrashLoop

## Date
2026-05-22

## Severity
SEV2 — ArgoCD ApplicationSet feature unavailable

## Duration
~2 hours (since ArgoCD installation)

## Detected by
PodCrashLooping Prometheus alert firing in Grafana

## Root Cause
The ApplicationSet CRD failed to install during ArgoCD setup due to
metadata annotation size exceeding Kubernetes limit (262144 bytes).
The applicationset-controller pod requires this CRD to start — without
it, the pod crashes every 2 minutes in a CrashLoopBackOff cycle.

## Timeline
- 13:11 — ArgoCD installed, CRD install warning observed but ignored
- 15:39 — PodCrashLooping alert fires in Grafana
- 15:43 — Root cause identified via kubectl logs
- 15:45 — Fix applied

## Fix
kubectl apply -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/crds/applicationset-crd.yaml

## Lessons Learned
1. Never ignore installation warnings — the CRD warning was a signal
2. Alerting worked correctly — Prometheus caught the crash loop
3. Structured logs made diagnosis fast (JSON logs with error field)

## Action Items
- Add CRD health check to post-install verification script
- Document CRD size limitation for future ArgoCD upgrades
