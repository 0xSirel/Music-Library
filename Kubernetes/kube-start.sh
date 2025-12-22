kubectl apply -f namespace.yaml

kubectl apply -f env-mongo-secret.yaml
kubectl apply -f env-music-library-configmap.yaml
kubectl apply -f music-library-secrets.yaml

kubectl apply -f mongo-headless-service.yaml
kubectl apply -f music-library-service.yaml
kubectl apply -f load-balancer.yaml

kubectl apply -f mongo-deployment.yaml

kubectl apply -f music-library-deployment.yaml

kubectl apply -f music-library-HPA.yaml
kubectl apply -f music-library-PDB.yaml

kubectl apply -f network-policy.yaml