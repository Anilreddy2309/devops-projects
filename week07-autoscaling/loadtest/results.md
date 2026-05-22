# Load Test Results

## HPA Scale-up Behavior
| Time | CPU Usage | Replicas |
|------|-----------|----------|
| 0s   | 0%        | 1        |
| 15s  | 66%       | 2        |
| 75s  | 142%      | 3        |
| 90s  | 97%       | 4        |
| 105s | 74%       | 5        |
| 120s | 74%       | 6        |

## Observations
- Scale up triggered at 66% CPU (above 50% threshold)
- HPA scaled from 1 → 6 pods in under 2 minutes
- Scale down takes ~5 minutes (stabilization window)
- CPU distributed across pods as replicas increased

## Key Learnings
- HPA formula: desired = ceil(current × currentCPU / targetCPU)
- Scale up fast, scale down slow — prevents flapping
- metrics-server required for HPA to function
